import datetime

from goals import (
    init_goals,
    add_goal,
    get_goals
)

from habits import (
    init_habits,
    add_habit,
    complete_habit,
    show_habits
)

from knowledge_base import (
    init_knowledge,
    add_knowledge,
    search_knowledge
)



init_goals()
init_habits()
init_knowledge()



NOTES_FILE = "saeed_notes.txt"



def get_time():

    now = datetime.datetime.now()

    return (
        "زمان فعلی: "
        +
        now.strftime("%Y-%m-%d %H:%M:%S")
    )



def save_note(note):

    with open(
        NOTES_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(note + "\n")


    return "یادداشت ذخیره شد."



def read_notes():

    try:

        with open(
            NOTES_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    except:

        return "یادداشتی وجود ندارد."




# =====================
# Knowledge
# =====================

def save_knowledge(text):

    return add_knowledge(
        "دانش حسین",
        text
    )



def find_knowledge(query):

    results = search_knowledge(
        query
    )


    if not results:

        return "چیزی در دانش ذخیره نشده."



    answer = "اطلاعات پیدا شده:\n"



    for title, content in results:

        answer += (
            "\n"
            +
            content
        )


    return answer





# =====================
# Tool Router
# =====================

def use_tool(text):


    if "زمان" in text or "ساعت" in text:

        return get_time()



    if "یادداشت کن" in text:

        note = text.replace(
            "یادداشت کن",
            ""
        )

        return save_note(
            note.strip()
        )



    if "یادداشت ها" in text:

        return read_notes()




    if "دانش ذخیره کن" in text:

        data = text.replace(
            "دانش ذخیره کن",
            ""
        )


        return save_knowledge(
            data.strip()
        )



    if "جستجو دانش" in text:

        query = text.replace(
            "جستجو دانش",
            ""
        )


        return find_knowledge(
            query.strip()
        )



    return None
