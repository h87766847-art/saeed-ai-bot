import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)


from core_router import route_message

from brain import (
    save_conversation,
    remember_important_information,
    init_database,
    build_memory_context
)


from context_intelligence import (
    get_context_information
)





TOKEN = os.getenv(
    "BOT_TOKEN"
)





# =========================
# شروع ربات
# =========================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):


    await update.message.reply_text(

        "سلام حسین 👋\n"
        "سعید آماده است."

    )








# =========================
# پردازش پیام
# =========================

async def message_handler(

    update: Update,

    context: ContextTypes.DEFAULT_TYPE

):


    user_text = update.message.text



    # ذخیره پیام

    save_conversation(

        "user",

        user_text

    )


    # تحلیل حافظه و زمینه

    remember_important_information(

        user_text

    )



    # مسیریابی

    route = route_message(

        user_text

    )






    # =====================
    # Decision Analysis
    # =====================

    if route["type"] == "decision_analysis":


        analysis = route["data"]


        response = (

            "⚖️ تحلیل تصمیم\n\n"

            "موضوع:\n"

            +

            analysis["problem"]

            +

            "\n\nگزینه‌ها:\n"

        )



        for option in analysis["options"]:


            response += (

                "\n• "

                +

                option["name"]

            )



        await update.message.reply_text(

            response

        )


        save_conversation(

            "assistant",

            response

        )


        return







    # =====================
    # Goal
    # =====================

    if route["type"] == "goal":


        response = str(

            route["data"]

        )


        await update.message.reply_text(

            response

        )


        return







    # =====================
    # Tool
    # =====================

    if route["type"] == "tool":


        response = str(

            route["data"]

        )


        await update.message.reply_text(

            response

        )


        return







    # =====================
    # Decision ساده
    # =====================

    if route["type"] == "decision":


        await update.message.reply_text(

            route["data"]

        )


        return







    # =====================
    # Chat معمولی
    # =====================


    memory = build_memory_context()

    context = get_context_information()



    response = (

        "🧠 وضعیت حافظه:\n"

        +

        context

        +

        "\n\n"

        +

        "پیام دریافت شد:\n"

        +

        user_text

    )




    await update.message.reply_text(

        response

    )



    save_conversation(

        "assistant",

        response

    )









# =========================
# اجرای اصلی
# =========================

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
        "Saeed AI is running..."
    )



    app.run_polling()






if __name__ == "__main__":

    main()
