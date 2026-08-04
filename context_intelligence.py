# context_intelligence.py
# Saeed Core
# Advanced Context Intelligence System


import datetime
import re





CONTEXT_TYPES = {


    "question": [

        "چی",
        "چرا",
        "چطور",
        "چگونه",
        "آیا",
        "؟"

    ],



    "learning": [

        "یاد بده",
        "آموزش",
        "یاد بگیرم",
        "توضیح بده"

    ],



    "coding": [

        "کد",
        "برنامه",
        "پایتون",
        "فایل",
        "خطا",
        "ارور"

    ],



    "creative": [

        "بساز",
        "ایده",
        "داستان",
        "انیمیشن",
        "ویدیو"

    ],



    "personal": [

        "من",
        "دوست دارم",
        "احساس",
        "حالم"

    ]

}








def detect_context(text):


    text = text.lower()



    scores = {}



    for context, keywords in CONTEXT_TYPES.items():


        score = 0


        for word in keywords:


            if word in text:

                score += 1



        scores[context] = score






    best = max(

        scores,

        key=scores.get

    )





    if scores[best] == 0:

        best = "general"





    return {


        "type": best,


        "confidence":
        scores.get(
            best,
            0
        ),


        "all_scores": scores,


        "time":
        str(
            datetime.datetime.now()
        )

    }








def get_context_information(text):


    return detect_context(
        text
    )








def extract_keywords(text):


    words = re.findall(

        r'\w+',

        text

    )


    return words







def is_technical_context(text):


    context = detect_context(
        text
    )


    return context["type"] == "coding"
