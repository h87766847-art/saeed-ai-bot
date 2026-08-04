# decision_intelligence.py
# Saeed Core v6.6
# Decision Intelligence System


DECISION_TYPES = {


    "question": [

        "چی",
        "چرا",
        "چطور",
        "چگونه",
        "آیا"

    ],


    "request": [

        "بساز",
        "انجام بده",
        "کمک کن",
        "ایجاد کن"

    ],


    "memory": [

        "یادته",
        "به یاد داشته باش",
        "ذخیره کن",
        "یادت بمونه"

    ],


    "command": [

        "شروع",
        "برو",
        "اجرا",
        "فعال کن"

    ]

}






def analyze_decision(text):


    text = text.lower()



    scores = {}



    for decision, words in DECISION_TYPES.items():


        score = 0



        for word in words:


            if word in text:

                score += 1



        scores[decision] = score





    best = max(
        scores,
        key=scores.get
    )




    if scores[best] == 0:

        best = "conversation"




    return {


        "type": best,


        "scores": scores,


        "confidence": scores.get(
            best,
            0
        )

    }







def get_decision(text):


    return analyze_decision(
        text
    )
