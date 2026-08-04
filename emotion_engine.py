# emotion_engine.py
# Saeed Core
# Advanced Emotion Intelligence System


import datetime



EMOTIONS = {


    "happy": [

        "خوشحال",
        "عالی",
        "خوبه",
        "شاد",
        "مرسی"

    ],


    "sad": [

        "غمگین",
        "ناراحت",
        "بد",
        "تنها",
        "گریه"

    ],


    "angry": [

        "عصبانی",
        "حرص",
        "اعصاب",
        "خشم"

    ],


    "confused": [

        "نمی‌دونم",
        "گیج",
        "چرا",
        "مشکل"

    ],


    "excited": [

        "هیجان",
        "باحال",
        "خفن",
        "عالیه"

    ]

}






def detect_emotion(text):


    text = text.lower()



    scores = {}



    for emotion, words in EMOTIONS.items():


        score = 0



        for word in words:


            if word in text:

                score += 1



        scores[emotion] = score





    selected = max(

        scores,

        key=scores.get

    )





    if scores[selected] == 0:

        selected = "neutral"





    return {


        "emotion":

        selected,


        "confidence":

        scores.get(

            selected,

            0

        ),


        "all_scores":

        scores,


        "time":

        str(

            datetime.datetime.now()

        )

    }







def get_emotion_response(

        emotion

):


    responses = {


        "happy":

        "خوشحالم که حالت خوبه.",


        "sad":

        "متوجه شدم. سعی می‌کنم کمکت کنم.",


        "angry":

        "آرام‌تر بررسی کنیم تا بهترین راه پیدا شود.",


        "confused":

        "بیایید مرحله به مرحله بررسی کنیم.",


        "excited":

        "عالیه، ایده‌ات جالب به نظر می‌رسه.",


        "neutral":

        "در خدمتم."

    }



    return responses.get(

        emotion,

        responses["neutral"]

    )
