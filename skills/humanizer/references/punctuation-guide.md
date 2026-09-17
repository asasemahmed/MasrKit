# Punctuation cleanup guide

Use this reference when punctuation cleanup could alter meaning.

| Source relationship | Preferred replacement for a long dash | Example pattern |
|---|---|---|
| Explanation | Colon | `One thing matters: clarity.` |
| Light interruption | Commas or parentheses | `The draft, although incomplete, is usable.` |
| Two complete thoughts | Period or semicolon | `The upload failed. Your draft is safe.` |
| Contrast | Period plus a contrast word | `The plan is simple. However, it takes time.` |
| Numeric range | Preserve an appropriate range mark or write `to` | Do not change version or date ranges blindly. |

## Usually remove

- Decorative arrows around headings
- Repeated stars or separator characters
- Multiple exclamation or question marks
- Emoji used as a bullet on every line
- Smart punctuation in destinations that explicitly require ASCII

## Usually preserve

- Hyphens in CLI flags such as `--dry-run`
- Hyphens in file names, slugs, IDs, and compound terms
- Minus signs, mathematical operators, and measurement symbols
- Currency symbols and decimal separators
- Markdown syntax, links, code fences, and table pipes
- Arabic question marks and punctuation when appropriate
- Exact quotations and citations

For mixed Arabic and English, protect Latin identifiers and technical tokens before changing surrounding punctuation. Punctuation can move visually in bidirectional text, so fix direction at rendering time rather than changing the stored value.
