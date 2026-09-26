# Egypt reference facts

**Last reviewed: 2026-09.** These are working defaults for design and planning, not legal or provider guarantees. Facts marked *(changes)* move over time: confirm them against the current official source before they become a hard rule in validation, pricing, or compliance. Everything else is stable enough to design with directly.

## Phone numbers

- Country calling code: `+20`.
- Mobile numbers are 11 digits in national form, starting `010`, `011`, `012`, or `015`. In international form the leading `0` is dropped: `+20 10 1234 5678`.
- The prefix historically identified the operator (Vodafone, Etisalat/e&, Orange, WE). Number portability means it no longer reliably does, so never route, price, or label by prefix. *(changes)*
- Landlines use area codes, for example `02` for Cairo and `03` for Alexandria: `+20 2 XXXX XXXX`.
- People type numbers with spaces, dashes, a leading `0`, `0020`, `+20`, or in Arabic-Indic digits (`٠١٠...`). Accept all of these and normalize on the server.

## Identity

- The national ID (الرقم القومي) is 14 digits. It encodes birth century and date, a governorate code, a sequence, and a check digit. Treat it as sensitive personal data: collect it only when a verified requirement exists, and never derive gender, age, or origin from it for UI purposes.

## Addresses

- There are 27 governorates (محافظات). Below them, cities, districts (أحياء/مراكز), and villages vary in naming and spelling.
- Delivery addresses commonly rely on building number, floor, apartment, and a landmark (علامة مميزة). Street names can be informal, duplicated, or missing.
- Postal codes exist (5 digits) but consumers rarely know or use them. Do not make them required.
- Couriers often confirm the address by phone call before delivery, which is why a reachable phone number is usually part of the address.

## Money

- Currency: Egyptian pound, ISO code `EGP`. 1 pound = 100 piastres (قرش).
- Display forms include `ج.م`, `جنيه`, `EGP`, `E£`, and `LE`. Pick one per product and keep it consistent.
- `Intl.NumberFormat('ar-EG', {style: 'currency', currency: 'EGP'})` renders Arabic-Indic digits by default. Use the locale `ar-EG-u-nu-latn` to keep Arabic labels with Western digits.
- Prices move often because of inflation and exchange-rate changes. Avoid hardcoding prices in copy, screenshots, or examples. *(changes)*

## Digits

- Western digits (0-9) dominate in apps, ecommerce, banking apps, and phone numbers.
- Arabic-Indic digits (٠-٩) appear in print, government documents, and some formal or traditional contexts.
- Users type either set, depending on their keyboard. Accept both in phone, OTP, amount, and ID fields and normalize before validation.

## Time and calendar

- Time zone: `Africa/Cairo`. Standard time is UTC+2. Daylight saving time was reinstated in 2023 and runs from the last Friday of April to the last Thursday of October (UTC+3). The rule has been suspended and restored several times, so always use maintained tz data, never a fixed offset. *(changes)*
- The weekend is Friday and Saturday; the typical workweek is Sunday to Thursday. Friday midday is prayer time and a common low-activity window.
- Business uses the Gregorian calendar. Ramadan and the two Eids follow the Hijri calendar and shift about 11 days earlier each year; working hours, delivery windows, and usage patterns change during Ramadan. Coptic Christmas is on 7 January.

## Payments

These are the methods Egyptian users commonly expect to see. Whether a given product supports each one depends on its provider contracts. *(changes)*

- **Cash on delivery (الدفع عند الاستلام):** still widely used in ecommerce, especially for first orders and lower-trust merchants.
- **Cards:** Visa and Mastercard, plus **Meeza**, the national domestic card scheme.
- **Mobile wallets:** Vodafone Cash, Orange Cash, e& cash, WE Pay, and bank wallets. Wallets are interoperable across operators.
- **InstaPay:** the instant payment network launched in 2022. Users pay to a phone number, account, or an InstaPay address (IPA, `name@instapay`).
- **Reference-code payments:** Fawry and similar networks let users pay a generated reference number at retail outlets or in-app. The order is pending until the provider confirms payment.
- **Installments and BNPL:** valU, Sympl, Souhoola, Contact, Aman, and bank installment plans are common for higher-value purchases.
- Gateways and aggregators such as Paymob, Fawry Pay, Kashier, and Geidea bundle several of these methods. Confirm exactly which methods an account has enabled.

## Language and channels

- Arabic is the primary language. English is common in tech, professional, and higher-education contexts, and many users switch between the two.
- **Franco** (Arabizi, Latin-script Egyptian Arabic such as `3ayez` or `ezayak`) is common in chats and informal search. Search and support flows may need to handle it.
- WhatsApp is the dominant messaging channel for talking to businesses. SMS remains the standard channel for OTP delivery.

## Privacy and regulation

- The Personal Data Protection Law is Law No. 151 of 2020. Check the current status of its executive regulations and licensing requirements with the Personal Data Protection Center and qualified counsel before relying on it. *(changes)*
- Payments, wallets, and lending are regulated by the Central Bank of Egypt (CBE) and the Financial Regulatory Authority (FRA). Telecom services, including SMS sender IDs, fall under the NTRA. *(changes)*
