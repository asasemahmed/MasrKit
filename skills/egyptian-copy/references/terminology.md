# Egyptian product terminology reference

This is a decision aid, not a mandatory translation table. Product domain, register, and user research take precedence.

## 1. Core Actions & Navigation (إجراءات أساسية وتنقل)

| Concept | Neutral/formal | Professional Egyptian possibility | Notes |
|---|---|---|---|
| Mobile phone | رقم الهاتف المحمول | رقم الموبايل | `موبايل` is familiar in Egypt, but use `رقم الهاتف` in legal/banking contracts |
| Send / Submit | إرسال | ابعت / إرسال | In applications, `إرسال الطلب` avoids ambiguity; `ابعت` works well in messaging/support |
| Save | حفظ | احفظ / حفظ | State whether progress is auto-saved or local draft |
| Edit | تعديل | عدّل / تعديل | Direct and actionable |
| Cancel | إلغاء | إلغاء | Universal across registers |
| Delete / Remove | حذف / إزالة | مسح / حذف | `حذف` is safer for irreversible deletions; `مسح` is common in conversational UI |
| Confirm | تأكيد | أكّد / تأكيد | Used before irreversible actions |
| Search | بحث | دوّر / بحث | Search inputs usually use placeholder `ابحث هنا...` or `بتدوّر على إيه؟` for casual apps |
| Filter / Sort | تصفية / ترتيب | تصفية / ترتيب | Clear and understood |
| Try again | حاول مرة أخرى | جرّب تاني | Pair specifically with what failed (e.g. `جرّب تاني بعد شوية`) |
| Next / Continue | التالي / متابعة | كمّل / التالي | `كمّل` creates momentum in multi-step onboarding |
| Back | الرجوع | ارجع / رجوع | Arrow icons must flip in RTL |
| View more / See all | عرض المزيد / عرض الكل | شوف الكل / عرض المزيد | Context-sensitive depending on space |

## 2. Account, Authentication & Security (الحساب والمصادقة والأمان)

| Concept | Neutral/formal | Professional Egyptian possibility | Notes |
|---|---|---|---|
| Sign in | تسجيل الدخول | ادخل على حسابك / تسجيل الدخول | Keep visually and semantically distinct from account creation |
| Create account | إنشاء حساب | اعمل حساب جديد / إنشاء حساب | State the immediate benefit before registration friction |
| Sign out | تسجيل الخروج | خروج / تسجيل الخروج | Safe and standard |
| Verification code (OTP) | رمز التحقق | كود التأكيد | `كود التأكيد` is universally recognized in Egypt; avoid `رمز المصادقة` (too bureaucratic) |
| Resend code | إعادة إرسال الرمز | ابعت الكود تاني | Include countdown timer (e.g. `ابعت الكود تاني خلال 45 ثانية`) |
| We sent a code to... | تم إرسال رمز التحقق إلى | بعتنا لك كود التأكيد على | Clear, active voice |
| Forgot password? | هل نسيت كلمة المرور؟ | نسيت كلمة السر؟ | Friendly and conversational |
| New password | كلمة مرور جديدة | كلمة سر جديدة | Avoid complex jargon |
| Phone already registered | رقم الهاتف مسجل بالفعل | الرقم ده متسجل عندنا قبل كده | Provide direct link to login or recovery |

## 3. E-Commerce & Orders (التسوق وإدارة الطلبات)

