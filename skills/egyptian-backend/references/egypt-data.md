# Egyptian data defaults for backends

**Last reviewed: 2026-09.** Working defaults for schemas, validation, and tests. Items marked *(changes)* must be re-checked against the current official source or a maintained library before they harden into validation rules.

## Phone numbers

- Store valid numbers in E.164: `+201012345678`. Country code `+20`; mobile numbers are `01` plus 9 digits nationally (11 digits), `+20 1X XXXX XXXX` internationally.
- Normalize input that arrives as `01012345678`, `0020 10 1234 5678`, `+20-10-1234-5678`, or Arabic-Indic digits `٠١٠١٢٣٤٥٦٧٨`.
- Validate with a maintained library (for example libphonenumber or a port of it), not a regex of operator prefixes. Number portability means the prefix does not identify the operator. *(changes)*

```text
normalize("٠١٠ ١٢٣٤ ٥٦٧٨") -> "+201012345678"
normalize("0020 10-1234-5678") -> "+201012345678"
```

## Digits

Convert Arabic-Indic (`٠-٩`, U+0660 to U+0669) and Extended Arabic-Indic (`۰-۹`, U+06F0 to U+06F9) digits to ASCII before validating phone, OTP, amount, and ID input. Keep the user's original text only where support or audit needs it.

## National ID

The national ID is 14 digits and encodes birth date, governorate, and a check digit. Store it only with a verified requirement, encrypt it at rest, restrict access, mask it in logs and responses, and never use it as a primary key.

## Money

- `EGP` has 2 minor-unit digits (piastres). Store `amount_minor` as an integer, for example `12550` for 125.50 EGP.
- Prices and fees change frequently. Store the price that applied to each order line rather than recomputing from a current catalog. *(changes)*
- Format at the edge. `ar-EG` renders Arabic-Indic digits; `ar-EG-u-nu-latn` keeps Western digits.

## Time

- Use the IANA zone `Africa/Cairo`, never a fixed `+02:00`. Daylight saving time (UTC+3) was reinstated in 2023 from the last Friday of April to the last Thursday of October, and the rule has changed several times before. Keep tz data updated. *(changes)*
- The weekend is Friday and Saturday. Business-day calculations (SLAs, delivery estimates, settlement) must not assume Saturday and Sunday.
- Test the DST switch dates: scheduled jobs and reminders around 00:00 on the transition nights are the usual failure point.

## Arabic search

Common normalization choices for an Egyptian search index (keep the original text untouched):

- strip diacritics (tashkeel) and tatweel (`ـ`);
- fold `أ إ آ` to `ا`, `ة` to `ه`, and `ى` to `ي` for search keys only;
- consider Franco (Latin-script Egyptian Arabic, for example `3ayez`) and English transliterations for product and place names;
- never apply these folds to passwords, IDs, legal names used for matching, or other exact-match fields.

## Payment state

Egyptian payment methods have different confirmation timing. Model them explicitly:

| Method | Typical confirmation |
|---|---|
| Card (Visa, Mastercard, Meeza) | Near-instant, possibly after a 3-D Secure step |
| Mobile wallet | Near-instant after the user approves in the wallet app |
| InstaPay | Near-instant; the merchant usually confirms by reconciliation |
| Reference code (Fawry and similar) | Pending until the user pays at an outlet or in-app, often hours later; codes expire |
| Cash on delivery | Unpaid until the courier collects and settlement is reconciled |
| Installments (valU, Sympl, and others) | Pending until the provider approves the plan |

Treat every method as unpaid until a verified provider callback or reconciliation confirms it. Which methods an account can actually use depends on the provider contract. *(changes)*

## Privacy and regulation

The Personal Data Protection Law is Law No. 151 of 2020. Its executive regulations and licensing requirements, CBE and FRA rules for payments and lending, and NTRA rules for SMS sender IDs change over time. Check them with the current authority and qualified counsel. *(changes)*
