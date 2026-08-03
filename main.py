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

from reflection import create_reflection_prompt

from tool_router import check_tools



# =========================
# Render
# =========================

class HealthHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.end_headers()

        self.wfile.write(
            b"Saeed Core v6.2 alive"
        )


def run_server():

    server = HTTPServer(
        ("0.0.0.0",10000),
        HealthHandler
    )

    server.serve_forever()



Thread(
    target=run_server
).start()



init_database()



SYSTEM = """

تو سعید هستی.

دستیار هوش مصنوعی شخصی حسین.

ویژگی‌ها:

- دقیق
- منطقی
- خلاق
- کمک‌کننده

قبل از جواب:
حافظه را بررسی کن.
هدف را بفهم.
بهترین راه را انتخاب کن.

حسین را با نام حسین صدا کن.

"""



TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

GROQ_KEY = os.environ["GROQ_KEY"]


client = Groq(
    api_key=GROQ_KEY
)




async def chat(update, context):

    text = update.message.text


    save_conversation(
        "user",
        text
    )


    remember_important_information(
        text
    )


    # بررسی ابزار

    tool = check_tools(
        text
    )


    if tool["used"]:

        answer = tool["result"]

        save_conversation(
            "assistant",
            answer
        )


        await update.message.reply_text(
            answer
        )

        return



    plan = planning_context(
        text
    )



    messages = [

        {
            "role":"system",

            "content":
            SYSTEM
            +
            "\n\nحافظه:\n"
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

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=messages,

            temperature=0.7

        )


        answer = (
            response
            .choices[0]
            .message
            .content
        )


        review_prompt = create_reflection_prompt(
            answer,
            text
        )


        review = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role":"user",
                    "content":review_prompt
                }
            ],

            temperature=0.3

        )


        final_answer = (
            review
            .choices[0]
            .message
            .content
        )


        save_conversation(
            "assistant",
            final_answer
        )


        await update.message.reply_text(
            final_answer
        )



    except Exception as e:

        print(e)

        await update.message.reply_text(
            "حسین، مشکل فنی پیش آمد."
        )





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
    "Saeed Core v6.2 running..."
)



app.run_polling()
