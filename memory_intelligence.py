# memory_intelligence.py
# Saeed AI v2.2
# Smart Memory Analyzer


import datetime





def detect_memory_type(text):


    text = text.lower()



    if (
        "من" in text
        or
        "هستم" in text
        or
        "دارم" in text
    ):

        return "user"



    if (
        "پروژه" in text
        or
        "ساخت" in text
        or
        "برنامه" in text
    ):

        return "projects"



    if (
        "دوست دارم" in text
        or
        "علاقه" in text
        or
        "عاشق" in text
    ):

        return "preferences"



    if (
        "هدف" in text
        or
        "میخواهم" in text
        or
        "می‌خواهم" in text
    ):

        return "goals"



    return "general"








def calculate_importance(text):


    score = 1



    important_words = [

        "هدف",

        "پروژه",

        "علاقه",

        "دوست دارم",

        "میخواهم",

        "کار",

        "یادگیری",

        "تخصص"

    ]




    for word in important_words:


        if word in text:


            score += 1





    if len(text) > 50:


        score += 1





    if score > 10:


        score = 10





    return score









def analyze_memory(text):


    memory_type = detect_memory_type(

        text

    )



    importance = calculate_importance(

        text

    )




    return {


        "type": memory_type,


        "importance": importance,


        "content": text,


        "time":

        str(datetime.datetime.now())


    }
