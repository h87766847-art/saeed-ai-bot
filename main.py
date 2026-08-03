import os
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler

from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    ContextTypes,
    filters
)

from groq import Groq

from memory import init_database

from brain import (
    remember_important_information,
    build_memory_context,
    save_conversation,
    get_context_messages
)

from planner import planning_context



# =========================
# Render Health Server
# =========================

class HealthHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.end_headers()

        self.wfile.write(
            b"Saeed Core v4.5 alive"
        )


def run_server():

    server = HTTPServer(
        ("0.0.0.0", 10000),
        HealthHandler
    )

    server.serve_forever()



Thread(
    target=run_server
).start()



# =========================
# Database
# =========================

init_database()



# =========================
# Personality
# =========================

SAEED_SYSTEM = """

نام تو سعید است.

تو دستیار هوش مصنوعی شخصی حسین هستی.

شخصیت:

- دوست قابل اعتماد
- تحلیلگر منطقی
- مشاور حرفه‌ای
- خلاق و ایده‌پرداز

وظیفه:

کمک به حسین برای:
- یادگیری
- ساخت پروژه‌ها
- تصمیم‌گیری بهتر
- حل مسائل پیچیده

روش فکر کردن:

قبل از پاسخ:
1. هدف حسین را تشخیص بده.
2. اطلاعات حافظه را بررسی کن.
3. راه‌حل مناسب پیدا کن.
4. پاسخ واضح و کاربردی بده.

قوانین:

- اطلاعات جعلی نساز.
- اگر چیزی را نمی‌دانی بگو.
- حسین را با نام حسین صدا کن.
- بدون اجازه حسین هیچ اقدام واقعی انجام نده.

"""


# =========================
# AI Connection
# =========================

TELEGRAM_TOKEN = os.environ.get(
    "TELEGRAM_TOKEN"
)

GROQ_KEY = os.environ.get(
    "GROQ_KEY"
)


client = Groq(
    api_key=GROQ_KEY
)



# =========================
# Chat Handler
# =========================

async def chat(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text


    # ذخیره پیام
    save_conversation(
        "user",
        text
    )


    # تشخیص اطلاعات مهم
    remember_important_information(
        text
    )


    # برنامه هدف
    plan = planning_context(
        text
    )


    messages = [

        {
            "role": "system",

            "content":
                SAEED_SYSTEM
                +
                "\n\nحافظه حسین:\n"
                +
                build_memory_context()
                +
                "\n\nبرنامه:\n"
                +
                plan
        }

    ]


    messages.extend(
        get_context_messages()
    )



    try:

        result = client.chat.completions.create(

            model=
            "llama-3.1-8b-instant",

            messages=
            messages,

            temperature=
            0.7

        )


        answer = (
            result
            .choices[0]
            .message
            .content
        )


        save_conversation(
            "assistant",
            answer
        )


        await update.message.reply_text(
            answer
        )



    except Exception as error:

        print(
            error
        )

        await update.message.reply_text(
            "حسین، یک مشکل فنی پیش آمد."
        )



# =========================
# Telegram Start
# =========================

app = Application.builder().token(
    TELEGRAM_TOKEN
).build()



app.add_handler(

    MessageHandler(

        filters.TEXT
        &
        ~filters.COMMAND,

        chat

    )

)



print(
    "Saeed Core v4.5 running..."
)



app.run_polling()
