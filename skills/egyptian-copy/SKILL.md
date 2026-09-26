---
name: egyptian-copy
description: Write natural Egyptian Arabic product copy (عامية مصرية or MSA) for apps and websites. Use when writing or translating UI strings, buttons, error messages, onboarding, notifications, marketing pages, WhatsApp or support replies for Egyptian users, choosing a register between MSA and Egyptian dialect, or deciding how to address users by gender and formality. Not for general text cleanup (use humanizer).
metadata:
  version: 1.0.0
  category: egypt-localization
  locale: ar-EG
  tags: [egypt, copywriting, localization, content-design]
---

# Egyptian Product Copy

## Purpose

Write copy that sounds chosen for its audience and task, not translated sentence by sentence. Egyptian copy is a register decision, not a license for exaggerated slang, forced humor, phonetic spellings, or indiscriminate English.

## Use this skill when

Use it for Egyptian product UI, onboarding, forms, marketing, transactions, support, commerce, education, fintech-style experiences, and service businesses. If market or brand evidence is missing, state a conservative register assumption rather than inventing a persona.

## Workflow

1. Identify audience, domain, relationship, risk, channel, and desired action.
2. Choose a register and a form of address, and record both in one sentence: for example, “professional Egyptian Arabic, warm, direct, and restrained; generic masculine second person, no gender inference.”
3. Create a terminology list for repeated actions, entities, and statuses before writing screens.
4. Write from user intent and consequence. Do not preserve English word order.
5. Make buttons specific, validation recoverable, and transactional content explicit about status and next steps.
6. Read the copy aloud. Remove phrases that sound theatrical, bureaucratic, patronizing, or mechanically translated.
7. Review consistency, bidi-sensitive tokens, accessibility, and factual claims in context.

## Choose the register deliberately

### Modern Standard Arabic (MSA)

Use for cross-region audiences, official or policy-heavy material, formal education content, and situations where local familiarity would reduce authority or clarity. Keep it contemporary; avoid ornate administrative language.

### Professional Egyptian Arabic

Use for many Egyptian consumer products, service businesses, local SaaS, practical onboarding, and support. It can use familiar Egyptian constructions while keeping spelling, tone, and terminology controlled. This is the safest default only when the product explicitly targets Egypt and no stricter voice is given.

### Casual Egyptian Arabic

Use when brand research supports friendliness and the consequence is low: community, lifestyle, lightweight onboarding, or conversational support. Keep instructions precise. Casual does not mean slang-heavy.

### Youth-focused Egyptian Arabic

Use only with evidence about the audience and brand. Favor energetic brevity over trending slang, which dates quickly and can exclude users. Never imitate a stereotype of young Egyptians.

### Business/formal Arabic

Use for B2B administration, contracts, invoices, account permissions, security, and high-stakes financial states. Plain MSA or restrained professional Arabic is usually safer than dialect. Formality must not hide the next action.

### Mixed Arabic and English

Retain English when the audience recognizes a product, protocol, plan, or technical term more reliably in English. Introduce it clearly and use it consistently. Do not transliterate merely to make the screen look local. Prefer an Arabic explanation plus the recognized English term when comprehension benefits.

## Address the user deliberately

Egyptian Arabic second-person forms are gendered: `اكتب` / `اكتبي`, `تحب` / `تحبي`, `جرّب` / `جرّبي`. Decide the policy once per product and apply it everywhere, including notifications and support templates.

1. **Generic masculine (default).** Egyptian interfaces conventionally use the masculine second person as the generic form, and most users read it as neutral in short commands and buttons. Use it when there is no stored preference and no brand decision. The examples in this skill follow this default.
2. **User-chosen form.** If the product lets users choose how to be addressed, use that choice in personalized messages (greetings, notifications, support replies). Keep shared UI such as buttons and labels generic.
3. **Neutral constructions.** Where they read naturally, avoid the choice altogether: verbal nouns on buttons (`حفظ التغييرات`, `إرسال الطلب`), first-person plural for system actions (`مقدرناش نبعت الطلب`), or statements about the object (`الملف اتحذف`). Do not force these where they sound stiff.

- Never infer gender from a name, photo, or national ID.
- Do not mix forms inside one flow.
- Use feminine forms throughout only when the audience is known to be women, for example a product built for mothers, and research supports it.
- Avoid slash forms like `اكتب/ي` in product UI. They are acceptable in formal documents and printed forms.

## Content patterns

### Landing pages and marketing

- Lead with the user's result, then explain how it works and why to trust it.
- Replace empty superlatives with specific capability or proof that the product can substantiate.
- Keep headlines idiomatic; do not translate English metaphors that do not travel.
- Align CTA with commitment: `جرّب النسخة التجريبية` differs from `اشترك دلوقتي`.
- Never invent Egyptian customer counts, approvals, partnerships, or market claims.

### Onboarding

- Explain the benefit before requesting effort or personal data.
- Keep each step about one decision. State whether progress is saved.
- Distinguish `تخطّي` from `لاحقًا`; explain consequences when skipping affects setup.
- Use a progress indicator only when it honestly reflects the flow.

### Forms and validation

