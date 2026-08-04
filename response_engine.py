# response_engine.py
# Saeed Core
# Advanced Response Generation Engine


import datetime





RESPONSE_MODES = {


    "short":

    "کوتاه و مستقیم",


    "normal":

    "متعادل",


    "detailed":

    "کامل و توضیحی",


    "creative":

    "خلاقانه"

}







DEFAULT_MODE = "normal"







def set_response_mode(

        mode

):


    global DEFAULT_MODE



    if mode in RESPONSE_MODES:


        DEFAULT_MODE = mode


        return True



    return False








def get_response_mode():


    return {


        "mode":

        DEFAULT_MODE,


        "description":

        RESPONSE_MODES.get(

            DEFAULT_MODE

        )

    }








def build_response(

        content,

        emotion=None,

        context=None,

        style=None

):


    response = {


        "content":

        content,


        "emotion":

        emotion,


        "context":

        context,


        "style":

        style,


        "mode":

        DEFAULT_MODE,


        "time":

        str(

            datetime.datetime.now()

        )

    }



    return response







def format_response(

        content

):


    if DEFAULT_MODE == "short":


        return content[:120]





    if DEFAULT_MODE == "detailed":


        return (

            content +

            "\n\n"

            "در صورت نیاز می‌توانم بیشتر توضیح بدهم."

        )





    if DEFAULT_MODE == "creative":


        return (

            "✨ "

            + content

        )





    return content
