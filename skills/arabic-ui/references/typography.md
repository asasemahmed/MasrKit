# Arabic typography decisions

Use this reference when choosing or reviewing a type system. Font availability and licensing change; verify the current official source and license before bundling a font.

## Selection matrix

| Need | Evaluate | Reject when |
|---|---|---|
| Long body copy | Open counters, distinct dots, comfortable regular weight, full punctuation | Marks collide, regular is too faint, or line height must be extreme |
| Dense product UI | Clear small sizes, tabular figures if needed, compact but legible forms | Labels blur or numerals are ambiguous |
| Arabic + Latin | Compatible perceived scale, weight, and voice | One script dominates or baselines feel unrelated |
| Display headings | Brand character with readable joins | Style becomes difficult beyond a few words |

## Token approach

Define semantic tokens rather than styling screens independently: display, heading, title, body, label, caption, and numeric/tabular. For each token specify family, size, weight, line height, and intended use. Test at least:

- a short Arabic label;
- a two-line Arabic heading;
- Arabic with an English product name;
- Arabic punctuation and parentheses;
- Western and Arabic-Indic digits;
- a marked/vocalized string;
- bold and disabled states.

Do not publish a rigid universal size table: the chosen font, platform, viewport, and content density determine usable metrics.
