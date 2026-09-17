---
name: humanizer
description: Rewrite stiff, mechanical, or over-formatted text into natural human prose while preserving meaning, voice, facts, and required structure.
metadata:
  version: 1.0.0
  category: content-quality
  locale: multilingual
  tags: [writing, editing, humanization, punctuation]
---

# Humanizer

## Purpose

Turn mechanical, repetitive, over-polished, or awkward text into clear human writing. Preserve the author's meaning, facts, audience, language, and level of formality. When requested, remove em dashes, en dashes, decorative symbols, and unnecessary special marks without damaging valid punctuation or structured content.

This skill improves writing quality. It must not claim to bypass AI detectors, conceal authorship, fabricate personal experience, or add facts that were not present in the source.

## Use this skill when

Use it to polish product copy, documentation, articles, emails, announcements, support messages, marketing text, or Arabic and English prose that sounds robotic or over-formatted.

Do not use it for source code, machine-readable data, legal clauses, quotations, citations, mathematical notation, or exact transcripts unless the user clearly asks to edit those parts. Preserve protected spans exactly.

## Workflow

1. Identify the audience, purpose, language, register, and facts that must not change.
2. Mark protected content such as code, commands, URLs, email addresses, citations, product names, identifiers, numbers, and quoted text.
3. Find mechanical patterns: repetitive sentence openings, generic transitions, inflated claims, excessive headings, canned conclusions, and uniform sentence length.
4. Rewrite for natural rhythm, directness, specificity, and an appropriate voice.
5. Apply the requested punctuation cleanup, including removal of em and en dashes.
6. Compare the rewrite with the source. Restore any lost fact, qualification, instruction, or formatting requirement.
7. Read the result aloud and remove wording that still sounds scripted, vague, or artificially enthusiastic.

## Preserve meaning before style

- Keep every factual claim, limitation, date, amount, name, and required action unless the user asks to change it.
- Do not strengthen uncertainty. `May`, `can`, and `is expected to` must not become `will`.
- Do not invent anecdotes, emotions, research, testimonials, or first-person experience.
- Preserve the user's point of view. Do not turn a personal note into corporate copy or a formal policy into casual conversation.
- Keep necessary warnings and accessibility information even when they make the text less conversational.
- If the source is ambiguous, improve clarity without pretending the ambiguity has been resolved.

## Make the writing sound human

- Prefer concrete verbs and familiar words over abstract noun chains.
- Vary sentence length naturally. Use short sentences for emphasis only when emphasis is useful.
- Join closely related ideas instead of producing a sequence of clipped statements.
- Remove filler openings such as `In today's fast-paced world`, `It is important to note`, and `In conclusion` unless they add real meaning.
- Replace generic praise such as `seamless`, `revolutionary`, `robust`, and `game-changing` with a specific benefit or remove it.
- Avoid announcing the structure repeatedly. Let headings and paragraph order do that work.
- Use contractions in English only when they fit the voice. Use natural Arabic constructions rather than translating English rhythm word for word.
- Keep some texture. Human writing can be concise without making every sentence identical or overly polished.

## Remove dashes and special marks

When the user requests clean punctuation, apply these rules:

- Replace em dashes and en dashes with a comma, colon, semicolon, parentheses, or a new sentence according to meaning.
- Do not replace every dash with the same mark. Choose punctuation from the grammatical relationship.
- Remove decorative bullets, stars, arrows, repeated separators, ornamental quotes, and excessive emoji when they do not carry meaning.
- Reduce repeated punctuation such as `!!!`, `???`, and `...` unless it is part of the intended voice.
- Convert smart quotes only if the user requests plain-text punctuation or the destination system requires ASCII.
- Preserve hyphens inside established compounds, command options, file names, identifiers, phone numbers, ranges, and URLs.
- Preserve mathematical operators, currency symbols, Arabic punctuation, diacritics, and accessibility markers when they are meaningful.
- Never alter punctuation inside code, exact quotations, citations, or data without explicit permission.

Read [references/punctuation-guide.md](references/punctuation-guide.md) when the text contains mixed punctuation, technical tokens, or Arabic and English together.

## Structure and formatting

- Keep the original format when it supports the task. A checklist should remain scannable, and a procedure should retain its steps.
- Remove headings that merely repeat the sentence below them.
- Merge one-line sections when they interrupt the reading flow.
- Keep bullets for genuinely parallel items. Use prose when the list is only a fragmented paragraph.
- Preserve Markdown, links, tables, and code fences unless the user asks for plain text.
- Do not remove all punctuation. Humanized text still needs grammatical structure and readable pauses.

## Arabic and Egyptian copy

- Preserve Arabic letter forms and do not strip meaningful diacritics automatically.
- Use Arabic punctuation or neutral punctuation consistently with the product's style.
- Do not add Egyptian slang merely to make text sound human. Match the declared register.
- Remove literal English transitions and rebuild the sentence naturally in Arabic.
- Keep mixed English product names, emails, codes, and numbers intact. Coordinate with RTL handling when direction affects display.
- Avoid exaggerated familiarity, repeated exclamation marks, and expressions that turn Egyptian Arabic into a caricature.

## Before and after examples

### Mechanical English

Before:

```text
Our revolutionary platform offers a seamless experience, designed to empower users to achieve their goals. It is important to note that you can get started today.
```

After:

```text
Set up your workspace today and keep your projects, tasks, and updates in one place.
```

### Dash cleanup

Before:

```text
The application is saved automatically — even if your connection drops — so you can return later.
```

After:

```text
The application is saved automatically, even if your connection drops. You can return to it later.
```

### Professional Egyptian Arabic

Before:

```text
يرجى العلم بأنه قد حدث خطأ غير متوقع أثناء عملية إرسال الطلب.
```

After:

```text
مقدرناش نبعت الطلب. بياناتك محفوظة، فجرّب تاني.
```

Use the Arabic rewrite only when professional Egyptian Arabic matches the requested voice. For a formal service, a neutral alternative may be better.

## Anti-patterns

- Changing facts while trying to improve flow.
- Adding fake personality, personal stories, or unsupported confidence.
- Replacing every dash with a comma and creating run-on sentences.
- Deleting meaningful symbols from code, prices, measurements, or identifiers.
- Turning every paragraph into short punchy fragments.
- Adding slang, contractions, humor, or emoji without an audience reason.
- Removing structure from instructions, policies, or accessibility content.
- Promising that rewritten text will evade detection systems.

## Output behavior

Return the polished text directly unless the user asks for commentary. If changes could affect meaning, provide a short note describing the interpretation. When useful, offer:

- a clean final version;
- a version with edits explained;
- two voice options with clearly stated register differences.

Do not surround the result with unnecessary introductions such as `Here is the humanized version` when the user only wants copy-ready text.

## Quality checklist

- [ ] Meaning, facts, qualifications, names, and required actions are preserved.
- [ ] Voice, audience, language, and formality match the request.
- [ ] Mechanical phrasing, repetition, filler, and inflated claims are removed.
- [ ] Sentence rhythm feels natural without becoming fragmented.
- [ ] Em and en dashes are absent when removal was requested.
- [ ] Decorative marks are removed, while meaningful punctuation and technical symbols remain.
- [ ] Code, URLs, identifiers, quotations, citations, numbers, and prices are unchanged unless explicitly edited.
- [ ] Arabic or Egyptian wording is natural and not stereotyped.
- [ ] The result makes no invented claims or authorship promises.
