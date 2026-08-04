import os
import datetime

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# اتصال سیستم ارتقا
try:
    from saeed_upgrade_command import upgrade_command
except Exception:
    upgrade_command = None


try:
    from core_router import route_message
except Exception:
    route_message = None


SYSTEM_NAME = "Saeed Core"
VERSION = "7.5"


def process_message(message):

    try:

        if route_message:
            return route_message(message)

        return "Core router not found"

    except Exception as e:

        return f"Error: {e}"



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "سعید دوباره فعال شد ✅"
    )



# دستور جدید ارتقا
async def upgrade_check(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:

        if upgrade_command:

            result = upgrade_command()

            await update.message.reply_text(
                str(result)
            )

        else:

            await update.message.reply_text(
                "Upgrade system not connected"
            )

    except Exception as e:

        await update.message.reply_text(
            f"Upgrade error: {e}"
        )



async def telegram_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = update.message.text

    answer = process_message(text)


    if isinstance(answer, dict):

        answer = answer.get(
            "message",
            str(answer)
        )


    await update.message.reply_text(
        str(answer)
    )



def start_bot():

    token = os.getenv("BOT_TOKEN")


    if not token:

        print("BOT_TOKEN missing")

        return



    app = ApplicationBuilder()\
        .token(token)\
        .build()



    # دستور شروع
    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    # دستور ارتقا
    app.add_handler(
        CommandHandler(
            "upgrade",
            upgrade_check
        )
    )


    # پیام‌های عادی
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            telegram_handler
        )
    )



    print("Saeed Telegram Connected...")

    print(
        "Time:",
        datetime.datetime.now()
    )


    app.run_polling()



if __name__ == "__main__":

    start_bot()
