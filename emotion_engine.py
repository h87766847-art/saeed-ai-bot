# emotion_engine.py
# Saeed Core v6.5
# Emotion Detection Engine


EMOTION_WORDS = {

    "happy": [
        "خوشحالم",
        "عالی",
        "خوبه",
        "😂",
        "😁"
    ],

    "sad": [
        "ناراحتم",
        "غمگین",
        "تنها",
        "بد",
        "😢"
    ],

    "angry": [
        "عصبانی",
        "حرصم",
        "اعصابم",
        "خشم"
    ],

    "confused": [
        "نمی‌فهمم",
        "گیج",
        "چرا",
        "چطور"
    ]

}





def detect_emotion(text):

    text = text.lower()


    scores = {}


    for emotion, words in EMOTION_WORDS.items():

        score = 0


        for word in words:

            if word in text:

                score += 1


        scores[emotion] = score



    best_emotion = max(
        scores,
        key=scores.get
    )


    if scores[best_emotion] == 0:

        best_emotion = "neutral"



    return {

        "emotion": best_emotion,

        "scores": scores

    }





def get_emotion_response(emotion):


    responses = {

        "happy":
        "خوبه که حالت خوبه 😊",


        "sad":
        "می‌فهمم، اگر خواستی درباره‌اش صحبت کنیم.",


        "angry":
        "به نظر میاد ناراحتی، بگو ببینم چه شده.",


        "confused":
        "بیا مرحله به مرحله بررسی کنیم.",


        "neutral":
        "باشه، ادامه بده."

    }


    return responses.get(
        emotion,
        "باشه."
)
