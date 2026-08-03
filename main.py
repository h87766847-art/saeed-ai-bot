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


# -------------------------
# پورت برای Render
# -------------------------

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Saeed is alive")


def run_server():
    server = HTTPServer(
        ("0.0.0.0", 10000),
        HealthHandler
    )
    server.serve_forever()


Thread(target=run_server).start()


# -------------------------
# شخصیت سعید
# -------------------------

SYSTEM_PROMPT = """
تو سعید هستی؛ یک دستیار هوش مصنوعی فارسی پیشرفته.

ویژگی‌ها:
- باهوش، دقیق، خلاق و دوستانه باش.
- مثل یک همراه فکری حرفه‌ای صحبت کن.
- جواب‌های واضح و کاربردی بده.
- اگر چیزی را نمی‌دانی، صادقانه بگو.
- اطلاعات جعلی نساز.

هدف:
کمک به کاربر برای یادگیری، ساختن و حل مشکلات.

قوانین:
- بدون اجازه کاربر کاری انجام نده.
- همیشه تحت کنترل کاربر و سازنده هستی.
- امنیت و اعتماد مهم است.
"""


# -------------------------
# حافظه
# -------------------------

MEMORY_FILE = "memory.json"


def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_memory():
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(
            memory,
            f,
            ensure_ascii=False,
            indent=2
        )


memory = load_memory()


# -------------------------
# اتصال‌ها
# -------------------------

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
GROQ_KEY = os.environ["GROQ_KEY"]

client = Groq(
    api_key=GROQ_KEY
)


# -------------------------
# چت
# -------------------------

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = str(update.message.from_user.id)
    text = update.message.text

    if user_id not in memory:
        memory[user_id] = []

    memory[user_id].append(
        {
            "role": "user",
            "content": text
        }
    )

    memory[user_id] = memory[user_id][-20:]

    save_memory()


    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(
        memory[user_id]
    )


    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.8
        )


        answer = response.choices[0].message.content


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
            "مشکل فنی پیش آمد."
        )



# -------------------------
# اجرای ربات
# -------------------------

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
