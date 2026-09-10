# Shared artifact templates

Store reusable source templates here. Rendered plots, populated decks, reports, tables, and diagrams belong under `scenarios/<name>/output/<run_id>/`.

```text
templates/
  registry.json
  plots/             # Future .mplstyle, Plotly themes, plotting specifications
  presentations/     # Future .potx/.pptx masters and slide specifications
  reports/           # Future Word, LaTeX, Markdown, HTML report sources
  tables/            # Future spreadsheet and table-layout templates
  diagrams/          # Future SVG/Mermaid/design sources
  scenarios/basic/   # Current local-project scaffold
```

For each added template, provide a subfolder and README with ID, version, purpose, required inputs, units, rendering dependencies/command, output formats, attribution, and a preview or validation example when available. Register actual usable templates in `registry.json`; do not register an empty folder as ready.

Keep engine models, propagation settings, and mission numerical assumptions out of presentation templates. A plot template defines style and labels, not fabricated analysis data. Do not overwrite template sources while rendering. Record template ID/version alongside the run inputs.

Only `scenario-basic` is implemented in this starter. Artifact folders are reserved for future additions, as requested; no finished plot, slide deck, or report template is claimed yet.
