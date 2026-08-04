# intent_engine.py
# Saeed Core
# Advanced Intent Detection System


import datetime





INTENTS = {


    "question":

    [

        "چرا",

        "چی",

        "چگونه",

        "چطور",

        "کدام"

    ],


    "request":

    [

        "بساز",

        "اضافه کن",

        "انجام بده",

        "کمک کن",

        "بفرست"

    ],


    "problem":

    [

        "خطا",

        "خراب",

        "کار نمی‌کند",

        "مشکل"

    ],


    "learning":

    [

        "یاد بگیر",

        "یادگیری",

        "آموزش"

    ],


    "command":

    [

        "اجرا",

        "شروع",

        "باز کن"

    ]

}







def detect_intent(

        text

):


    text = text.lower()



    scores = {}



    for intent, words in INTENTS.items():


        score = 0



        for word in words:


            if word in text:


                score += 1



        scores[intent] = score





    result = max(

        scores,

        key=scores.get

    )





    if scores[result] == 0:


        result = "unknown"





    return {


        "intent":

        result,


        "confidence":

        scores.get(

            result,

            0

        ),


        "scores":

        scores,


        "time":

        str(

            datetime.datetime.now()

        )

    }









def get_intent_type(

        text

):


    return detect_intent(

        text

    )["intent"]
