<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/f/fe/Flag_of_Egypt.svg" alt="علم مصر بنسر صلاح الدين الذهبي" width="132">

<img src="assets/masrkit-hero-premium.svg" alt="MasrKit: ابنِ منتجات تحسّ إنها معمولة لمصر" width="100%">

# 🇪🇬 MasrKit 🇪🇬

**ابنِ منتجات تحسّ إنها معمولة لمصر.**

</div>

MasrKit مشروع مفتوح المصدر يوفّر مهارات تعليمية لوكلاء البرمجة بالذكاء الاصطناعي، علشان يساعدهم يبنوا منتجات مناسبة للمستخدمين في مصر فعلًا، مش مجرد واجهات إنجليزية مترجمة للعربي.

[![skills.sh](https://skills.sh/b/asasemahmed/masrkit)](https://www.skills.sh/asasemahmed/masrkit)

[English README](README.md) · [صفحة المشروع على skills.sh](https://www.skills.sh/asasemahmed/masrkit)

## المشروع بيحل إيه؟

التعريب مش ترجمة نصوص وبس. ممكن الزر يكون مكتوب بالعربي لكن ترتيب الصفحة يبوّظ في RTL، أو رقم الموبايل يظهر بترتيب مربك، أو رسالة الدفع تقول إن العملية نجحت وهي لسه معلّقة. مهارات MasrKit بتدي الوكيل قواعد عملية، وأمثلة، وحالات لازم يختبرها قبل ما يعتبر الشغل مكتمل.

## مهارات الإصدار الأول

- [`arabic-ui`](skills/arabic-ui/SKILL.md): تصميم واجهات عربية واضحة وحديثة.
- [`arabic-rtl`](skills/arabic-rtl/SKILL.md): تنفيذ RTL والنصوص المختلطة بشكل تقني سليم.
- [`egyptian-copy`](skills/egyptian-copy/SKILL.md): كتابة محتوى طبيعي ومناسب للسياق المصري.
- [`egyptian-product-ux`](skills/egyptian-product-ux/SKILL.md): تصميم تدفقات استخدام تراعي السوق والمستخدمين في مصر من غير تعميمات.
- [`egyptian-web-audit`](skills/egyptian-web-audit/SKILL.md): مراجعة المواقع والمنتجات بأدلة ومقترحات قابلة للتنفيذ.
- [`egyptian-backend`](skills/egyptian-backend/SKILL.md): نمذجة البيانات، والفلوس، والوقت، والإشعارات، والأمان، والتكاملات.
- [`humanizer`](skills/humanizer/SKILL.md): تحسين النصوص الجامدة وإزالة الشرطات الطويلة والعلامات الزخرفية مع الحفاظ على المعنى والنبرة والمعلومات.
- [`egyptian-session-report`](skills/egyptian-session-report/SKILL.md): تلخيص شغل الجلسة في تقرير HTML بالعربي المصري، بخط Cairo ووضع نهاري وليلي.

المحتوى الأساسي مكتوب بصيغة Markdown عادية ومش مربوط بشركة أو أداة واحدة. كل مهارة لها ملف `SKILL.md` ومراجع إضافية تُقرأ وقت الحاجة.

## التثبيت

MasrKit موجود على [skills.sh](https://www.skills.sh/asasemahmed/masrkit)، دليل مهارات الوكلاء المفتوح. أسهل طريقة إنك تثبّت المهارات بأمر واحد (محتاج Node.js 18 أو أحدث):

```bash
npx skills add asasemahmed/masrkit
```

الأداة هتسألك تثبّت أنهي مهارات ولأنهي وكيل. ولو عايز تختار مهارات معيّنة من غير أسئلة:

```bash
npx skills add asasemahmed/masrkit --skill arabic-rtl --skill egyptian-copy -y
```

### التثبيت من نسخة محلية

عاين اللي هيتم من غير ما تنسخ ملفات:

```bash
python scripts/install.py --all --target codex --dry-run
```

أو استخدم Node.js 18 أو أحدث من داخل نسخة المشروع:

```bash
npx --yes . --all --target codex --dry-run
npx --yes . --all --target codex
```

ثبّت كل المهارات أو مهارة واحدة:

```bash
python scripts/install.py --all --target codex
python scripts/install.py --skill egyptian-copy --target codex
```

تقدر تستخدم `--target` مع `codex` أو `claude` أو `cursor` أو `gemini`، أو تحدد مسار موثّق عندك باستخدام `--dest`. السكربت ما بيكتبش فوق مجلد موجود. ولو مش محتاج السكربت، انسخ مجلد المهارة كاملًا من `skills/` إلى مجلد المهارات الخاص بالأداة.

التفاصيل الكاملة وأوامر PowerShell وmacOS/Linux موجودة في [README بالإنجليزية](README.md).

## الاستخدام

```text
استخدم مهارات arabic-ui وarabic-rtl وegyptian-copy وegyptian-product-ux من MasrKit.

السوق: مصر
الجمهور: طلبة جامعات في مصر من 18 إلى 25 سنة
المطلوب: صفحة وتدفق تقديم لمنحة، مصممين للموبايل أولًا
مهم: احتفظ بالأسماء الرسمية للجامعات، وما تفترضش مواعيد أو شروط غير مؤكدة
```

شوف أمثلة أكثر في [`examples/`](examples/scholarship-platform.md)، واقرأ [دليل المساهمة](CONTRIBUTING.md) قبل اقتراح تغيير.

## الترخيص

المشروع متاح بترخيص [MIT](LICENSE).
