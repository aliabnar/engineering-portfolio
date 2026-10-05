# Ali Abnar
### Product-minded software engineering

**Business workflows, practical architecture, and accountable delivery.**

I build software around the people doing the work. My background in product, growth, sales, and operations informs the requirements; the implementation makes the rules, state changes, and responsibilities explicit.

This portfolio presents selected commercial work and a workflow prototype. Each case connects a business problem to product decisions, architecture, and dated evidence.

## Selected projects

| Project | Audience and need | Engineering focus | Status |
| --- | --- | --- | --- |
| [Rahbar — Company Operations](case-studies/company-operations/README.md) | Employees, managers, HR, sales, and finance need connected operational workflows | Modular API, financial invariants, scoped access, background jobs, and hybrid AI planning | Private source reviewed; successful deployment workflow observed |
| [Abnar Academy](case-studies/education-career-platform/README.md) | Learners and academy teams need a connected assessment-to-learning journey | Server-side assessment, resumable state, document persistence, consent, and role-specific workspaces | Active branch reviewed; CI report shows 144 passing tests |
| [Abnar OS — Workflow Prototype](case-studies/agency-workflow-prototype/README.md) | Agency teams need clear ownership, capacity, and deliverable review | Workflow modeling, acceptance gates, and interface exploration | Browser-backed prototype; production integrations incomplete |

All three were reviewed on **5 October 2026**. Commercial source, customer records, and infrastructure details stay private. [Verification scope and revisions](engineering/verification.md)

## A two-minute review

Start with [Rahbar's business problem](case-studies/company-operations/README.md), then its [architecture](case-studies/company-operations/architecture.md) and [product decisions](case-studies/company-operations/product-decisions.md).

For another product domain, explore [Abnar Academy](case-studies/education-career-platform/README.md). For early product exploration, see the [agency workflow prototype](case-studies/agency-workflow-prototype/README.md).

## What I bring to a project

- **Product judgment:** translate an operational need into workflows, constraints, and acceptance criteria.
- **Business context:** connect implementation to adoption, process ownership, and a useful outcome.
- **Full-stack implementation:** work across React interfaces, TypeScript services, data models, and integrations.
- **Delivery discipline:** document trade-offs, verify critical behavior, and preserve business data across releases.

[Review guide](engineering/review-guide.md) · [AI-assisted development](engineering/ai-assisted-development.md) · [Evidence policy](engineering/evidence-policy.md) · [Publication scope](SECURITY.md)

## Other work

A private personal website includes a contact workflow and an administration interface. An earlier [public real-estate landing page](https://github.com/aliabnar/houseforsalerealtor) demonstrates a small HTML/CSS lead-capture interface. Its reviewed source contains a contact form; an AI valuation engine is not implemented there.

## Working together

I am interested in remote product engineering, full-stack development, internal tools, CRM workflows, and business automation projects.

For an initial conversation, share the workflow you want to improve, who uses it, the main constraint, and what a successful first release would achieve. Use [Discussions](https://github.com/aliabnar/engineering-portfolio/discussions) for general questions without confidential information.

## Verify this documentation

```bash
python3 tools/verify_portfolio.py
```

GitHub Actions runs the same check. It validates local Markdown file links, readable text, allowed file types, and selected disclosure patterns. It does not audit the applications or verify remote links.
