---
name: report
description: Create GIS analysis reports, academic report sections, figure narratives, abstracts, and PDF-ready Markdown deliverables.
tags: [report, gis, academic-writing, markdown]
version: 1.0.0
---

# Report Skill

Use this skill when the user asks for a GIS report, academic report, report section,
abstract, structured narrative, or PDF-ready Markdown deliverable.

## Operating Rules

- Treat report writing as a workflow, not a primitive map tool.
- Prefer `read_file`, `query_features`, `execute_code`, and ordinary file writing
  to inspect data, generate figures, and assemble Markdown.
- Keep figures as separate image artifacts under a workspace report/output folder,
  then reference them from Markdown with relative paths.
- Do not use layout composer tools. Layout composition is a manual UI workflow.
- For long reports, write incrementally to files instead of returning the full
  report in chat.
- When producing academic text, preserve factual uncertainty. If source data does
  not support a claim, say so rather than inventing a region, event, metric, or
  conclusion.

## Suggested Report Structure

1. Title and short executive summary.
2. Data and methods.
3. Key spatial/statistical findings.
4. Figures and map interpretation.
5. Limitations.
6. Conclusion and next steps.

## Output Contract

For a full report, produce:

- `report.md` in a clear workspace folder, such as `output/report/`.
- Figure files under `output/report/figures/`.
- A short chat summary with the report path and the main conclusions.

For a section-only request, update or create the target Markdown file and reply
with only the section path plus a concise summary.
