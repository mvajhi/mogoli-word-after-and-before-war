﻿![دانشگاه تهران - ویکی‌پدیا، دانشنامهٔ آزاد](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.001.png)![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.002.png)تاثیر زبان مغولی بر زبان فارسی

استاد: سرکار خانم لیلا کرمی

دانشجویان: مهدی وجهی - سید علیرضا میرشفیعی - امیرحسین میرمحمدی  

مقدمه

یکی از ارکان فرهنگ هر کشوری ، زبان آن کشور است که در طول تاریخ دستخوش تغییرات کوچک و بزرگ شده است ولی در هر صورت میراثی است که از گذشتگان برای آیندگان باقی مانده است و یکی از ابعاد هویتی هر ملیتی هست.

حال میزان تاثیر اتفاقات مختلف تاریخی در زبان یک کشور ، متفاوت خواهد بود و در این مسیر جنگها یکی از راههای اصلی تعامل فرهنگی بین دو کشور می باشد ، که شامل سنت ها ، اعتقادات ،روش زندگی، تغذیه و البته زبان آن دو می باشد و نسل آینده هر کشوری زبانی دارد که نمی داند کدام قسمت آن زبان اصلی اوست و کدام قسمت زبان وارداتی ملیتی دیگر است.

در این پژوهش برآنیم تا ببینیم واژگان مغولی بعد از حمله مغول به ایران تا چه حد در آثار نوشتاری بزرگان ادب وارد شده است. 

سوالات و اهداف پژوهش

هدف این پژوهش پاسخ به سوالات ذیل است:

1. چه تعداد واژگان مغولی قبل ، بعد و در حین حمله مغول در آثار برخی نویسندگان و شعرا وجود داشته است؟
1. حمله مغول چه تاثیری بر تعداد این واژگان گذاشته است؟

چکیده:

تا بحال مقالات و نوشته های فراوانی درباره حمله مغول و آسیب های آن بر کشور نوشته شده است.

اما ما در این پژوهش برآنیم تا به طور مختصر تاثیر این اتفاق را در ورود واژگان مغولی به اشعار و نوشته های اشخاص بزرگ ادبی بررسی کنیم. از این رو نویسندگانی را مورد بررسی قرار دادیم و نتیجه آن شد که آمار استفاده واژگان مغولی در آثار ادبی قبل از حمله مغول ناجیز و سپس با سیری صعودی در حین حمله بالا رفته و دوباره پس از این دوره با شیبی ملایم تر نزول پیدا کرده است.

کلیدواژه:

زبان فارسی – زبان مغولی – حمله مغول ها-  هجویری – کیکاووس – مولوی – جامی – زاکانی

مستندات فنی:

برای شروع مواردی که باید انجام شوند را فهرست می کنیم:

1. پیدا کردن فایل متنی کتب و واژه نامه مغولی
1. تبدیل فایل های متنی به فرمت خوانا برای برنامه (مانند txt)
1. نوشتن برنامه با قابلیت های زیر:
   1. باز کردن و دریافت متن از فایل و واژه نامه
   1. جدا کردن کلمات از یکدیگر (Word Tokenizing)
   1. بررسی ریشه کلمات فایل و مقایسه با واژه نامه
      1. تبدیل کلمات به ریشه ها (کتابهایش ← کتاب، می خوردیم ← خور)
      1. مقایسه لغات و شمارش آنها
      1. خروجی نتیجه خام
1. دادن ورودی ها (فایل های کتب، واژه نامه مغولی و کلمات ایست) به برنامه و دریافت خروجی
1. تحلیل خروجی ها

**پیدا کردن فایل کتب و نوشته های شاعران**

