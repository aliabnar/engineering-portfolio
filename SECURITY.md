# Security and publication scope

This repository contains portfolio documentation and a documentation checker. It is separate from commercial applications and their operating environments.

Public material is limited to business problems, product reasoning, abstract components, selected source observations, and evidence boundaries.

Production credentials, customer and employee records, internal endpoint mappings, deployment configuration, and private security findings do not belong here.

## Reporting an issue

For an issue in this documentation or the checker, open a GitHub issue that omits secrets and sensitive operating details. If a file contains a credential or personal information, do not repost its contents.

Public documentation does not authorize testing a commercial system. Security assessments of commercial applications require a separately agreed scope.

## Checker limitations

The automated checker detects selected publication mistakes. It cannot establish that every sensitive detail has been removed, that a business outcome is correct, or that the commercial software is secure. Manual review remains necessary.

The workflow uses a read-only repository token, a commit-pinned checkout action, and no deployment step.
