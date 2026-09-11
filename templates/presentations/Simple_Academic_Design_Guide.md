# Simple Academic presentation style

## Reference and design findings

Based on visual review of all 21 pages of the supplied **Ch1_SI.pdf**, with font sizes and positions checked against PDF text spans. This is a design review, not verification of the lecture's technical or historical claims.

The strongest feature is a stable reading order: title, a thin horizontal rule, then one broad body area. The slides carry useful explanatory content without dividing it into many competing containers. White space remains after the readable content; it is not a reason to make text smaller, or to add decoration.

| Aspect | Observed in the reference | Reusable rule |
|---|---|---|
| Canvas | 720 × 540 PDF points; 4:3 | 10 × 7.5 inches; retain 4:3 by default |
| Background | White throughout | White |
| Main typeface | Arial / Arial Bold | Arial for Latin; a verified available Korean sans-serif for Korean |
| Cover title | 44 pt, navy | 44 pt, bold; one or two lines |
| Content title | 28 pt, navy | 28 pt, bold; normally one line |
| Body | Mostly 18–20 pt | 22 pt default; 20 pt minimum for essential prose |
| Dense figure notes | 13 pt on p. 8; 15 pt on pp. 17 and 19 | Improve to 18–20 pt for information needed during the talk |
| Page number | 11 pt, gray, bottom right | 11 pt, optional; not an essential reading element |
| Palette | Navy #1F2A44; text #222222; gray #666666; white | Same palette; use additional colors only when data require them |
| Content margins | Approximately 36 PDF points, or 0.5 inches | 0.5-inch side margins |
| Title rule | Navy, 1.5 pt; approximately y = 1.10 inches | One thin navy rule below each content title |
| Body start | Approximately y = 1.36 inches | Approximately 1.36 inches |
| Text structure | One main reading area with bullets and occasional sub-bullets | One main body placeholder; one nested level at most |
| Figures | One relevant figure, usually beside or above text | Give each figure enough space for its labels |
| Footer | Page number only | No repeated project labels, taglines, or multi-part footers |
| Logo | Small APL logo on the cover | Optional cover logo; omit or replace for other organizations |

The source is not uniformly sparse. Pages 2–4 and 21 contain substantial text, while page 20 leaves much of the lower canvas empty. The consistent typography and alignment keep both types coherent. The goal is **readable, useful content with few visual containers**, not a fixed low word count.

Some source pages should not be copied mechanically: figure notes can be small, some bullets are long, and the scanned table is not editable. The new template raises the body default, limits figure commentary, and includes a native table.

## Layout selection

| Layout | Use | Content budget and arrangement |
|---|---|---|
| Cover | Presentation title and scope | Context line, large title, short outline; optional logo |
| Title and text | Definitions, background, methods, findings | One body area; usually 3–5 points or short paragraphs |
| Text and figure | Explain one system or result | Approximately 58% text, 5% gap, 37% figure; 3–4 concise points |
| Large figure | Figure, chart, or evidence that needs inspection | Broad figure with 1–2 short observations underneath |
| Simple table | Compare exact attributes or values | Usually 3–4 columns and up to 5–6 data rows; 20 pt cells |
| Equation and explanation | Explain one relation and its assumptions | One large equation; definitions and assumptions below |

The six sample slides are layout examples, not a mandatory outline. Repeat the layout appropriate to the material. Do not force variety merely to make successive slides look different.

## Generation rules

1. Start with the substantive outline. Assign one coherent subject to each slide.
2. Duplicate the closest sample slide or use its named layout. Replace the sample content and images; do not keep the style instructions in a finished research presentation.
3. Retain the white background, Arial typography, navy title/rule, and fixed margins.
4. Use one body text area for related paragraphs or bullets. Use native bullets with hanging indents; do not create one box per bullet.
5. Set body text to 22 pt by default. A 20 pt size is allowed for moderately dense prose; do not reduce essential prose below 20 pt to fit. Use 18–20 pt for necessary figure labels and table notes. A short source credit may be 14–16 pt; move full references to notes or an appendix. Page numbers may remain 11 pt.
6. When content does not fit, shorten repeated wording, widen the main text area within the margins, rearrange the figure, or split the slide. Preserve required technical definitions and evidence. Do not silently omit requested material.
7. Avoid cards, colored panels, badges, pills, gradients, shadows, decorative icons, background illustrations, oversized section numbers, and redundant footers.
8. Default to one title, one body area, one title rule, and one optional page number. A necessary figure, table, equation, or caption may add objects; their number should follow the explanation rather than a decorative grid.
9. Use bold sparingly for meaningful terms. Keep body text near-black. For scientific data, permit additional distinguishable colors only when needed; retain labels, line styles, or markers so color is not the only distinction.
10. Prefer native tables and charts for new data. Inspect embedded figures at the size shown on the slide. Enlarge, crop only irrelevant margins, or rebuild from available source data if essential labels are unreadable. Never distort the figure or crop away evidence.
11. Preserve natural sentence explanations where useful. Do not impose a three-bullet formula or slogan-like titles. A topic title is appropriate for definitions and methods; a factual finding title is appropriate when supported.
12. Use blank space deliberately after readability is satisfied. Do not fill it with decorative elements. Do not distribute a short list into tiny disconnected regions.
13. For Korean, use an available font such as Malgun Gothic or Noto Sans CJK KR, keep the same visual hierarchy, and check actual glyph rendering and line breaks. Never assume Arial covers Hangul. Neither Korean font was used in the English sample deck.
14. If 16:9 is requested, reflow to 13.333 × 7.5 inches. Keep body text at least as large, use roughly 0.6-inch side margins, and allocate extra width to the figure or a broader text area. Do not stretch the 4:3 slide or increase word count simply because the canvas is wider.
15. Render every final slide and inspect clipping, overlaps, title wrapping, figure labels, and actual text size. Check a long slide as well as a sparse one. Source references belong in notes and concise visible credits where appropriate.

Suggested English content budget: around 70–100 words for a text-only slide and 40–70 words for text with a figure. These are planning ranges, not quotas. Wrapped-line count and visual fit are the controlling checks. Do not pad short slides or discard necessary material just to satisfy a number.

## Reusable instruction

Create this presentation in the Simple Academic style derived from Ch1_SI.pdf. Use a white 4:3 canvas, Arial, navy 28 pt titles, a thin navy rule, and near-black 22 pt body text. Keep one broad reading area and use only the figures, tables, and equations needed to explain the content. Split crowded slides before reducing essential prose below 20 pt. Avoid decorative cards, colorful panels, icons, shadows, and redundant labels. Preserve useful technical explanation and allow blank space after the content is readable. Use the supplied sample layouts and inspect every rendered slide before delivery.

## Deliverables and limitations

- `Simple_Academic_Presentation.pptx`: editable six-slide reference deck.
- `Simple_Academic_Template.potx`: PowerPoint template with the same six sample slides and reusable layouts.
- This guide: the measured design analysis and generation rules.

The template reconstructs the PDF's visual style; it does not recover the original PowerPoint structure. Sample figures are images extracted from the supplied PDF. The sample equation is editable text, not an Office Math object. The optional APL logo is retained from the supplied cover and should be removed or replaced when it is not appropriate.

The PPTX specifies Arial as in the reference. A computer without Arial may substitute another font; recheck wrapping after substitution. Render checks do not constitute testing in the desktop PowerPoint application.
