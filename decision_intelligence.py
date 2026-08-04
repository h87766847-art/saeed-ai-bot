# decision_intelligence.py
# Saeed Core
# Advanced Decision Intelligence System


import datetime





DECISION_PATTERNS = {


    "question": [

        "چی",
        "چرا",
        "چطور",
        "چگونه",
        "آیا",
        "؟"

    ],



    "command": [

        "برو",
        "اجرا کن",
        "فعال کن",
        "شروع کن"

    ],



    "creation": [

        "بساز",
        "ایجاد کن",
        "طراحی کن",
        "درست کن"

    ],



    "memory": [

        "یادته",
        "ذخیره کن",
        "فراموش نکن",
        "به یاد داشته باش"

    ],



    "analysis": [

        "بررسی کن",
        "تحلیل کن",
        "مقایسه کن",
        "نظر بده"

    ]

}








def analyze_decision(text):


    text = text.lower()



    scores = {}



    for decision, patterns in DECISION_PATTERNS.items():


        score = 0



        for pattern in patterns:


            if pattern in text:

                score += 1



        scores[decision] = score





    selected = max(

        scores,

        key=scores.get

    )





    confidence = scores[selected]





    if confidence == 0:


        selected = "conversation"





    return {


        "decision": selected,


        "confidence": confidence,


        "all_scores": scores,


        "time":

        str(
            datetime.datetime.now()
        )

    }









def get_decision(text):


    return analyze_decision(
        text
    )








def get_decisions(text):


    result = analyze_decision(
        text
    )


    return result
