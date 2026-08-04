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
    init_database
)


from response_engine import (
    generate_response
)


from self_evaluator import (
    evaluate
)


from reflection_engine import (
    create_reflection
)


from learning_loop import (
    add_experience
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

        "سلام 👋\n"
        "سعید AI v2 آماده است."

    )









# =========================
# پردازش پیام
# =========================

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




    # استخراج اطلاعات مهم

    remember_important_information(

        user_text

    )





    # مسیریابی

    route = route_message(

        user_text

    )







    # =====================
    # ابزار
    # =====================

    if route["type"] == "tool":


        response = str(

            route["data"]

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
    # تصمیم ساده
    # =====================

    if route["type"] == "decision":


        response = str(

            route["data"]

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
    # تحلیل تصمیم
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
    # هدف
    # =====================

    if route["type"] == "goal":


        response = str(

            route["data"]

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
    # چت هوشمند
    # =====================


    response = generate_response(

        user_text

    )




    await update.message.reply_text(

        response

    )




    save_conversation(

        "assistant",

        response

    )







    # =====================
    # خودارزیابی و یادگیری
    # =====================


    evaluate(

        user_text,

        response,

        8

    )



    create_reflection(

        user_text,

        True,

        "پاسخ تولید شد و برای بهبود آینده ثبت شد"

    )



    add_experience(

        user_text,

        response,

        "تجربه جدید ذخیره شد"

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

        "Saeed AI v2 is running..."

    )





    app.run_polling()







if __name__ == "__main__":

    main()
