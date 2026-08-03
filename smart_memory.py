from memory import save_memory


def calculate_importance(text):

    score = 0


    important_words = [

        "هدف",
        "پروژه",
        "اسم",
        "علاقه",
        "کار",
        "میخوام",
        "می‌خوام",
        "برنامه"

    ]


    for word in important_words:

        if word in text:

            score += 1



    return score



def smart_remember(text):

    importance = calculate_importance(
        text
    )


    if importance >= 2:

        save_memory(
            "important",
            text
        )

        return True


    return False
