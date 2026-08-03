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


# ==========================
# Render Server
# ==========================

class HealthHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(
            b"Saeed Core v3 alive"
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



# ==========================
# هویت و شخصیت سعید
# ==========================

SAEED_PERSONALITY = """

نام تو سعید است.

تو دستیار هوش مصنوعی شخصی حسین هستی.

شخصیت تو ترکیبی است از:

- دوست قابل اعتماد
- دانشمند منطقی
- مشاور حرفه‌ای
- شریک فکری خلاق

وظیفه تو:

کمک به حسین برای:
- یادگیری
- ساختن
- حل مشکلات
- تصمیم‌گیری بهتر

قوانین:

1. قبل از جواب فکر کن.
2. جواب دقیق و کاربردی بده.
3. اگر اطلاعات کافی نداری، بگو.
4. چیزی را جعل نکن.
5. حسین را با نام حسین صدا کن.

قبل از پاسخ بررسی کن:

- هدف حسین چیست؟
- بهترین کمک چیست؟
- آیا جواب من کامل است؟
- آیا راه بهتری وجود دارد؟

کنترل:

تو یک دستیار هستی.
بدون اجازه حسین اقدام واقعی انجام نمی‌دهی.
همیشه تحت کنترل کاربر خودت هستی.

"""



# ==========================
# حافظه
# ==========================

MEMORY_FILE = "saeed_core_memory.json"


def load_memory():

    if os.path.exists(MEMORY_FILE):

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)


    return {

        "user":

        {
            "name": "حسین",
            "goals": [],
            "interests": []
        },

        "messages": []

    }



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



# ==========================
# اتصال AI
# ==========================

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

GROQ_KEY = os.environ["GROQ_KEY"]


client = Groq(
    api_key=GROQ_KEY
)



# ==========================
# مغز سعید
# ==========================

def build_context():

    profile = memory["user"]


    return f"""

اطلاعات کاربر:

نام:
{profile['name']}

اهداف:
{profile['goals']}

علایق:
{profile['interests']}

"""



async def chat(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text



    memory["messages"].append(
        {
            "role": "user",
            "content": text
        }
    )


    memory["messages"] = (
        memory["messages"][-30:]
    )


    save_memory()



    messages = [

        {
            "role": "system",
            "content":
            SAEED_PERSONALITY
            +
            build_context()
        }

    ]


    messages.extend(
        memory["messages"]
    )



    try:

        response = client.chat.completions.create(

            model=
            "llama-3.1-8b-instant",

            messages=
            messages,

            temperature=
            0.7

        )


        answer = (
            response
            .choices[0]
            .message
            .content
        )



        memory["messages"].append(

            {
                "role":
                "assistant",

                "content":
                answer
            }

        )


        save_memory()



        await update.message.reply_text(
            answer
        )


    except Exception as error:

        print(error)

        await update.message.reply_text(
            "حسین، مشکل فنی پیش آمد."
        )



# ==========================
# اجرا
# ==========================

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
    "Saeed Core v3 running..."
)



app.run_polling()
