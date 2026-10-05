# Abnar OS — Agency Workflow Prototype

**Exploring the relationship between requests, task ownership, capacity, and quality review.**

| | |
| --- | --- |
| Product stage | Interface and workflow prototype |
| Audience | Agency operators, project managers, department managers, reviewers, and clients |
| My contribution | Product requirements, domain modeling, interface flows, and AI-assisted prototyping |
| Stack | TypeScript, React, Vite, Tailwind CSS, and browser-backed state |
| Evidence | Source reviewed on 5 October 2026 at revision `73c2984`; application not executed in this review |

## The problem being explored

A project manager owns delivery priorities, while a department manager owns people and capacity. A task may look complete to its creator but still need review before the client receives it. A useful operational product needs to represent those relationships clearly.

This prototype explores the product model and interfaces before treating the full production architecture as implemented.

## What the prototype contains

The reviewed React implementation includes executive and daily-work views, requests, tasks, projects, CRM, finance views, time tracking, performance, quality review, and a client portal. A central typed store holds sample entities and uses browser local storage for persistence.

Concrete workflow behaviors include requiring acceptance criteria before a task becomes ready, converting a reviewed request into a task, creating a quality-review record when appropriate, and recording review or override events in the prototype's audit model.

## Product decisions

**Separate priority from capacity.** Project and department responsibilities are modeled independently so the interface can explain who owns the deadline and who assigns people.

**Make quality review a state transition.** Delivery should include explicit acceptance and review, not only a completed checkbox. Revision reasons and override rationale make exceptions visible.

**Prototype the complete journey.** Connecting request, assignment, review, and client-facing delivery helps reveal gaps that isolated dashboard mockups can hide.

## Implementation boundary

Preview adapters and interfaces for storage, queues, bots, and monitoring exist. The reviewed production-labeled adapters do not complete the actual external integrations. The source does not establish a working PostgreSQL backend, real BullMQ processing, real S3 uploads, production messaging, or durable server-side authorization.

Browser-side permissions and audit records are useful for exploring the interface. Production authorization and trustworthy audit history require server enforcement and durable storage. This prototype is therefore presented as product exploration, not as a deployed enterprise system or a blockchain implementation.

## Moving toward a releasable product

A practical first release would narrow the scope to request → assignment → deliverable → review. It would add authenticated server-side records, role and record-scope checks, durable file handling, and tests for denied access and invalid state transitions.

That is a proposed development direction. It is not an implemented feature list or a commitment to a specific future product.

[Portfolio](../../README.md) · [Verification scope](../../engineering/verification.md)
