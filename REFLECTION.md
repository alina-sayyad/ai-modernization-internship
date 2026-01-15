# Reflection

## My Approach
I intentionally limited the scope of this project to a single ERP domain
(Sales Invoice) instead of analyzing the entire ERPNext codebase. This
allowed me to focus on understanding real business logic rather than
producing shallow analysis across many modules.

## New Concepts I Learned
- How ERPNext uses DocType JSON files to define entity schemas
- How business logic is implemented separately in Python files
- Using Python’s AST module for static code analysis
- Understanding lifecycle hooks such as `validate` and `on_submit`

## Trade-offs I Made
- Chose lightweight static analysis over deep call-graph analysis to
  ensure the project was completed end-to-end
- Focused on structured outputs (JSON, diagrams, summaries) rather than
  advanced AI or RAG features

## Challenges Faced
Navigating a large and unfamiliar ERP codebase was initially challenging.
Understanding how schema, logic, and UI files interact required careful
exploration and reading of the code.

## What I Would Improve With More Time
- Add call-graph analysis to detect deeper function relationships
- Expand analysis to multiple ERP modules
- Automatically extract and summarize business rules

## Open Questions
- How are cross-module dependencies managed at scale in ERP systems?
- How can AI assist in explaining complex business logic more effectively?