![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.003.png)**	سایت منبع باز (Open source) [گنجور1](https://ganjoor.net/) که به عنوان مرجع انتخاب شده وارد می شویم. در بخش [کتابخانه گنجور](http://epub.ganjoor.net/) می توانیم کتاب ها را با فرمت epub دانلود کنیم (تصویر 1).

تصویر 1-نمایی از سایت کتابخانه ی گنجور


1.«گنجور» مجموعه‌ای تحت وب از آثار سخنسرایان پارسی‌گو است که با استفاده از آن می‌توان ضمن مرور به تفکیک نام شاعر و نام آثار او، در بین آثار جستجو کرد. این مجموعه در ابتدا به کمک نرم‌افزار مدیریت محتوای وردپرس راه‌اندازی شده بود و از سال ۱۴۰۰ به بعد به پشتوانه نرم‌افزار اختصاصی بازمتن خود کار می‌کند.

سپس فایل را از حالت کتاب الکترونیک (epub) خارج می کنیم.

![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.004.png)

تصویر2 – نمای متحوای باز شده کتاب نمونه (کیکاووس) با فرمت epub

با بررسی فایل های باز شده ی epub متوجه می شویم، فایل های در پوشه OPF به شکل \*sec\*.xhtml حاوی محتوای کتاب ما هستند.

حال باید فایل های xhtml را به فرمت خوانا تری برای بررسی (همچون txt) در برنامه تبدیل کنیم.

سایت ها و برنامه های مختلفی برای تبدیل xhtml به txt وجود دارد. ما از [aspose ](https://products.aspose.app/words/conversion/xhtml-to-html)استفاده کردیم. هر فایل xhtml به یک فایل txt تبدیل می شود.

سپس با ادغام فایل های txt، همه را به یک فایل تبدیل کردیم. با دستور زیر می توانیم این کار را انجام دهیم. (فرض شده که تمامی فایل ها در یک پوشه هستند و هیچ فایل دیگری در آن پوشه نیست.) (تصویر 3)

|cat \* > your\_address/file\_name.txt|
| - |

![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.005.png)

تصویر3 – نمای تبدیل فایل های txt به یک فایل txt

درنهایت یک فایل را برای دادن به برنامه آماده می شود.

**نوشتن برنامه**

`	`برای نوشتن برنامه از زبان پایتون و کتابخانه ی wordcloud\_fa که متشکل از کتابخانه های wordcloud، hazm و nltk است استفاده کردیم. ابتدا توضیحات مختصری درباره ی کتابخانه ها می دهیم.

کتابخانه های hazm و nltk به ترتیب برای پردازش زبان های فارسی و انگلیسی کاربرد دارند.

![NLP vs. NLU vs. NLG - Unterschiede und Funktionen - datasolut GmbH](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.006.png)پردازش زبان طبیعی (Natural Language Processing) که به اختصار NLP نیز نامیده می‌شود، روشی است برای درک زبان انسانی برای رایانه؛ این علم یکی شاخه‌های دانش هوش مصنوعی محسوب می‌شود و به رایانه‌ها کمک می‌کند تا با آگاهی از چگونگی استفاده بشر از زبان، زبان انسانی را درک کند. پردازش زبان طبیعی یک دانش پیچیده و دشوار است. این شاخه از هوش مصنوعی خود به دو شاخه دیگر یعنی NLG و NLU تقسیم می شوند. Natural Language Understanding یا به اختصار NLU به فارسی درک زبان طبیعی بر درک خواندن ماشینی از طریق قواعد دستور زبانی و موضوع تمرکز دارد و ماشین‌ها را قادر می‌سازد تا معنای مورد نظر یک جمله را تعیین کنند. Natural Language Generation یا به اختصار NLG به فارسی تولید زبان طبیعی بر تولید متن یا ساخت متن به زبان انگلیسی یا زبان‌های دیگر توسط یک ماشین و بر اساس یک مجموعه داده معین تمرکز می‌کند (تصویر 4).

تصویر4 – ارتباط بین NLP، NLG و NLU با یکدیگر

در جدول زیر کتابخانه های معروف NLP آورده شده اند (جدول 1).

![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.007.jpeg)

جدول 1 – جدول مقایسه کتابخانه های مشهور NLP

از کتابخانه های فارسی معروف در این حوزه می توان به Hazm، Stanford، farsiNLPTools و parsivar اشاره کرد.

کتابخانه‌ NLTK (Natural Language Toolkit) یکی از جامع‌ترین و قدیمی‌ترین کتابخانه‌های پردازش زبان طبیعی در پایتون است. این کتابخانه پایه و استانداردی برای کتابخانه‌های پردازش متن محسوب شده و برای کاربردهای پژوهشی فوق‌العاده است. یکی از ویژگی‌های خوب این کتابخانه امکان اتصال به پیکره‌های مختلف متنی است.

کتابخانه هضم با استفاده از کتابخانه NLTK در سال ۱۳۹۲ توسط دانشجویان دانشگاه علم و صنعت برای پردازش زبان فارسی توسعه داده‌شده است. در ابتدا هضم تنها برای زبان پایتون و سیستم‌عامل لینوکس طراحی‌شده بود، اما اکنون برای زبان‌های جاوا و #C نیز قابل‌استفاده است. نسخه جاوایی این کتابخانه با عنوان JHazm منتشرشده است. ازجمله ویژگی‌های این کتابخانه مرتب کردن متون، بخش‌بندی، ریشه‌یابی کلمات، تحلیل صرفی و تجزیه نحوی جملات، سازگاری با NLTK و پشتیبانی از نسخه‌های ۲ و ۳ پایتون هست.

همچنین میزان دقت این کتابخانه در تحلیل متون در جدول زیر آمده است (جدول 2).

|**Module name**|**Precision**|
| - | - |
|**Lemmatizer (ریشه یابی)**|89.9%|
|**Chunker (تشخیص گروه های اسمی و فعلی)**|89.9%|
|**POSTagger (تحلیل نقش کلمات)**|97.1%|
|**DependencyParser (درخت وابستگی)**|97.1%|
جدول 2 – میزان دقت کتابخانه هضم

در ادامه تعدادی دستورات کاربردی هضم آورده شده:

|<p>>>> normalizer = Normalizer()</p><p>>>> normalizer.normalize ( 'اصلاح نویسه ها و استفاده از نیم فاصله پردازش را آسان می کند' )</p><p>'اصلاح نویسه ها و استفاده از نیم فاصله پردازش را آسان می کند'</p><p>>>> sent\_tokenize ( 'ما هم برای وصل کردن آمدیم! ولی برای پردازش، جدا بهتر نیست؟' )</p><p>[ 'ما هم برای وصل کردن آمدیم!' , 'ولی برای پردازش، جدا بهتر نیست؟' ]</p><p>>>> word\_tokenize ( 'ولی برای پردازش، جدا بهتر نیست؟' )</p><p>[ 'ولی', 'برای', 'پردازش'، '،'، 'جدا', 'بهتر', 'نیست', '؟' ]</p><p>>>> stemmer = Stemmer()</p><p>>>> stemmer.stem ( 'کتاب ها' )</p><p>'کتاب'</p><p>>>> lemmatizer = Lemmatizer()</p><p>>>> lemmatizer.lemmatize ( 'می روم' )</p><p>'رفت#رو'</p><p>>>> tagger = POSTagger ( model = 'resources/postagger.model' )</p><p>>>> tagger.tag ( word\_tokenize( 'ما بسیار کتاب می‌خوانیم' ))</p><p>[ ( 'ما' , 'PRO' ), ( 'بسیار' , 'ADV' ), ( 'کتاب' , 'N' ), ( 'می خوانیم' , 'V' ) ]</p><p>>>> chunker = Chunker( model= 'resources/chunker.model' )</p><p>>>> tagged = tagger.tag ( word\_tokenize( 'کتاب خواندن را دوست داریم' ))</p><p>>>> tree2brackets( chunker.parse (tagged))</p><p>'[کتاب خواندن NP] [را POSTP] [دوست داریم VP]'</p><p>>>> parser = DependencyParser (tagger = tagger, lemmatizer = lemmatizer )</p>|
| - |

![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.008.png)همچنین این کتابخانه حتی توانایی رسم درخت تحلیل نحوی جملات را دارد. به عنوان مثال دستور زیر درخت تحلیل نحوی جمله " زنگ‌ها برای که به صدا درمی‌آید؟" را رسم می کند (تصویر 5)

|<p>>>> parser.parse (  word\_tokenize( 'زنگ‌ها برای که به صدا درمی‌آید؟' ))</p><p><DependencyGraph with 8 nodes></p>|
| - |
تصویر 5 – نمودار تحلیل نحوی



کتابخانه wordcloud\_fa برای تولید ابر کلمات در زبان فارسی کاربرد دارد. ابر کلمات به تصویری می گویند که در آن لغات متنی به نمایش در می آید به صورتی که در آن کلمه ای که بزرگ تر است بیشتر تکرار شده اند. در تصویر زیر می توانید ابر کلمات مجموعه آثار مولانا مشاهده کنید (تصویر 6).

![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.009.png)

تصویر 6 – ابر کلمات مجموعه آثار مولانا

از آنجایی که در این کتابخانه واژه ها از هم جدا و شمرده می شوند ما می توانیم با تغییراتی در کد های آن، خروجی مد نظر خود را ستخراج کنیم و با ایجاد شرطی مغولی بودن آن را نیز بررسی کنیم.

موضوع دیگری که در این برنامه اهمیت دارد داشتن فهرستی از کلمات ایست (stop word) است. کلمه ایست به کلماتی از جمله از، به، است، گفت، یا، ای و... می گویند که مفهوم خاصی ندارند ویا صرفا برای تکمیل جمله به کار می روند و اهمیت معنایی زیادی ندارند. به همین علت و برای بهتر شدن تحلیل، لازم است این لغات از متن حدف شوند. با جست و جویی در اینترنت به [فهرستی](https://github.com/kharazi/persian-stopwords) از این کلمات رسیدیم. این فهرست شامل 1900 کلمه بود. درهنگام بررسی و تحلیل تعدادی لغت نیز به آن اضافه کردیم. لازم به ذکر است که این فهرست کاربرد عمومی دارد. بنابراین برای تحلیل متون مختلف نیاز به تغییر و اختصاصی کردن این فهرست می باشد. به عنوان مثال فهرست کلمات ایست برای متون عادی، مقاله، نظرات مشتریان، موجود در شبکه های اجتماعی و... متفاوت می باشد. بنابراین برای تحلیل و بررسی دقیق تر اشعار و نوشته های ادیبان لازم است که این لغات تک به تک بررسی شوند و در صورت نیاز کم ویا اضافه شوند اما به دلیل کمبود وقت این بررسی انجام نشده است.

درنهایت بعد از جدا کردن و شمارش لغات برای خروجی خام برنامه، فرمت CSV انتخاب شد. «CSV» مخفف عبارت «Comma Separated Values» و به معنای «مقادیر جدا شده با ویرگول» است. اینگونه فایل‌ها در واقع نوعی فایل خام متنی هستند که شامل لیستی از داده‌ها می‌شوند. به صورت رایج فایل‌های یاد شده برای جابه‌جایی داده‌ها بین نرم‌افزارهای متفاوت مورد استفاده قرار می‌گیرند. برای مثال، پایگاه‌های داده و نرم‌افزارهایی از جمله اکسل معمولا از فایل‌های CSV پشتیبانی می‌کنند. همچین این فایل ها سازگاری بسیار خوبی با زبان پایتون دارند و به آسانی نیز قابل تولید هستند.



با توجه به توضیحات بالا، در ارتباط با پروژه "بررسی نفوذ زبان مغولی قبل و بعد از حمله مغول به ایران" به صورت زیر برنامه نویسی و پیاده سازی شد.

ابتدا برای نصب wordcloud\_fa (که شامل تمامی کتابخانه های مورد نیازمان است) دستور زیر را در خط فرمان وارد می کنیم:

|pip install wordcloud-fa|
| - |

سپس طبق توضیحات موجود در [اسناد کتابخانه](https://github.com/alihoseiny/word_cloud_fa) کد های اولیه را می نویسیم. حاصل کد main.py، تصویر ابر کلمات است. که مشابه آن را در تصویر 6 مشاهده شد.

main.py

from wordcloud\_fa import WordCloudFa

wodcloud = WordCloudFa(no\_reshape=True, persian\_normalize=True, include\_numbers=False, collocations=False, width=1600, height=800, background\_color="white")

text = ""

with open('book.txt', 'r') as file:

`    `text = file.read()

wc = wodcloud.generate(text)

image = wc.to\_image()

image.show()

image.save('output.png')

حال لازم است فایل های کتابخانه ی wordcloud\_fa را طبق نیاز خود تغییر بدهیم. کتابخانه ی wordcloud\_fa برای codespase github که سیستم عامل اوبونتو1 است در آدرس زیرقابل دستیابی است:

|/usr/local/python/3.10.4/lib/python3.10/site-packages/wordcloud\_fa/WordCloudFa.py|
| - |

بعد از باز کردن فایل مذکور برای اینکه با استفاده از تمامی ابزار های هضم، Header File را به صورت زیر تغییر می دهیم:

\# from hazm import Normalizer, word\_tokenize

from hazm import \*

با بررسی ساختار فایل متوجه می شویم لغات در شئی (Class) و تابع (def) زیر جدا می شوند (tokenize).

class WordCloudFa(WordCloud):

`    `def process\_text(self, text: str) -> Dict[str, int]



\1. اوبونتو (به انگلیسی: Ubuntu) یک توزیع گنو/لینوکس بر مبنای دبیان است.

با ایجاد دو ویژگی برنامه را به صورتی که می خواهیم تغییر میدهیم.

الف) تبدیل کلمات به ریشه ی آنها

ب) فیلتر کردن واژگان و جدا سازی واژگان مغولی 

برای ایجاد ویژگی های ذکر شده تکه کد زیر را اضافه می کنیم.

`        `if self.regexp:

`            `words = re.findall(self.regexp, text, flags)

`        `else:

`            `words = word\_tokenize(text)



`        `#############added

`        `#####Stemmer

`        `root = False

`        `if root:

`            `buffer = list()

`            `for i in words:

`                `buffer.append(Stemmer().stem(i))

`            `words = buffer

`        `#####tokeniz and add mogol dic

`        `mogoli = True

`        `if mogoli:

`            `with open("../../mogholi\_dic.txt") as file\_dic:

`                `text = file\_dic.read()

`                `mogoli\_words = word\_tokenize(text)

`            `find\_mogoli = True

`            `if find\_mogoli:

`                `buffer = list()

`                `for i in words:

`                    `for j in mogoli\_words:

`                        `if i == j :

`                            `buffer.append(i)

`                `words = buffer

`        `##############

با تغییر درستی و نادرستی متغیر های root و mogoli در اول دستورات می توان آنها را فعال یا غیر فعال کرد. سپس برای تنظیم قالب خروجی، در شئی و تابع

class WordCloudFa(WordCloud):

`    `def generate\_from\_frequencies(self, frequencies: Dict[str, float], max\_font\_size=None)

قطعه کد زیر را اضافه می کنیم:

`        `if self.persian\_normalize:

`            `words = WordCloudFa.normalize\_words(words)

`        `new\_frequencies = dict(zip(words, values))

`        `############ added

`        `sort\_dic = sorted(new\_frequencies.items(), key=lambda x:x[1], reverse=True)

`        `for i in sort\_dic:

`            `coma = True

`            `for j in i:

`                `print(j, end="")

`                `if coma:

`                    `print(",", end="")

`                    `coma = False

`            `print()

`        `############

حاصل کد بالا خروجی ای به شکل فایل CSV است که هم با پایتون و هم با اکسل قابل بررسی است.

سپس فهرست لغات ایست اختصاصی مورد نظر خود را اضافه کنیم برای این منظور به فایل زیر رفته و آن را با فهرست خود جایگزینش می کنیم.

|/usr/local/python/3.10.4/lib/python3.10/site-packages/wordcloud\_fa/stopwords|
| - |

با اجرای برنامه به صورت زیر، خروجی در فایلی با فرمت CSV (مثلا log.csv) ذخیره می شود.

|Python main.py > log.csv|
| - |

خروجی تفکیک و شمارش کلمات به 4 حالت (همه کلمات، همه کلمات مغولی، ریشه ی همه کلمات، همه ی کلمات با ریشه مغولی) گرفته شد، اما در نهایت فقط خروجی "همه ی کلمات مغولی" و "همه ی کلمات" مورد ارزیابی قرار گرفت. لازم است بررسی شود که چرا ریشه های کلمات به درستی تحلیل نمی شوند.

` `دو خروجی CSV هر ادیب که شامل "همه کلمات مغولی" و "همه ی کلمات" می شود را باهم ادغام کرده و به صورت یک فایل اکسل در می آوریم که برای تحلیل آماده شوند. (جدول 3)

![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.010.png)

جدول 3 – نمایی از ادغام دو فایل خروجی حاصل از کتب مولانا که به صورت یک جدول اکسل درآمده است

تمامی کد ها، ورودی ها و خروجی ها در[ مخزن گیت هاب مربوطه](https://github.com/mvajhi/mogoli-word-after-and-before-war) بارگزاری شده است.



همواره در طی زمان موضوعاتی از این قبیل توسط افرادی متخصص و به صورت جامع مورد پژوهش و بررسی قرار گرفته اند ، اما ما در این پژوهش قصد داریم فقط به بررسی آثار برخی از بزرگان ادبیات بپردازیم که عبارتند از:

[هجویری](https://fa.wikipedia.org/wiki/%D9%87%D8%AC%D9%88%DB%8C%D8%B1%DB%8C) (کشف المحجوب)

[عنصرالمعالی کیکاووس](https://fa.wikipedia.org/wiki/%DA%A9%DB%8C%DA%A9%D8%A7%D9%88%D9%88%D8%B3_%D8%B2%DB%8C%D8%A7%D8%B1%DB%8C) (قابوسنامه)

[مولوی](https://fa.wikipedia.org/wiki/%D9%85%D9%88%D9%84%D9%88%DB%8C) (دیوان شمس – مثنوی معنوی – فیه ما فیه – مجالس سبعه)

[جامی](https://fa.wikipedia.org/wiki/%D8%AC%D8%A7%D9%85%DB%8C) (دیوان اشعار – هفت اورنگ – بهارستان – رساله اربعین)

[عبید زاکانی](https://fa.wikipedia.org/wiki/%D8%B9%D8%A8%DB%8C%D8%AF_%D8%B2%D8%A7%DA%A9%D8%A7%D9%86%DB%8C) (دیوان اشعار – عشاق نامه – اخلاق الشراف – موش وگربه)

برای بررسی بهتر تاثیر این اتفاق آن را به سه دوره زمانی قبل ، هنگام و بعد از آن تقسیم میکنیم ، هرکدام از این بزرگان مربوط به یکی از سه دوره زمانی مربوط به حمله مغول (616-654  هـ . ق) می باشند که در ادامه به بررسی هرکدام خواهیم پرداخت.

` `-1قبل از حمله مغول:

-1-1 علی بن عثمان بن علی جلابی هُجویری غَزنَوی (قرن پنجم هـ . ق)

وی نوشتن کتاب کشف المحجوب را حدود 150 سال قبل از حمله مغول به ایران کمی پیش از سال 465 قمری آغاز کرد.

و تعجبی ندارد که در اثر او تعداد انگشت شماری از کلمات مغولی یافت میشود ، با این حال نگاه کوچکی به این کلمات در غالب یک تصویر می اندازیم.

![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.011.png)([کشف المحجوب](https://github.com/mvajhi/mogoli-word-after-and-before-war/blob/master/finall%20output/hajviri/mogoli.csv))

احتمالا در نگاه اول این سوال مانند ما برایتان ایجاد شده است که این کلمات شباهتی به کلمات مغولی ندارند! و باید در پاسخ به شما بگوییم که حق با شماست ، زیرا برخی از واژگان مغولی با شباهت به واژگان فارسی اما در معنایی متفاوت وجود دارند که نمیتوانیم از آن ها صرف نظر کنیم پس اگر در ادامه باز هم از این قشر کلمات دیدید تعجب نکنید. 

` `-2-1عنصرالمعالی کیکاووس بن اسکندر بن قابوس زیاری (412 – 480 هـ . ق)

وی نصیحت نامه مشهور به قابوسنامه را در سال 475 هجری به اتمام رساند و در این اثر تعداد واژگان بسیار کم است.

![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.012.png)([قابوسنامه](https://github.com/mvajhi/mogoli-word-after-and-before-war/blob/master/finall%20output/keykavos/mogoli.csv))

با توجه به دو نمونه دیده شده و در نظر گرفتن این موضوع که تنها این کلمات اندک از مجموعه 500 واژه مغولی جمع آوری شده توسط ما در این آثار یافت شده اند میتوان نتیجه گرفت که قبل از حمله مغول فارسی زبانان با واژگان مغولی آشنایی نداشته و از آنها استفاده نمی کردند.

حال وقت آن است که کمی در زمان جلوتر برویم و به دوره حمله مغول به ایران برسیم. 




-2 در حین حمله مغول: (616-654 هـ . ق)

` `-1-2جلال‌الدین محمد بلخی معروف به مولوی(604 – 672 هـ . ق)

با وجود این موضوع که عموم آثار مولوی پس از حمله مغول تالیف شده اند ، ما به این دلیل این آثار را در این بخش آوردیم که شخص مولوی در این دوره زمانی حضور داشته و آثار وی بازتاب مناسبی از تاثیر واژگان مغول بر زبان فارسی خواهد بود.

مثنوی معنوی و دیوان شمس آثاری از مولانا اند که به دست وی تالیف شده اند ، در حالی که دو اثر فیه ما فیه و مجالس سبعه برگرفته  از سخنان مولوی میباشند و پس از وفات وی از دست نوشته ها و مکتوبات دیگران جمع آوری شده اند. به همین علت این دو اثر را از نظر زمان پس از مثنوی معنوی و دیوان شمس مورد بررسی قرار خواهیم داد.

در هر کدام از این دو آثار حدود 40 کلمه مغلولی با تکرار تقریبا 400 بار بکار رفته است ، که در مقایسه با آثار هجویری و کیکاووس این ارقام معنادار میشوند.

![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.013.png)([مثنوی](https://github.com/mvajhi/mogoli-word-after-and-before-war/blob/master/while/molana/book/masnavi/log.csv))

![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.014.png)([دیوان شمس]( ))

کتب فیه ما فیه و مجالس سبعه آثاری هستند که به قلم شخص مولوی نوشته نشده اند و زمان تالیف این دو نیز به پس از وفات وی یعنی سال 672 هجری باز میگردد . این دو برخلاف آثار قبل دارای کلمات مغولی بسیار اندکی هستند که تعداد تکرارشان مشابه آثار هجویری و کیکاووس میباشد.


![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.015.png)([فیه ما فیه](https://github.com/mvajhi/mogoli-word-after-and-before-war/blob/master/while/molana/book/fi_ma_fi/log.csv))![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.016.png)([مجالس سبعه]( ))

![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.017.png)([کل آثار](https://github.com/mvajhi/mogoli-word-after-and-before-war/blob/master/finall%20output/molana/mogoli))

حال با دانستن مطالب فوق میتوانیم حداقل درباره شخص مولوی این را بگوییم که قرار گرفتن او در این دوره زمانی بر واژگانی که وارد نوشته هایش میشوند تاثیر بسزایی داشته است. هرچند که این راهم نباید نادیده گرفت که حجم کتبی که که در این دو قسمت تا به اینجا مورد بررسی قرار گرفته است بسیار متفاوت بوده و دارای شرایط یکسانی نیستند.

` `اما این را میدانیم که تنوع کلمات ، ناشی از حجم کتاب نیست.





` `-3 بعد از حمله مغول:

` `دوران پس از حمله مغول دورانیست که واژگان جای خودشان را پیدا میکنند ، یا در میان باقی واژگان جاخوش میکنند و یا در کتب قدیمی می مانند ، اگر زمانی در آن ها بوده اند.

آثار نویسندگان این دوران به ما نشان خواهد داد که آیا واژگان مغولی توانسته اند وارد زبان رسمی یک ملیت شوند یا خیر.

` `-1-3خواجه نظام‌الدین عبیدالله زاکانی (701-772 هـ . ق)

عبید زاکانی 30 سال پس از حمله مغول ها بدنیا آمد.

اما در آثار او اثری از کثرت تنوع و تکرار کلمات نیست .

![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.018.png)([آثار زاکانی](https://github.com/mvajhi/mogoli-word-after-and-before-war/blob/master/finall%20output/zakani/mogoli.csv))

بدون توضیحی بیشتر سراغ آثار بعدی میرویم.

` `-2-3نورالدّین عبد الرّحمن بن احمد بن محمد جامی (817 – 871 هـ . ق)

وی نیز حدود 120 سال پس از حمله مغول ها بدنیا آمده است و مانند زاکانی در آثارش از کلمات بیگانه زیادی استفاده نکرده است.

![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.019.png)([آثار جامی](https://github.com/mvajhi/mogoli-word-after-and-before-war/blob/master/finall%20output/jami/mogol.csv))

در این دوران تعداد واژگان مغولی نسبت به دوران حمله مغول ها کمتر شده است ولی نسبت به دوران قبل از حمله مغول تا حدودی بیشتر است.



نتیجه گیری:

در دوره قبل از حمله مغول ، واژگان بسیار کمی در ادبیات فارسی بوده است با توجه به اینکه قوم مغول اهل ادبیات و نوشتاره نبوده اند.

و در هنگام حمله مغول با سیر بسیار  صعودی آن مواجه شدیم و پس از حمله مغول بزرگان ادبیات دوباره شروع به کاهش استفاده از این قبیل واژگان کردند.

به عبارتی این سه دوره زمانی به صورت یک اوج در ابتدا و یک کاهش در انتها دیده میشود.

منابع:

1. پردازش زبان طبیعی (NLP) چیست؟ - مهرداد توکلی – همیار آی تی ([لینک](https://www.hamyarit.com/blog/nlp/#:~:text=%D9%BE%D8%B1%D8%AF%D8%A7%D8%B2%D8%B4%20%D8%B2%D8%A8%D8%A7%D9%86%20%D8%B7%D8%A8%DB%8C%D8%B9%DB%8C%20\(Natural%20Language,%D8%B2%D8%A8%D8%A7%D9%86%20%D8%A7%D9%86%D8%B3%D8%A7%D9%86%DB%8C%20%D8%B1%D8%A7%20%D8%AF%D8%B1%DA%A9%20%DA%A9%D9%86%D8%AF.))
1. معرفی بهترین کتابخانه‌های پردازش متن - بخش اول – textmining – ویرگول ([لینک](https://blog.text-mining.ir/nlp-lib1-nltk-spacy-corenlp-jrgpcjfyawfx))
1. پردازش زبان طبیعی چیست؟ - نویسنده ناشناس – هوشینو ([لینک](https://hooshio.com/%D9%BE%D8%B1%D8%AF%D8%A7%D8%B2%D8%B4-%D8%B2%D8%A8%D8%A7%D9%86-%D8%B7%D8%A8%DB%8C%D8%B9%DB%8C-%DA%86%DB%8C%D8%B3%D8%AA/))
1. هضم ([لینک](https://www.roshan-ai.ir/hazm/))
1. فایل CSV چیست و چه کاربردی دارد؟ - نویسنده ناشناس – فرادرس ([لینک](https://blog.faradars.org/csv-%DA%86%DB%8C%D8%B3%D8%AA%D8%9F/))
1. مقاله کلمات ترکی – مغولی در کلیات شمس (محمود عابدي - محمد شادرويمنش- بدریه قوامی)
1. واژگان ترکی و مغولی تاریخ جهانگشای جوینی(مصطفی موسوی)
1. بررسی لغات ترکی و مغولی تاریخ گیتی گشا (رضا الوندی- مینا سهرابی)
1. ارتباطِ زبانهای ترکی و مغولی و خطا در تشخیص واژههای دخیل ترکی و مغولی در زبان فارسی (مهدی رضائی)
1. کلمات (ترکی مغولی و عثمانی) در غزلیات مولوی (محمود عابدی – بدریه قوامی)
1. توضیح برخی از لغات و اصطلاحات مغولی در زبان و ادبیات فارسی (دکتر مهری باقری)
1. [ویکی پدیا](https://fa.wikipedia.org/wiki/%D9%81%D9%87%D8%B1%D8%B3%D8%AA_%D9%88%D8%A7%D9%85%E2%80%8C%D9%88%D8%A7%DA%98%D9%87%E2%80%8C%D9%87%D8%A7%DB%8C_%D9%85%D8%BA%D9%88%D9%84%DB%8C_%D8%AF%D8%B1_%D9%81%D8%A7%D8%B1%D8%B3%DB%8C)
1. [مهر میهن](https://www.mehremihan.ir/language-and-dialect/2954-%D9%88%D8%A7%DA%98%DA%AF%D8%A7%D9%86-%D9%85%D8%BA%D9%88%D9%84%DB%8C-%D9%BE%D8%B1%DA%86%D9%85-%D8%8C-%DA%86%D8%A7%D9%82%D9%88-%D8%8C-%D9%82%DB%8C%DA%86%DB%8C-%D8%8C-%D8%B4%D9%82%D8%A7%DB%8C%D9%82)
1. [ویستا](https://vista.ir/m/c/p4els/%D9%84%D8%BA%D8%A7%D8%AA-%D9%85%D8%BA%D9%88%D9%84%DB%8C)








19

بررسی نفوذ زبان مغولی قبل و بعد از حمله مغول به ایران در ادبیات فارسی

![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.020.png)![](Aspose.Words.d07596df-3fe5-4bfe-9acd-838bfa816e38.021.png)

