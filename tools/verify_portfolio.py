#!/usr/bin/env python3
"""Check documentation publication hygiene; this does not audit an application."""

from __future__ import annotations

import argparse
import ipaddress
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit

ALLOWED_SUFFIXES = {".md", ".svg", ".py", ".yml", ".yaml"}
ALLOWED_NAMES = {".gitignore"}
ALLOWED_HOSTS = {"github.com", "docs.github.com"}
IGNORED_PARTS = {".git", "__pycache__"}
PRIVATE_PARTS = {
    "private-review", "private-sources", "working-drafts", "node_modules",
    ".next", "backups", "deployment", "deploy",
}
PATTERNS = (
    ("private-key material", re.compile(r"-----BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-----")),
    ("GitHub access token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b")),
    ("cloud access key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("JWT-like credential", re.compile(r"\beyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b")),
    ("database credential URL", re.compile(r"(?:postgres(?:ql)?|mysql|redis)://[^/\s:@]+:[^/\s@]+@", re.I)),
    ("non-English portfolio text", re.compile(r"[\u0600-\u06ff]")),
)
LINKS = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")
FENCES = re.compile(r"\x60{3}.*?\x60{3}|~~~.*?~~~", re.S)
IP_CANDIDATES = re.compile(r"(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])")


def verify(root: Path) -> dict:
    errors: list[str] = []
    files = []
    local_links = 0
    external_links = 0

    def error(path: Path, message: str) -> None:
        # Never include matched credentials in error messages.
        errors.append(f"{path.relative_to(root).as_posix()}: {message}")

    if not root.is_dir():
        return {"ok": False, "errors": ["Repository root does not exist"]}
    if not (root / "README.md").is_file():
        errors.append("README.md: repository overview missing")

    for path in sorted(root.rglob("*")):
        parts = path.relative_to(root).parts
        if IGNORED_PARTS.intersection(parts) or path.suffix == ".pyc":
            continue
        if path.is_symlink():
            error(path, "symlinks require separate review")
            continue
        if path.is_dir():
            continue
        files.append(path)
        if PRIVATE_PARTS.intersection(parts):
            error(path, "private or operational directory in publication tree")
        if path.name.startswith(".env") or (
            path.name not in ALLOWED_NAMES and path.suffix not in ALLOWED_SUFFIXES
        ):
            error(path, "file type outside the documentation allowlist")
            continue
        if path.stat().st_size > 1024 * 1024:
            error(path, "file exceeds documentation size limit")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeError:
            error(path, "not UTF-8 text")
            continue

        for label, pattern in PATTERNS:
            match = pattern.search(text)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                error(path, f"{label} detected at line {line}")
        for match in IP_CANDIDATES.finditer(text):
            try:
                address = ipaddress.ip_address(match.group())
            except ValueError:
                continue
            if not address.is_loopback:
                line = text.count("\n", 0, match.start()) + 1
                error(path, f"IP address requires manual review at line {line}")

        if path.suffix == ".svg":
            try:
                tree = ET.fromstring(text)
            except ET.ParseError:
                error(path, "invalid SVG XML")
                continue
            for element in tree.iter():
                name = element.tag.rsplit("}", 1)[-1].lower()
                if name in {"script", "foreignobject", "image", "use"}:
                    error(path, "active or externally referenced SVG element")
                for attr in element.attrib:
                    short = attr.rsplit("}", 1)[-1].lower()
                    if short == "href" or short.startswith("on"):
                        error(path, "active SVG attribute")

        if path.suffix != ".md":
            continue
        prose = FENCES.sub("", text)
        for match in LINKS.finditer(prose):
            target = match.group(1).strip().split(" ", 1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                external_links += 1
                if parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS:
                    error(path, "external link outside the reviewed host allowlist")
                continue
            if not parsed.path:
                # Anchor names are not checked by this script.
                continue
            local_links += 1
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(root):
                error(path, "local link leaves repository root")
            elif not destination.is_file():
                error(path, "local Markdown file link does not resolve")

    return {
        "ok": not errors,
        "files_checked": len(files),
        "local_file_links_checked": local_links,
        "external_links_reviewed_by_host_only": external_links,
        "errors": errors,
        "scope": "Documentation hygiene; no remote links, anchors, application tests, or security audit",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    report = verify(args.root.resolve())
    print(json.dumps(report, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
