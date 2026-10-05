# Technical review guide

## Start with a workflow

For Rahbar, trace an employee request from input through clarification, approval, and the resulting records. Ask which layer owns each rule and what happens when a permission changes before execution.

For Abnar Academy, trace an assessment attempt through saved state, result, enrollment, and role-specific follow-up. Ask which fields can become public, how consent changes access, and how an interrupted attempt resumes.

For Abnar OS, inspect how the prototype connects a request, assignment, acceptance criteria, and review. Keep browser-side exploration separate from the server behavior a release would require.

## Questions worth discussing

- Which rules are enforced by the interface, service, and database?
- What prevents a user from reaching another user's or project's records?
- What happens after a timeout, repeated request, malformed input, or unavailable provider?
- Which operations need a transaction, an idempotency rule, or a compensating action?
- How are migrations, persistence, backups, and rollback verified?
- Which test proves a business rule, and which important behavior remains unverified?

## Relevant reading

[Rahbar architecture](../case-studies/company-operations/architecture.md) · [Rahbar decisions](../case-studies/company-operations/product-decisions.md) · [Abnar Academy](../case-studies/education-career-platform/README.md) · [Workflow prototype](../case-studies/agency-workflow-prototype/README.md) · [Verification](verification.md)

For project conversations, begin with the user's workflow and the first release's acceptance criteria. Confidential implementation details should use an agreed private channel.

[Portfolio](../README.md)
