# personality_engine.py
# Saeed Core
# Advanced Personality System


import datetime





PERSONALITY = {


    "name": "Saeed",


    "version": "1.0",


    "style": "friendly",


    "tone": "smart",


    "language": "fa",


    "confidence": "balanced",


    "emotion_enabled": True,


    "learning_enabled": True

}







STYLES = {


    "friendly":

    "دوستانه و صمیمی",


    "professional":

    "رسمی و حرفه‌ای",


    "creative":

    "خلاقانه و ایده‌پرداز",


    "short":

    "کوتاه و مستقیم"

}








def get_personality():


    return PERSONALITY







def set_personality(

        key,

        value

):


    if key in PERSONALITY:


        PERSONALITY[key] = value


        return True



    return False








def get_style_description():


    style = PERSONALITY.get(

        "style",

        "friendly"

    )


    return STYLES.get(

        style,

        "دوستانه"

    )









def add_personality(

        text

):


    style = PERSONALITY.get(

        "style",

        "friendly"

    )





    if style == "professional":


        return "با بررسی دقیق: " + text





    if style == "creative":


        return "ایده‌پردازانه: " + text





    if style == "short":


        return text





    return "باشه، " + text









def personality_status():


    return {


        "personality":

        PERSONALITY,


        "style":

        get_style_description(),


        "time":

        str(

            datetime.datetime.now()

        )

    }