- Labels name the requested value. Helper text explains format or reason. Placeholders show examples only.
- Required-field errors should name the field: `اكتب رقم الموبايل` rather than `هذا الحقل مطلوب` repeated everywhere.
- Format errors should show a valid example without implying it is the only valid data.
- Server errors must not blame the user. Preserve input and offer a retry or alternate path.

### Transactional messages and notifications

- State what happened, to which object/order/account, current status, and any required action.
- Distinguish submitted, pending, completed, rejected, cancelled, and failed. Do not use a generic success message for a pending operation.
- Put identifiers, dates, and amounts in isolated, readable form. Avoid sensitive detail on a lock screen.
- For irreversible or time-sensitive actions, state the deadline or consequence only when verified by the system.

### Empty, loading, success, and error states

- First-use empty: explain value and offer setup.
- No results: reflect filters/search and offer reset/edit.
- Loading: say what is loading only when delay is perceptible.
- Success: name the completed action and next step.
- Error: state the failure, what was preserved, and how to recover.

### Support and WhatsApp-like messaging

- Open naturally and ask for the smallest missing detail.
- Match the channel's brevity without losing identity, privacy, or status information.
- Do not promise an immediate human response unless operations support it.
- Use message templates as adaptable structures, not robotic scripts. Provide escalation and closure language.

## Domain guidance

- **SaaS:** Keep familiar role, workspace, report, export, and plan terminology consistent. Explain uncommon English rather than scattering transliterations.
- **Ecommerce:** Make size, stock, delivery, return, payment, and order status distinct. Never imply delivery/payment availability until confirmed.
- **Education:** Prefer supportive clarity, avoid condescension, preserve official institution/program names, and distinguish draft from submitted applications.
- **Fintech-style:** Use restrained, unambiguous language. State amount, status, destination, and recovery. Do not claim regulation, guarantee, or instant settlement without verified facts.
- **Service businesses:** Specify service, appointment time, location/channel, rescheduling, and what confirmation means.

## Bad, better, best

These examples show adaptation, not universal approved strings.

| Context | Bad: machine-shaped | Better: neutral | Best: context-appropriate professional Egyptian |
|---|---|---|---|
| Form submit | `تقديم النموذج` | `إرسال الطلب` | `ابعت طلبك` when the brand permits dialect |
| Required phone | `حقل الهاتف مطلوب` | `أدخل رقم الهاتف` | `اكتب رقم الموبايل` |
| Network error | `حدث خطأ ما` | `تعذّر إرسال الطلب. حاول مرة أخرى.` | `مقدرناش نبعت الطلب. بياناتك محفوظة، جرّب تاني.` |
| Empty orders | `لا توجد أوامر` | `لا توجد طلبات حتى الآن` | `لسه مفيش طلبات. أول طلب هيظهر هنا.` |
| Pending payment | `تم الدفع بنجاح` | `عملية الدفع قيد المراجعة` | `الدفع لسه بيتأكد. هنحدّث حالة الطلب أول ما النتيجة توصل.` |
| Delete | `هل أنت متأكد؟` | `هل تريد حذف الملف؟` | `تحب تحذف الملف؟ مش هتقدر ترجّعه بعد الحذف.` |

“Best” changes with audience and risk. In a bank or official portal, the neutral/formal option may be best. The “best” column uses the generic masculine default described in [Address the user deliberately](#address-the-user-deliberately).

## Terminology and consistency

Maintain a small termbase with: concept ID, preferred Arabic, allowed English, rejected variants, register, definition, and example. Read [references/terminology.md](references/terminology.md) for a starter reference.

- One concept should have one preferred name within a flow.
- Distinguish `حساب` (account), `طلب` (request/order/application depending on domain), and `عملية` (transaction/operation) by context.
- Preserve official names and identifiers. Do not translate brands or legal entity names unless an official form exists.
- Choose `هاتف` versus `موبايل`, `إرسال` versus `ابعت`, and similar pairs based on the declared register, not personal taste.

## Editing heuristics

- Remove openings equivalent to “please be informed that” unless courtesy is necessary.
- Prefer active, direct sentences. State the object of an action.
- Avoid stacked nouns copied from English and literal gerunds on buttons.
- Do not overuse exclamation marks, emojis, diminutives, or `يا بطل`-style familiarity.
- Do not Arabize every English word phonetically. Ask whether the term is recognized, explainable, or replaceable.
- Use inclusive language without assuming gender, income, literacy, location, religion, or digital confidence.
- Keep punctuation and numerals readable under RTL; coordinate with `arabic-rtl` rather than embedding ad hoc invisible marks in source copy.

## Quality checklist

- [ ] Audience, domain, risk, channel, register, and form of address are explicit.
- [ ] Gendered forms follow one policy across the flow; gender is never inferred.
- [ ] Copy is written for intent rather than translated line by line.
- [ ] CTAs describe results and reflect the actual commitment.
- [ ] Errors name the problem, preserve work, and offer recovery.
- [ ] Pending and completed states are not conflated.
- [ ] Terms are consistent across UI, notifications, support, and backend templates.
- [ ] Dialect is natural and restrained; no caricature or trend-chasing slang.
- [ ] English and transliteration are used only when they improve recognition.
- [ ] Claims, timing, availability, and policy statements are verifiable.
