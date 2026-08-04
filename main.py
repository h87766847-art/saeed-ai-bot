# main.py
# Saeed Core v6.3
# Telegram AI Assistant Main


import os
import logging


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
    save_conversation,
    init_database
)


from core_router import (
    analyze_request
)



# تنظیمات لاگ
logging.basicConfig(
    level=logging.INFO
)



# توکن ربات
TOKEN = os.getenv(
    "BOT_TOKEN"
)



# شروع دیتابیس
init_database()





async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "سلام 👋\n"
        "Saeed AI Core فعال شد."
    )





async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user_text = update.message.text


    try:

        # عبور از روتر هوشمند
        result = analyze_request(
            user_text
        )


        # پردازش مغز
        brain_result = process_brain(
            user_text,
            result
        )


        response = str(
            brain_result
        )


        save_conversation(
            user_text,
            response
        )


        await update.message.reply_text(
            response[:4000]
        )



    except Exception as e:


        logging.error(e)


        await update.message.reply_text(
            "خطا در پردازش پیام ❌"
        )







def main():


    if not TOKEN:

        print(
            "BOT_TOKEN پیدا نشد"
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
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message
        )
    )



    print(
        "Saeed AI Bot Started..."
    )



    app.run_polling()





if __name__ == "__main__":

    main()
