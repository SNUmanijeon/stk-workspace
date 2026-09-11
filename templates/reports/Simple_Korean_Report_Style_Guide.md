# Simple Korean Technical Reports

## Purpose

A reusable family of restrained Korean reports reconstructed from the three supplied PDF examples. The technical report is the default. Use the progress report for recurring status updates and the review memo for numbered comments or requests. These are editable Word reconstructions, not recovered HWP originals or exact PDF conversions.

## Files and reuse

| File | Use |
|---|---|
| `Simple_Korean_Technical_Report.docx` | Default report reference: optional summary sheet, technical body, table, figure placeholders, conclusions and references |
| `Simple_Korean_Technical_Report.dotx` | Word template with the same content and styles; opening it creates a new document |
| `Simple_Korean_Progress_Report.docx` / `.dotx` | One-page status form with period, progress, expenditure, milestones, next steps and requests |
| `Simple_Korean_Review_Memo.docx` / `.dotx` | Numbered review comments and requests, with a centered title and right-aligned date |
| `Simple_Korean_Report_Style_Guide.md` | This style specification and authoring rules |
| `Report_Request_Prompt.txt` | Copyable prompt for a later session |

For a later ChatGPT session, attach the appropriate DOCX and this guide along with the actual source material. The DOCX and guide are the minimum reusable pair. Alternatively attach the complete template-files ZIP and state which layout to use. A DOTX is useful for Word but is not required when asking ChatGPT to write a report. The original PDFs are not required for routine reuse.

If the saved template is available, select **Simple Korean Technical Reports** with Documents and provide the subject, intended reader, content sources and required length. The saved template retains all three DOCX layouts and this guide. Do not assume selecting it supplies new research facts or project data.

## What the references establish

| Reference | Observed properties | Applied in this family |
|---|---|---|
| 우주소형무인제조플랫폼실증사업 서면보고, 2026년 8월 2주차 | One A4 page; centered 18 pt title; right date; 12 pt Haansoft Dotum text; narrow category column and wide content column; mostly white cells; black outer border and fine inner rules | Progress report layout, 18 pt title, 12 pt text, 27 mm category column, short noun-ending entries |
| 스페이스린텍 보완사항 | Two A4 pages; 14 pt centered title; 12 pt Haansoft Dotum body; 13 pt section labels; numbered paragraphs with hanging indents; selective bold emphasis | Review memo layout, numbered requests, bold parenthetical subjects, restrained spacing |
| H-hub 1차년도 연차보고서 supplied excerpt | Ten supplied A4 pages, with nonconsecutive printed page labels; summary form; 14/13/12 pt heading levels; 10–11 pt body; square subheadings and bullet paragraphs; grey table headers; centered captions; bottom-centered page numbers | Technical report layout, optional summary, 11 pt prose, heading hierarchy, simple tables, Figure/Table captions, page-number fields |

The annual-report PDF uses anonymized font names, so its exact original family cannot be established from the PDF font names. The two shorter references explicitly identify Haansoft Dotum. The measurements above come from the supplied PDFs; the exact Word settings below are standardized reconstruction choices. Source content, signatures, organizations, financial amounts and technical findings are not reusable boilerplate.

## Page and typography specification

| Element | Template setting |
|---|---|
| Page | A4 portrait, 210 × 297 mm, one column |
| Side margins | 20 mm; usable width 170 mm |
| Technical report margins | Top 25 mm; bottom 22 mm |
| Review memo margins | Top 25 mm; bottom 20 mm |
| Progress report margins | Top and bottom 20 mm |
| Korean text | Malgun Gothic / 맑은 고딕, black |
| Latin text | Arial, black |
| Document title | 18 pt bold, centered; review memo title 14 pt |
| Heading 1 | 14 pt bold, numbered `1.`; 14 pt before / 5 pt after |
| Heading 2 | 13 pt bold, numbered `1)`; 8 pt before / 3 pt after |
| Heading 3 | 12 pt bold, square marker `□`; 7 pt before / 3 pt after |
| Technical report body | 11 pt, exact 17.6 pt line spacing; 4 pt after |
| Progress and memo body | 12 pt, exact 19.2 pt line spacing |
| Main table text | 10.5 pt, exact 15 pt line spacing |
| Captions | 10 pt, exact 15 pt line spacing, centered |
| Metadata | 10.5 pt, right aligned |
| References | 10 pt, 15 pt line spacing, left aligned, 8 mm hanging indent |
| Page number | Technical report only, 9 pt, centered `- 1 -`, native PAGE field |

