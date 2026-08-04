# main.py
# Saeed Core
# Advanced Telegram Interface


import os
import logging
import traceback



from telegram import Update


from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)



from brain import (
    process_brain,
    save_conversation
)


from core_router import (
    analyze_request
)





# -------------------------
# Logging
# -------------------------


logging.basicConfig(

    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",

    level=logging.INFO

)


logger = logging.getLogger(
    "Saeed"
)






# -------------------------
# Config
# -------------------------


TOKEN = os.getenv(
    "BOT_TOKEN"
)







# -------------------------
# Commands
# -------------------------


async def start(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):


    await update.message.reply_text(

        "سلام 👋\n"
        "سعید فعال شد.\n"
        "هسته هوشمند آماده دریافت پیام است."

    )







async def status(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):


    await update.message.reply_text(

        "🧠 Saeed Core Online\n"
        "Memory: Active\n"
        "Brain: Active\n"
        "Router: Active"

    )









# -------------------------
# Message Processor
# -------------------------


async def handle_message(

        update: Update,

        context: ContextTypes.DEFAULT_TYPE

):


    try:


        user_text = update.message.text



        if not user_text:

            return






        # Router

        route = analyze_request(

            user_text

        )






        # Brain

        result = process_brain(

            user_text,

            context=route

        )






        response = result.get(

            "response",

            "پیام پردازش شد."

        )







        save_conversation(

            user_text,

            response

        )







        await update.message.reply_text(

            response

        )







    except Exception as e:


        logger.error(

            str(e)

        )


        traceback.print_exc()



        await update.message.reply_text(

            "خطایی در پردازش رخ داد."

        )









# -------------------------
# Error Handler
# -------------------------


async def error_handler(

        update,

        context

):


    logger.error(

        "Telegram Error",

        exc_info=context.error

    )









# -------------------------
# Run
# -------------------------


def main():


    if not TOKEN:


        print(

            "BOT_TOKEN تنظیم نشده"

        )

        return






    app = Application.builder().token(

        TOKEN

    ).build()






    app.add_handler(

        CommandHandler(

            "start",

            start

        )

    )





    app.add_handler(

        CommandHandler(

            "status",

            status

        )

    )





    app.add_handler(

        MessageHandler(

            filters.TEXT & ~filters.COMMAND,

            handle_message

        )

    )






    app.add_error_handler(

        error_handler

    )






    print(

        "Saeed Core Started..."

    )






    app.run_polling()








if __name__ == "__main__":

    main()
