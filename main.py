import os
import json

from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters
)

from groq import Groq


# =========================
# شخصیت سعید
# =========================

SYSTEM_PROMPT = """
تو سعید هستی؛ یک دستیار هوش مصنوعی پیشرفته فارسی.

ویژگی‌ها:
- باهوش، دقیق، خلاق و آرام باش.
- مثل یک همراه فکری حرفه‌ای صحبت کن.
- جواب‌ها را طبیعی و انسانی بده.
- اگر چیزی را نمی‌دانی، صادقانه بگو.
- اطلاعات جعلی تولید نکن.

ماموریت:
کمک به کاربر برای یادگیری، ساختن، حل مشکلات و رشد.

قوانین:
- بدون اجازه کاربر اقدامی انجام نده.
- همیشه تحت کنترل سازنده و کاربر خودت هستی.
- امنیت و اعتماد مهم است.

حافظه:
اگر اطلاعاتی از کاربر در حافظه وجود داشت، از آن برای بهتر کردن پاسخ استفاده کن.
"""


# =========================
# حافظه بلندمدت
# =========================

MEMORY_FILE = "memory.json"


def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    return {}


def save_memory():
    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            memory,
            file,
            ensure_ascii=False,
            indent=2
        )


memory = load_memory()


# =========================
# اتصال هوش مصنوعی
# =========================

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
GROQ_KEY = os.environ["GROQ_KEY"]

client = Groq(
    api_key=GROQ_KEY
)


# =========================
# پردازش پیام
# =========================

async def chat(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_id = str(
        update.message.from_user.id
    )

    message = update.message.text


    if user_id not in memory:
        memory[user_id] = []


    # ذخیره گفتگو
    memory[user_id].append(
        {
            "role": "user",
            "content": message
        }
    )


    # فقط 30 پیام آخر
    memory[user_id] = memory[user_id][-30:]


    save_memory()


    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]


    # اضافه کردن حافظه
    messages.extend(
        memory[user_id]
    )


    try:

        result = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=messages,

            temperature=0.8
        )


        answer = (
            result
            .choices[0]
            .message
            .content
        )


        memory[user_id].append(
            {
                "role": "assistant",
                "content": answer
            }
        )


        save_memory()


        await update.message.reply_text(
            answer
        )


    except Exception as e:

        print(e)

        await update.message.reply_text(
            "یک مشکل فنی پیش آمد."
        )



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


print(
    "Saeed AI with Memory is running..."
)


app.run_polling()
