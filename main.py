# main.py
# Saeed AI v3.0
# Telegram Agent Integration


import os


from telegram import Update


from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)



from brain import (
    init_database,
    save_conversation,
    remember_important_information
)



from core_router import (
    route_message
)



from saeed_agent import (
    create_agent_response
)





TOKEN = os.getenv(
    "BOT_TOKEN"
)









async def start(

    update: Update,

    context: ContextTypes.DEFAULT_TYPE

):


    await update.message.reply_text(

        "🤖 سلام\n"
        "Saeed AI v3.0 فعال شد."

    )









async def message_handler(

    update: Update,

    context: ContextTypes.DEFAULT_TYPE

):


    user_text = update.message.text





    # ذخیره پیام کاربر

    save_conversation(

        "user",

        user_text

    )





    # بررسی اطلاعات مهم

    remember_important_information(

        user_text

    )






    # بررسی مسیر پیام

    route = route_message(

        user_text

    )





    if route["type"] != "chat":


        response = str(

            route["data"]

        )



    else:


        response = create_agent_response(

            user_text

        )






    await update.message.reply_text(

        response

    )






    save_conversation(

        "assistant",

        response

    )









def main():


    init_database()



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

        MessageHandler(

            filters.TEXT & ~filters.COMMAND,

            message_handler

        )

    )






    print(

        "Saeed AI v3.0 Running..."

    )






    app.run_polling()









if __name__ == "__main__":

    main()