### Font portability

The editable files name **Malgun Gothic** for Korean, a practical sans-serif substitute for the source Dotum, and **Arial** for Latin text. The creation environment rendered Korean with **Droid Sans Fallback** because Haansoft Dotum and Malgun Gothic were unavailable there. Arial also resolves to an installed sans-serif when unavailable. The preview therefore demonstrates the reconstructed layout with substitutions; it is not a claim of an exact font match. No fonts are embedded or redistributed.

When reproducing the source closely, use licensed Haansoft Dotum if installed. Otherwise keep Malgun Gothic; if it is unavailable, select a complete installed Korean sans-serif such as Noto Sans CJK KR, Noto Sans KR or Nanum Gothic. Apply the substitution consistently to styles, list markers and table text, not individually to a few runs. Latin text may use the same family; equations may use a suitable math font. Always render again after substitution, because line wrapping and page count can change. Do not use a font subset extracted from the PDF as the font for new content.

## Visual and writing rules

- Keep the page white and the text black. Use grey only for table labels or headers. Use color in scientific figures when it conveys data; do not add decorative accents.
- Preserve a continuous report structure. Use paragraphs, native headings and native lists. Avoid dashboards, cards, large banners, badges, floating text boxes, ornamental rules and oversized covers.
- Use coherent Korean explanatory paragraphs for background, methods, results and interpretation. Bullet paragraphs may contain several connected sentences, as in the annual-report example.
- Use noun endings such as `검토`, `작성`, `수행 중`, `확인 요청` for progress entries and action lists. Do not force all explanatory prose into terse fragments. Follow a later user's explicit writing instructions.
- Keep essential English terms and acronyms when Korean alone would be unclear. Define unfamiliar acronyms on first use.
- Bold only the main issue, request, variable or short lead-in. Avoid bolding whole paragraphs.
- Do not inherit source projects, names, signatures, dates, claimed achievements, budgets, objectives or technical conclusions into a new report. Replace all `{{...}}` placeholders with supplied facts; remove unused example material.
- Do not fill slots with invented values. Ask for indispensable missing inputs or clearly identify unresolved items, as appropriate to the requested report.

## Layout selection and adaptation

### Technical report

The first sheet is an **optional summary form**, reflecting the annual-report reference. Keep it for formal reports requiring front matter; omit it for short technical notes. The remaining pages demonstrate the body style. The sample section sequence is a starting point, not a required report structure or fixed page count.

Default sequence: scope and purpose → method and assumptions → evidence and results → interpretation and limitations → conclusions and next actions → references. Rename, add, remove or repeat sections to suit the actual subject. Extend the content without shrinking the type. Do not repeat the placeholder prose.

Use `Heading 1`, `Heading 2` and `Heading 3` for navigation. The supplied level 1 and level 2 headings use native multilevel numbering. Continue the existing list when adding a heading; restart level 2 under a new major section. Square topic labels use a separate native bullet list and do not consume numbered section counters.

The demonstrated page breaks separate the optional summary, body example and figure example. Remove or relocate the example body page break when real content flows better. Do not impose a break after every section.

### Progress report

Keep the two-column form. Center the short left labels vertically and horizontally; write the right cells as short dated bullet entries. Leave cells white, as in the reference. Include status, budget, milestones, next steps and requests only when relevant. If content requires a second page, split logically or continue the table with clear labels; never reduce the 12 pt body just to force one page.

### Review memo

