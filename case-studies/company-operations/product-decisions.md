# Rahbar product decisions

## One workflow, multiple entry points

A conversational interface is useful when an employee wants to perform a small action quickly. Structured screens are useful for reviewing lists, comparing records, and completing more involved work. Both should lead to the same application rules.

The alternative of a chat-only product would make some review tasks harder and would put too much responsibility on language interpretation. Separate screen-only and chat-only business logic would also invite inconsistent behavior.

Acceptance questions include whether the same request reaches the same state through either interface, whether ambiguity produces clarification, and whether revoked permissions prevent a prepared action from executing.

## AI proposes; the application decides

The current implementation combines local intent routing with optional structured model planning. This balances predictable handling of common commands with better interpretation of more complex Persian requests.

A general autonomous agent with broad database or tool access would make authorization and failure behavior harder to reason about. A bounded action catalog creates a clearer contract for validation, confirmation, and evaluation.

Useful checks include unsupported requests, model outages, invalid structured output, ambiguous names, incorrect dates, and attempts to bypass confirmation. A successful language interpretation is only one part of a successful business action.

## Explicit financial history

Invoices, expenses, receipts, and payroll affect accounting records. Modeling those effects as domain operations makes their consequences visible and testable.

Editing a posted financial record in place would obscure what happened. Reversal and void workflows preserve a clearer history, with integer money and journal constraints expressing correctness requirements.

Acceptance questions include partial payments, balanced entries, closed-period rejection, repeated actions, and the consistency of workflow state with the financial record.

## A modular application before distributed services

The implementation keeps related business modules in one API with shared data boundaries, while separating background processing. This is a practical fit for interconnected workflows maintained as one product.

Distributing every department into a service would introduce coordination and operational costs before there is evidence those boundaries need independent deployment. The current approach still requires clear service responsibilities and careful transaction handling.

## Localization as workflow behavior

Persian RTL layouts and Jalali date entry are part of usability, not an afterthought. Shared date conversion reduces inconsistent interpretation between screens, while standard API values keep storage and interoperability predictable.

Checks should cover date boundaries, user-visible labels, relative dates in chat, and whether localized entry resolves to the intended stored date.

[Case study](README.md) · [Architecture](architecture.md)
