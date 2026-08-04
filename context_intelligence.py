# context_intelligence.py
# Saeed Core v7.0
# Context Intelligence System


import datetime





CONTEXT_TYPES = {


    "technical":

    [

        "کد",

        "برنامه",

        "خطا",

        "فایل",

        "پایتون",

        "api"

    ],


    "question":

    [

        "چرا",

        "چگونه",

        "چطور",

        "چی"

    ],


    "creative":

    [

        "ایده",

        "بساز",

        "طراحی",

        "داستان"

    ],


    "learning":

    [

        "یادگیری",

        "آموزش",

        "یاد بده"

    ]

}







def detect_context(

        text

):


    text = text.lower()



    scores = {}



    for context, words in CONTEXT_TYPES.items():


        score = 0



        for word in words:


            if word in text:


                score += 1



        scores[context] = score





    selected = max(

        scores,

        key=scores.get

    )





    if scores[selected] == 0:


        selected = "general"





    return {


        "type":

        selected,


        "confidence":

        scores.get(

            selected,

            0

        ),


        "scores":

        scores,


        "time":

        str(

            datetime.datetime.now()

        )

    }









def get_context_information(

        text

):


    return detect_context(

        text

    )








def context_status():


    return {


        "contexts":

        len(CONTEXT_TYPES),


        "status":

        "active"

    }
