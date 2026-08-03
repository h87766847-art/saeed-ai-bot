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


from self_evaluator import create_evaluation_prompt


from core_router import route_message


from knowledge_router import retrieve_knowledge


from personality_core import (
    init_personality,
    get_personality
)





# =========================
# Health Server
# =========================


class HealthHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)

        self.end_headers()

        self.wfile.write(
            b"Saeed Core v15.1 alive"
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






# =========================
# Initialize
# =========================


init_database()

init_personality()






# =========================
# Personality
# =========================


personality = get_personality()



SYSTEM = f"""

تو {personality["name"]} هستی.

دستیار هوش مصنوعی شخصی {personality["user"]}.


سبک:

{personality["style"]}


قوانین:

{chr(10).join(personality["behavior_rules"])}


همیشه:

- دقیق جواب بده.
- منطقی تحلیل کن.
- اگر مطمئن نیستی بگو.
- از حافظه و دانش مرتبط استفاده کن.

"""







# =========================
# API
# =========================


TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

GROQ_KEY = os.environ["GROQ_KEY"]



client = Groq(
    api_key=GROQ_KEY
)







# =========================
# Chat
# =========================


async def chat(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):


    text = update.message.text





    save_conversation(
        "user",
        text
    )




    remember_important_information(
        text
    )






    # =====================
    # Router
    # =====================


    route = route_message(
        text
    )






    if route["type"] == "tool":


        answer = route["data"]


        save_conversation(
            "assistant",
            answer
        )


        await update.message.reply_text(
            answer
        )


        return







    if route["type"] == "decision":


        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[

                {
                    "role":"system",
                    "content":SYSTEM
                },


                {
                    "role":"user",
                    "content":route["data"]
                }

            ],

            temperature=0.5

        )



        answer = (

            response
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


        return







    # =====================
    # Memory + Knowledge
    # =====================


    knowledge = retrieve_knowledge(
        text
    )



    plan = planning_context(
        text
    )







    messages = [


        {

            "role":"system",

            "content":

            SYSTEM


            +

            "\n\nحافظه حسین:\n"

            +

            build_memory_context()



            +

            "\n\nدانش مرتبط:\n"

            +

            knowledge



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


        # جواب اولیه


        response = client.chat.completions.create(


            model="llama-3.1-8b-instant",


            messages=messages,


            temperature=0.7

        )



        draft = (

            response
            .choices[0]
            .message
            .content

        )








        # Reflection


        reflection_prompt = create_reflection_prompt(

            draft,

            text

        )





        reflection = client.chat.completions.create(


            model="llama-3.1-8b-instant",


            messages=[

                {

                    "role":"user",

                    "content":reflection_prompt

                }

            ],


            temperature=0.3

        )





        improved = (

            reflection
            .choices[0]
            .message
            .content

        )








        # Self Evaluation


        evaluation_prompt = create_evaluation_prompt(

            text,

            improved

        )






        evaluation = client.chat.completions.create(


            model="llama-3.1-8b-instant",


            messages=[

                {

                    "role":"user",

                    "content":evaluation_prompt

                }

            ],


            temperature=0.2

        )






        answer = (

            evaluation
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

            "حسین، خطای فنی پیش آمد."

        )









# =========================
# Telegram
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
    "Saeed Core v15.1 running..."
)





app.run_polling()
