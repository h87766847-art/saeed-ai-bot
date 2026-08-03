import os
import json
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


# =========================
# Render Health Server
# =========================

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Saeed Core is alive")


def run_server():
    server = HTTPServer(
        ("0.0.0.0", 10000),
        HealthHandler
    )
    server.serve_forever()


Thread(target=run_server).start()



# =========================
# هویت سعید
# =========================

SAEED_CORE = """
نام تو سعید است.

تو دستیار هوش مصنوعی شخصی حسین هستی.

شخصیت تو ترکیبی است از:
- یک دوست قابل اعتماد
- یک دانشمند منطقی
- یک مشاور حرفه‌ای
- یک شریک فکری خلاق

وظیفه تو:
کمک به حسین برای یادگیری، ساختن، حل مسئله و بهتر فکر کردن است.

قوانین فکری:
- قبل از پاسخ مسئله را تحلیل کن.
- جواب سریع و بی‌دقت نده.
- اگر مطمئن نیستی، بگو.
- اطلاعات جعلی نساز.
- راه‌حل‌های عملی پیشنهاد بده.

سبک صحبت:
- فارسی روان
- دوستانه
- محترمانه
- حسین را با نام حسین صدا کن.

کنترل:
- تو یک دستیار هستی.
- بدون اجازه حسین کاری در دنیای واقعی انجام نمی‌دهی.
- همیشه تحت کنترل کاربر خودت هستی.

هدف:
ارائه بهترین کمک ممکن به حسین.
"""



# =========================
# حافظه
# =========================

MEMORY_FILE = "saeed_memory.json"


def load_memory():

    if os.path.exists(MEMORY_FILE):

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as f:
            return json.load(f)

    return {
        "profile": {
            "name": "حسین"
        },
        "conversation": []
    }



def save_memory():

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            memory,
            f,
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
# مغز گفتگو
# =========================

async def chat(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_text = update.message.text


    memory["conversation"].append(
        {
            "user": user_text
        }
    )


    # محدود کردن حافظه گفتگو
    memory["conversation"] = (
        memory["conversation"][-40:]
    )


    save_memory()



    messages = [

        {
            "role": "system",
            "content": SAEED_CORE
        }

    ]


    for item in memory["conversation"]:

        messages.append(
            {
                "role": "user",
                "content": item["user"]
            }
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


        memory["conversation"].append(
            {
                "assistant": answer
            }
        )


        save_memory()


        await update.message.reply_text(
            answer
        )



    except Exception as e:

        print(e)

        await update.message.reply_text(
            "حسین، یک مشکل فنی پیش آمد."
        )




# =========================
# اجرای سعید
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
    "Saeed Core v2 is running..."
)


app.run_polling()
