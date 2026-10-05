# Rahbar security and quality

This page describes controls observed in the reviewed source and the questions used to evaluate them. It is not a security certification.

| Area | Observed implementation | Verification priority |
| --- | --- | --- |
| Identity and sessions | Authentication, rotating refresh sessions, session policies, and revocation behavior | Expiry, reuse, concurrent refresh, and logout |
| Authorization | Permission checks, project scope, and domain-specific access rules | Cross-user and cross-project denial; permissions revoked between planning and execution |
| Assistant actions | Allowed action catalog, structured plan validation, clarification, and confirmation | Unsupported mutations, malformed plans, ambiguous entities, and provider failures |
| Finance | Integer money, journal balance checks, posted-record constraints, and period locks | Partial settlement, reversals, transactions, and concurrency |
| Files and imports | Server-side handling, storage abstraction, background processing, and dedicated tests | Scope, validation, invalid files, and failure recovery |
| Workflow history | Audit records and explicit business state transitions | Actor attribution and consistency between related records |
| Releases | Automated build/test gates, acceptance checks, and documented data preservation | Restore rehearsal, migration review, and rollback behavior |

## Evidence

Tests are present for selected business rules and access boundaries. A successful GitHub Actions deployment run was observed for the reviewed revision, including its configured quality and acceptance gates.

The review did not independently reproduce the complete application test environment, inspect live customer records, perform a penetration test, or establish comprehensive coverage. A passed CI run is evidence for that revision and configuration; it does not establish the absence of defects.

[Verification status](verification-status.md) · [Publication scope](../../SECURITY.md) · [Case study](README.md)
