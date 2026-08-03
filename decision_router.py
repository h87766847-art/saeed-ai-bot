from decision_engine import analyze_decision



def check_decision(text):

    keywords = [

        "کدام بهتر",
        "کدوم بهتر",
        "انتخاب",
        "بین",
        "تصمیم",
        "نظر تو",
        "مقایسه"

    ]


    for word in keywords:

        if word in text:

            return {

                "used": True,

                "prompt":
                    analyze_decision(text)

            }


    return {

        "used": False,

        "prompt": None

    }