| Concept | Neutral/formal | Professional Egyptian possibility | Notes |
|---|---|---|---|
| Cart | سلة التسوق | السلة / سلة المشتريات | Keep consistent across header, badge, and drawer |
| Checkout | إتمام الشراء / الدفع | كمّل الدفع / تأكيد الطلب | `إتمام الشراء` for neutral; `كمّل الطلب` or `تأكيد الشراء` in consumer UI |
| Order | طلب | طلبك / أوردر | Use `أوردر` only when brand research strongly supports young/casual consumer culture; `طلب` is universally professional |
| Order summary | ملخص الطلب | تفاصيل الطلب | Explains costs, items, and taxes |
| Track order | تتبع الطلب | تابِع طلبك / تتبع الشحنة | Actionable and clear |
| In stock | متوفر | متوفر في المخزون | Reassuring status |
| Out of stock | نفد من المخزون | خلصان / غير متوفر حالياً | `غير متوفر حالياً` is respectful; `خلصان` only for casual storefronts |
| Coupon / Promo code | قسيمة شراء / رمز الخصم | كود الخصم / بروموكود | `كود الخصم` is widely preferred over `قسيمة شراء` in Egypt |
| Apply coupon | تطبيق الرمز | طبّق الكود / استخدم الكود | Immediate feedback |
| Free shipping | شحن مجاني | الشحن ببلاش / شحن مجاني | `شحن مجاني` is professional; `شحن ببلاش` works well in consumer marketing banners |
| Estimated delivery | موعد التوصيل المتوقع | هيوصلك يوم / التوصيل المتوقع | Give a realistic window (e.g. `هيوصلك خلال يومين إلى 3 أيام عمل`) |

## 4. Payments, Wallets & Financials (المدفوعات والمحافظ الرقمية)

| Concept | Neutral/formal | Professional Egyptian possibility | Notes |
|---|---|---|---|
| Cash on Delivery (COD) | الدفع عند الاستلام | الدفع كاش عند الاستلام | Specify if exact change is required or card on delivery is supported |
| Electronic Wallet | محفظة إلكترونية | محفظة كاش / محافظ المحمول | Egyptian users associate `محفظة` with mobile wallets. Only name specific providers you actually support. |
| Top up wallet | شحن الرصيد / تغذية المحفظة | اشحن محفظتك / تزويد الرصيد | Clear verb |
| Reference number / Code | الرقم المرجعي / رمز المعاملة | كود العملية / الرقم المرجعي | Crucial for Fawry, Aman, or InstaPay manual transfers |
| Insufficient balance | الرصيد غير كافٍ | رصيدك مش كافي | Friendly guidance to top up without embarrassing the user |
| Payment pending | الدفعة قيد المراجعة | جاري تأكيد الدفع | Never show success screen while transaction is still pending |
| Payment failed | فشلت عملية الدفع | الدفع ما كملش / فشل الدفع | Explain why and offer alternate method (e.g. `جرّب وسيلة تانية أو ادفع كاش`) |
| Refunded | تم رد المبلغ | رجّعنا لك فلوسك / تم استرداد المبلغ | Clear status in order history |
| Installments / BNPL | تقسيط / الدفع بالتقسيط | قسّط طلبك | State monthly payment clearly (e.g. `قسّط على 6 شهور بمبلغ ... ج.م/شهرياً`). Only name specific providers you actually support. |

## 5. System States, Errors & Network (حالات النظام والأخطاء)

| Concept | Neutral/formal | Professional Egyptian possibility | Notes |
|---|---|---|---|
| Something went wrong | حدث خطأ غير متوقع | حصلت مشكلة غير متوقعة | Reassure user that data is safe; provide recovery action |
| No internet connection | لا يوجد اتصال بالإنترنت | النت فصل... متقلقش كل بياناتك محفوظة | Tell user whether form state was preserved locally |
| No results found | لا توجد نتائج مطابقة | ملقيناش نتائج للي بتدوّر عليه | Offer filter reset or suggestion |
| Not yet | ليس بعد / حتى الآن | لسه | Avoid dialect in legal/contract copy |
| Support / Help | الدعم / خدمة العملاء | كلم خدمة العملاء / المساعدة | Clarify available hours or channels |

---

## Guidelines for Egyptian Register Selection

1. **Avoid Mechanical Transliteration:** Do not transliterate English terms phonetically when an organic Arabic term exists (e.g. use `تأكيد الشراء` instead of `تشيك أوت`).
2. **Respect the Gravity of Financial Actions:** When money, refunds, or passwords are at stake, shift slightly towards **Neutral / Professional Arabic** (`تم خصم المبلغ`, `الرقم المرجعي`) rather than ultra-slangy dialect.
3. **Keep Numbers & Codes Isolated:** Always wrap dynamic codes, phone numbers, and reference numbers in `<bdi dir="ltr">` so Arabic punctuation does not distort them.
4. **Record Decisions:** For a project termbase, record rejected variants and why, to avoid revisiting the same debates.
