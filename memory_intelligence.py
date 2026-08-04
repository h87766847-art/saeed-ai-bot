# memory_intelligence.py
# Saeed Core
# Advanced Memory Intelligence System


import re
import datetime





IMPORTANT_PATTERNS = {


    "identity": [

        r"اسم من (.+)",
        r"نام من (.+)",
        r"من (.+) هستم"

    ],



    "age": [

        r"(\d+) ساله هستم",
        r"سن من (\d+)"

    ],



    "interest": [

        r"علاقه دارم به (.+)",
        r"دوست دارم (.+)"

    ],



    "goal": [

        r"هدف من (.+)",
        r"میخوام (.+)"

    ]

}







def analyze_memory(text):


    score = 0

    found = []



    important_words = [

        "اسم",
        "نام",
        "سن",
        "علاقه",
        "هدف",
        "دوست دارم",
        "یاد بگیر",
        "یاد داشته باش"

    ]



    for word in important_words:


        if word in text:


            score += 1

            found.append(
                word
            )




    return {


        "important":

        score > 0,


        "importance_score":

        score,


        "keywords":

        found,


        "time":

        str(
            datetime.datetime.now()
        )

    }









def extract_information(text):


    information = {}



    for category, patterns in IMPORTANT_PATTERNS.items():


        for pattern in patterns:


            result = re.search(

                pattern,

                text

            )



            if result:


                information[category] = result.group(1).strip()


                break



    return information







def calculate_memory_priority(data):


    priority = 1



    if data.get(
        "important"
    ):

        priority += 3




    priority += data.get(

        "importance_score",

        0

    )



    return priority
