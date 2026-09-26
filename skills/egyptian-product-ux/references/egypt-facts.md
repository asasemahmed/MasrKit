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

## Addresses and Logistics

- There are 27 governorates (محافظات). Below them, cities, districts (أحياء/مراكز), and villages vary in naming and spelling.
- Delivery addresses commonly rely on building number, floor, apartment, and a landmark (علامة مميزة). Street names can be informal, duplicated, or missing.
- Postal codes exist (5 digits) but consumers rarely know or use them. Do not make them required.
- Couriers often confirm the address by phone call before delivery, which is why a reachable phone number is usually part of the address.

### Canonical Egyptian Governorates

Software interfaces should maintain standardized Arabic and English labels alongside ISO 3166-2:EG codes.

| Governorate (Arabic) | Governorate (English) | ISO Code | Standard Courier Shipping Tier |
|---|---|---|---|
| القاهرة | Cairo | `EG-C` | Greater Cairo (القاهرة الكبرى) |
| الجيزة | Giza | `EG-GZ` | Greater Cairo (القاهرة الكبرى) |
| القليوبية | Qalyubia | `EG-KB` | Greater Cairo (القاهرة الكبرى) |
| الإسكندرية | Alexandria | `EG-ALX` | Alexandria (الإسكندرية) |
| البحيرة | Beheira | `EG-BH` | Lower Egypt / Delta (الوجه البحري) |
| الغربية | Gharbia | `EG-GH` | Lower Egypt / Delta (الوجه البحري) |
| كفر الشيخ | Kafr El-Sheikh | `EG-KFS` | Lower Egypt / Delta (الوجه البحري) |
| المنوفية | Menofia | `EG-MNF` | Lower Egypt / Delta (الوجه البحري) |
| الدقهلية | Dakahlia | `EG-DK` | Lower Egypt / Delta (الوجه البحري) |
| الشرقية | Sharqia | `EG-SHR` | Lower Egypt / Delta (الوجه البحري) |
| دمياط | Damietta | `EG-DT` | Lower Egypt / Delta (الوجه البحري) |
| بورسعيد | Port Said | `EG-PTS` | Canal Cities (مدن القناة) |
| الإسماعيلية | Ismailia | `EG-IS` | Canal Cities (مدن القناة) |
| السويس | Suez | `EG-SUZ` | Canal Cities (مدن القناة) |
| بني سويف | Beni Suef | `EG-BNS` | Northern Upper Egypt (شمال الصعيد) |
| الفيوم | Fayoum | `EG-FYM` | Northern Upper Egypt (شمال الصعيد) |
| المنيا | Minya | `EG-MN` | Middle Upper Egypt (وسط الصعيد) |
| أسيوط | Asyut | `EG-AST` | Middle Upper Egypt (وسط الصعيد) |
| سوهاج | Sohag | `EG-SHG` | Southern Upper Egypt (جنوب الصعيد) |
| قنا | Qena | `EG-KN` | Southern Upper Egypt (جنوب الصعيد) |
| الأقصر | Luxor | `EG-LX` | Southern Upper Egypt (جنوب الصعيد) |
| أسوان | Aswan | `EG-ASN` | Southern Upper Egypt (جنوب الصعيد) |
| البحر الأحمر | Red Sea | `EG-BA` | Coastal & Frontier (المحافظات الحدودية) |
| الوادي الجديد | New Valley | `EG-WAD` | Frontier & Remote (المحافظات الحدودية) |
| مطروح | Matrouh | `EG-MT` | Coastal & Frontier (المحافظات الحدودية) |
| شمال سيناء | North Sinai | `EG-SIN` | Frontier & Remote (المحافظات الحدودية) |
| جنوب سيناء | South Sinai | `EG-JS` | Coastal & Frontier (المحافظات الحدودية) |

### Courier Logistics & Delivery Zones *(changes)*

Most Egyptian third-party logistics couriers (Bosta, Mylerz, Aramex Egypt, Egypt Post) group governorates into delivery tiers for turnaround and pricing. **Delivery times, fees, and COD limits differ by courier and change over time. The following is an example of common tiers:**

1. **Greater Cairo (القاهرة الكبرى):** Cairo, Giza, Qalyubia. Highest order density, same-day or next-day turnaround (24h), lowest delivery fees.
2. **Alexandria (الإسكندرية):** Alexandria. Standard 24–48h window.
3. **Lower Egypt / Delta (الوجه البحري):** Dakahlia, Gharbia, Sharqia, Menofia, Beheira, Kafr El-Sheikh, Damietta. Standard 24–48h window.
4. **Canal Zone (مدن القناة):** Port Said, Ismailia, Suez. 24–48h window.
5. **Upper Egypt (محافظات الصعيد):** From Beni Suef down to Aswan. 48–72h turnaround, incremental rate tiers.
6. **Frontier & Coastal (المحافظات الحدودية):** Red Sea, Matrouh, South Sinai, North Sinai, New Valley. 3–5 days, higher shipping fees, occasional Cash-on-Delivery restrictions based on courier branch coverage.

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