Use a 14 pt centered title, right-aligned date and simple section headings. Use numbered paragraphs with hanging indents; emphasize concise parenthetical subjects. Restart numbering for a new independent list. Distinguish observations from requested changes. Add pages when comments need explanation.

## Tables and figures

### Tables

- Outer border: black, approximately 1 pt. Inner rules: grey `#888888`, 0.5 pt. These deliberately follow the supplied report references.
- Technical data table header: `#D9D9D9` grey with black text. Summary labels: `#E7E7E7`. Progress report cells remain white.
- Default padding: approximately 1.7 mm left/right and 1.3 mm top/bottom. Let rows expand; never impose a fixed height that clips content.
- Allocate width by information type. Keep IDs, units and short numeric fields compact. Use wider columns for conditions and explanations.
- Repeat header rows when tables span pages. Prefer keeping ordinary records intact, but allow or split unusually long records if a row cannot fit on a page.
- Center short labels and numeric values when that helps comparison; left-align explanatory text. Do not force every column to be centered.
- Put numbered table captions above the table. Keep the caption with the first row.
- The summary form and progress form intentionally use tables for document structure, matching the user's references. Do not turn the main technical narrative into a sequence of tables.

### Figures

- Insert meaningful figures near the paragraphs discussing them. Use a single broad figure or two aligned panels, without decorative framing.
- The two cells on the result page are **editable placeholders**, not scientific figures. Replace them with appropriate figures and remove the placeholder text; preserve aspect ratios.
- Prefer vector figures when the delivery format supports them reliably; otherwise use a sufficiently high-resolution image. Use real plotting tools for precise data.
- Keep labels readable at the final printed size. Split a crowded montage into separate figures instead of shrinking all labels.
- Place a centered numbered caption below the figure. Keep figure and caption together; split a multi-panel figure with a clearly marked continuation if it cannot fit on one page.
- The templates contain editable Word SEQ fields for `Figure` and `Table`. Update fields after adding, deleting or moving captions; do not trust old cached numbers. Word: select all, then Update Field / F9 (keyboard combination may vary).
- Use `Figure 1.` and `Table 1.` by default, matching the annual report. Korean `그림 1.` / `표 1.` is acceptable if used consistently when requested.
- Use native Word equations for editable mathematics. Do not write raw LaTeX or approximate complex equations with plain text. No example equation is supplied in this template family.

## Native style names

| Style | Role |
|---|---|
| `Title` | Main document title |
| `Heading 1`, `Heading 2`, `Heading 3` | Navigation and heading hierarchy |
| `Report Body` | Full explanatory paragraph |
| `Report Bullet`, `Report Subbullet` | Main bullet and subordinate dash paragraph |
| `Report Numbered` | Review/request numbered paragraph |
| `Report Table`, `Report Table Header` | Table cells and labels |
| `Report Caption` | Table and figure caption with SEQ field |
| `Report Metadata`, `Report Footer` | Date/author and page number |
| `Report Reference`, `Report Note` | Bibliography and secondary notes |

Use style definitions as the starting point. Some list formatting belongs to native numbering definitions; copying only `styles.xml` will not reproduce numbering or page setup. Clone the whole DOCX, or copy all required OOXML parts deliberately. Applying a DOTX alone does not necessarily override direct formatting in an existing document.

## Quality check before delivery

1. Confirm the selected layout matches the user's request and the content comes from the current task.
2. Remove unused placeholders, sample instructions and empty figure slots.
3. Confirm A4 page size, margins, actual Korean font, body size and table widths.
4. Update heading, caption and page-number fields; verify the displayed numbering.
5. Render the final DOCX to page images and inspect every page for missing Korean glyphs, clipped text, awkward wrapping, separated captions, oversized gaps and broken tables.
6. Preserve editable text and tables. Deliver the requested format; produce a PDF only if requested.

The reconstructed templates have been rendered for layout inspection. Word, Hancom Office and other editors may paginate differently, especially when fonts change. This family does not include a native HWP or HWPX file.
