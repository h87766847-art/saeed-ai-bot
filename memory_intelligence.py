from long_term_memory import (
    init_long_memory,
    save_long_memory,
    get_important_memories
)



init_long_memory()





def calculate_importance(text):


    score = 1


    important_words = [

        "هدف",

        "پروژه",

        "میخواهم",

        "می‌خواهم",

        "همیشه",

        "دوست دارم",

        "برنامه",

        "زندگی",

        "کار"

    ]



    for word in important_words:


        if word in text:

            score += 1



    if len(text) > 100:

        score += 2



    if score > 10:

        score = 10



    return score






def analyze_memory(text):


    importance = calculate_importance(
        text
    )



    if importance >= 5:


        category = "important"



        save_long_memory(

            category,

            text,

            importance

        )


        return True



    return False






def get_memory_context():


    memories = get_important_memories()



    context = ""



    for category, content in memories:


        context += (

            content

            +

            "\n"

        )



    return context
