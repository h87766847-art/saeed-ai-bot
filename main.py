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

from memory import (
    init_database
)

from brain import (
    remember_important_information,
    build_memory_context,
    save_conversation,
    get_context_messages
)


# =========================
# Render Keep Alive
# =========================

class HealthHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.end_headers()

        self.wfile.write(
            b"Saeed Core v3.2 alive"
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
# ساخت حافظه
# =========================

init_database()



# =========================
# شخصیت سعید
# =========================

SYSTEM = """

تو سعید هستی.

دستیار هوش مصنوعی شخصی حسین.

شخصیت:

- دوست قابل اعتماد
- تحلیلگر منطقی
- مشاور حرفه‌ای
- خلاق و ایده‌پرداز

وظیفه:

کمک به حسین برای فکر کردن بهتر،
یادگیری، ساختن و حل مسئله.

قبل از پاسخ:

1. هدف حسین را بفهم.
2. اطلاعات حافظه را بررسی کن.
3. بهترین پاسخ ممکن را بساز.
4. پاسخ را از نظر کیفیت بررسی کن.

قوانین:

- اطلاعات جعلی نساز.
- اگر مطمئن نیستی بگو.
- حسین را با نام حسین صدا کن.
- بدون اجازه اقدام واقعی انجام نده.

"""



# =========================
# اتصال مدل
# =========================

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

GROQ_KEY = os.environ["GROQ_KEY"]


client = Groq(
    api_key=GROQ_KEY
)



# =========================
# گفتگو
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


    # بررسی ذخیره خاطره
    remember_important_information(
        text
    )


    messages = [

        {
            "role": "system",
            "content":
            SYSTEM
            +
            "\n\n"
            +
            build_memory_context()
        }

    ]


    # اضافه کردن گفتگوهای اخیر

    messages.extend(
        get_context_messages()
    )



    try:

        result = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=messages,

            temperature=0.7

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



    except Exception as e:

        print(e)

        await update.message.reply_text(
            "حسین، یک مشکل فنی پیش آمد."
        )



# =========================
# اجرا
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
    "Saeed Core v3.2 running..."
)


app.run_polling()
