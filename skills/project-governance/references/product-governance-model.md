# Product Governance Model

Use this lightweight model when a project has many flat goals or requirements that conflict.

## Record types and hierarchy

Keep these types distinct:

```text
Goal → Story Map outcome/activity/task → Capability or requirement → Verification
```

Cross-cutting constraints (security, legal, data guarantees, accessibility, cost, and operations) are gates on every lower-level item. A solution or implementation task is never a peer goal.

A requirement must link to at least one story-map item or an explicit constraint. A capability must state the user outcome it serves. A verification item must state which requirement or acceptance criterion it proves. Use a graph when one item supports multiple goals.

## Story Map and ADR responsibilities

Use User Story Mapping to organize the user's path: outcome, activities, tasks, capabilities, and release slices. Preserve normal and exception paths and make the smallest valuable slice visible.

Use an Architecture Decision Record (ADR) when a choice changes user-visible behavior, permissions, data guarantees, compatibility, operational burden, or a cross-cutting constraint. An ADR records context, options, decision, rationale, consequences, and links to affected story-map items and requirements.

## Conflict procedure

1. Classify both items as goal, story-map item, requirement, constraint, or solution.
2. Reject options that violate a hard constraint.
3. Trace the remaining items to their nearest shared outcome.
4. Prefer the option that best satisfies the higher-level outcome and acceptance evidence.
5. Record material trade-offs in an ADR; do not resolve them only in chat or task priority fields.
6. Revalidate downstream requirements, release slices, and verification evidence after the decision.

Do not use numeric priority as a substitute for hierarchy. Priority orders items within a governed scope; it does not decide whether a solution is justified.
