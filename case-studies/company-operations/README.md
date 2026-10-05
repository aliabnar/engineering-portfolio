# Rahbar — Company Operations

**An operational workspace connecting people, requests, approvals, sales activity, and financial records.**

| | |
| --- | --- |
| Product | Private, self-hosted company operating system |
| Users | Employees, managers, HR, sales operations, and finance |
| My contribution | Product definition, business rules, workflow design, AI-assisted implementation, and iteration |
| Stack | TypeScript, Next.js 16, NestJS 11, PostgreSQL/Prisma, Redis/BullMQ, MinIO |
| Evidence | Current source reviewed; successful GitHub deployment workflow observed on 5 October 2026 |

## The business problem

An employee submits a request in one tool, a manager approves it in a message, HR updates a record elsewhere, and finance later reconstructs the history. Tasks and sales follow-ups face the same problem: ownership and state are scattered.

Rahbar brings those workflows into one application. A request has an accountable actor, an explicit state, a decision history, and consequences for downstream work.

## Product scope

The reviewed implementation includes employee records, attendance and leave workflows, delegated approvals, tasks, projects, CRM activity, expenses, invoicing, payroll, and journal entries. The Persian RTL interface includes a shared Jalali date input while the API and data store use Gregorian/UTC values.

Structured screens and a conversational assistant offer two entry points to the same application rules.

## A representative workflow

1. An employee requests leave through a screen or a Persian message.
2. The application resolves the employee and relevant dates, checks the applicable policy, and asks for missing information.
3. The employee reviews the proposed request before submission when confirmation is required.
4. The approval workflow routes the request to an authorized decision maker, including supported delegation.
5. The resulting decision updates the request history and relevant leave records.

This is a product-level walkthrough of the inspected implementation. It contains no live employee data.

## Decisions that shaped the system

**Keep the assistant inside business boundaries.** Simple commands use a local intent router. More complex Persian requests can use the OpenAI Responses API with Structured Outputs. The model proposes an action plan from an allowed catalog; application code handles permissions, entity resolution, validation, and confirmation. Unsupported or ambiguous requests have explicit fallback or clarification paths.

**Treat financial events as domain operations.** Money uses integer arithmetic. Financial actions generate journal entries, and the data model includes balancing checks, immutable posted lines, and closed-period restrictions. Corrections use reversal or void workflows rather than silently replacing financial history.

**Separate interactive work from background processing.** A modular API handles the business transaction; queues and a separate worker handle background work such as imports. PostgreSQL remains the source of business records, while object storage holds files.

[Product decisions and trade-offs](product-decisions.md) · [Architecture](architecture.md)

## Delivery and verification

The inspected source includes unit and acceptance tests for business rules, access, sessions, files, imports, finance, and assistant workflows. On 5 October 2026, the latest commit's GitHub Actions deployment run was observed as successful. Its workflow includes build, lint, unit tests, infrastructure acceptance, and deployment acceptance gates.

This is evidence from the existing CI run, not a fresh independent production audit. [Detailed verification scope](verification-status.md) · [Security and quality](security-and-quality.md)

## Business value

The product makes work traceable across departments and gives the assistant a useful role without handing business authority to the model. Quantified business impact has not been established for this case study.

Measures worth tracking include approval turnaround, overdue requests, follow-up completion, payroll corrections, and the time spent reconstructing a decision's history.

[Portfolio](../../README.md)
