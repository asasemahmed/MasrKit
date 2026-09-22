---
name: egyptian-session-report
description: Summarize what an agent changed in a working session and deliver it as a clean RTL HTML report written in natural Egyptian Arabic, using Cairo font with a light and dark theme toggle.
metadata:
  version: 1.0.0
  category: egypt-localization
  locale: ar-EG
  tags: [egypt, reporting, html, summary]
---

# Egyptian session report

## Purpose

Turn the work an agent completed in a session into a short, honest, shareable report: a written summary in natural Egyptian Arabic plus a single self-contained HTML page that presents the tasks and file changes in a clean RTL layout. The page uses the Cairo font, works in light and dark mode with a visible toggle, and stays readable for non-technical Egyptian stakeholders.

The report is a communication artifact, not a legal record. It describes only work that actually happened and labels anything uncertain.

## Use this skill when

Use it when the user asks for a summary of what was done, a report of agent changes, or a presentable page showing completed tasks and modified files, especially for Egyptian or Arabic-speaking teammates, clients, or managers.

Do not use it for commit messages, developer changelogs, English release notes, analytics dashboards, or billing and time-tracking documents. Those have different audiences and conventions.

## Workflow

1. Collect the facts before writing anything: run `git status --short`, `git diff --stat`, and `git log --oneline -n 10`, and review the session's task list.
2. Group the work into a small number of meaningful tasks. Merge trivial edits into the task they belong to instead of listing every file touch.
3. Write the summary in professional Egyptian Arabic: what was done, why it matters, and what is left, in that order.
4. Fill the HTML template from [references/report-template.html](references/report-template.html) with the real content and save it as a new file.
5. Open the result in a browser and verify RTL rendering, both themes, and mobile width before delivering.

## Gather the changes

- Prefer evidence over memory. Git output and the session task list are the source of truth; never invent a change to make the report look fuller.
- If the workspace is not a git repository, rely on the session task list and say so inside the report.
- Separate completed work from work that is partial, blocked, or only attempted. Partial work is reported as partial.
- Keep exact numbers when they are available: files changed, lines added and removed, tasks completed.

## Write the Egyptian Arabic summary

- Coordinate with `egyptian-copy` for register decisions. Professional Egyptian Arabic is the default: warm, direct, and free of caricature slang.
- Write the summary natively in Arabic. Do not draft in English and translate; translated rhythm reads as stiff.
- Keep file names, commands, branch names, and technical identifiers in English, each isolated in an LTR span so it never flips the sentence direction. Coordinate with `arabic-rtl` for mixed-direction text.
- Use short sentences and familiar words. State limits honestly: an unverified assumption is written as an assumption.
- Keep numbers and counters consistent with the audience. Western digits with Arabic labels are the safe default for technical stakeholders.

## Build the HTML report

- Start from [references/report-template.html](references/report-template.html) and replace its sample content. Do not leave sample tasks or files in the delivered page.
- Keep everything in one self-contained file: inline CSS, a small inline script, and Cairo loaded from the Google Fonts CDN with a system fallback stack. No external frameworks.
- RTL first: the document is `<html lang="ar" dir="rtl">`, styled with logical CSS properties so spacing follows direction automatically.
- Ship both themes together: CSS variables on `:root` for light and on `[data-theme="dark"]` for dark, a visible toggle button, the choice persisted in local storage, and the visitor's system preference as the default.
- Recommended structure: header with report title, project, and date; a summary paragraph; stat chips for tasks and changes; a completed-tasks list; a changed-files table; a short what-is-left note; a footer.
- Keep the design quiet. Generous spacing, one accent color, clear hierarchy. The page is a report, not a landing page.

## Anti-patterns

- Reporting changes that do not appear in git evidence or the session task list.
- Dumping raw diffs or terminal logs into the page instead of summarizing them.
- Translating an English summary word for word into stiff formal Arabic.
- Letting Latin file names flip the reading direction of an Arabic sentence.
- Shipping only one theme, or a toggle that forgets the choice on reload.
- Adding CSS or JS frameworks, icon libraries, or trackers. The report must stay a single portable file.
- Decorative clutter: heavy gradients, animations, emoji walls, or marketing language about the work.

## Output behavior

- Save the report as `session-report.html` in the project root unless the user names a different path.
- Reply with the file path and one sentence in Egyptian Arabic describing what the report covers. Do not paste the whole HTML into chat unless asked.
- Offer to adjust the register, more formal or more casual, or to change the default theme.

## Quality checklist

- [ ] Every reported change traces back to git evidence or the session task list.
- [ ] Partial or uncertain work is labeled as such, not presented as done.
- [ ] The summary reads as natural Egyptian Arabic, not translated English.
- [ ] File names, commands, and identifiers stay in English and are direction-isolated.
- [ ] The HTML is one self-contained file with `lang="ar"` and `dir="rtl"`.
- [ ] Cairo loads from the Google Fonts CDN with a system font fallback.
- [ ] Light and dark themes are both readable, and the toggle persists the choice.
- [ ] The page reads correctly on a narrow mobile screen.
- [ ] No external frameworks, no dead links, and no leftover sample content.

