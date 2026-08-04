import os

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters
)

from main import process_message


TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "سلام، سعید آماده است."
    )



async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    result = process_message(text)


    if isinstance(result, dict):

        answer = result.get(
            "message",
            str(result)
        )

    else:

        answer = str(result)


    await update.message.reply_text(
        answer
    )



def main():

    app = ApplicationBuilder()\
        .token(TOKEN)\
        .build()


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
        "Saeed Telegram Bot Running..."
    )


    app.run_polling()



if __name__ == "__main__":

    main()
