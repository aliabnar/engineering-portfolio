# My approach to AI-assisted development

AI tools support implementation, refactoring, test drafting, and technical exploration. I remain responsible for choosing the product behavior, understanding the system boundaries, reviewing the changes, and deciding what the available evidence supports.

This document describes my engineering approach. It is not a retrospective claim that every historical change completed every gate below.

## A workflow I can explain and defend

1. **Define the behavior.** State the user problem, business rule, and acceptance criteria before asking for implementation.
2. **Set boundaries.** Identify which records the actor may access, what can be changed, and which actions require approval.
3. **Build an inspectable change.** Prefer a bounded patch whose effects can be understood.
4. **Review the implementation.** Check data access, side effects, error paths, assumptions, and whether the code matches the requirement.
5. **Verify the important behavior.** Use tests and execution evidence appropriate to the change.
6. **Record the decision.** Document material trade-offs, verification results, and remaining limitations.

## Areas requiring particular judgment

Access control, financial calculations, retries, data migrations, file handling, and AI tool execution affect more than whether a screen renders correctly.

For those areas, compilation is only one check. The useful questions are whether the wrong actor can perform the action, whether invalid state is rejected, and what happens if execution fails halfway through.

## Evidence belongs to a version

Test results should identify the version and environment tested. A suggested test is not an executed test. A passing isolated test is not proof of a complete production workflow.

The commercial case study's [verification status](../case-studies/company-operations/verification-status.md) follows that distinction.
