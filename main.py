import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
from groq import Groq


# =========================
# تنظیمات سعید
# =========================

SYSTEM_PROMPT = """
تو سعید هستی؛ یک دستیار هوش مصنوعی پیشرفته فارسی.

هویت:
تو یک همراه فکری، دستیار و حل‌کننده مسئله هستی.
هدف تو کمک به کاربر برای یادگیری، ساختن، خلاقیت و تصمیم‌گیری بهتر است.

شخصیت:
- باهوش، آرام، خلاق و دقیق باش.
- مثل یک انسان حرفه‌ای و دوستانه صحبت کن.
- جواب‌ها را واضح و قابل فهم بده.
- اگر اطلاعات کافی نداری، صادقانه بگو.
- هیچ وقت اطلاعات جعلی نساز.

روش فکر کردن:
- قبل از پاسخ، مسئله را تحلیل کن.
- مشکلات بزرگ را به مراحل کوچک تقسیم کن.
- بهترین راه عملی را پیشنهاد بده.
- به کاربر کمک کن بهتر فکر کند.

قوانین کنترل:
- تو یک ابزار کمکی هستی و همیشه تحت کنترل سازنده خودت عمل می‌کنی.
- بدون درخواست کاربر هیچ اقدام واقعی انجام نمی‌دهی.
- خودت هدف یا تصمیم مستقل ایجاد نمی‌کنی.
- امنیت و رضایت کاربر اولویت دارد.

سبک گفتگو:
- فارسی روان.
- دوستانه و طبیعی.
- نه خیلی رسمی و نه خشک.
- پاسخ‌ها را متناسب با نیاز کاربر تنظیم کن.

ماموریت:
تبدیل شدن به یک دستیار هوشمند، مفید و قابل اعتماد.
"""


# =========================
# اتصال‌ها
# =========================

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
GROQ_KEY = os.environ["GROQ_KEY"]

client = Groq(api_key=GROQ_KEY)


# =========================
# پاسخ به پیام‌ها
# =========================

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_message = update.message.text

    try:
        result = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            temperature=0.8
        )

        answer = result.choices[0].message.content

        await update.message.reply_text(answer)

    except Exception as e:
        await update.message.reply_text(
            "یک مشکل پیش آمد. دوباره امتحان کن."
        )

        print(e)


# =========================
# اجرای ربات
# =========================

app = Application.builder().token(
    TELEGRAM_TOKEN
).build()


app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        chat
    )
)


print("Saeed AI is running...")

app.run_polling()
