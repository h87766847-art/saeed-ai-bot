import datetime

from goals import (
    init_goals,
    add_goal,
    get_goals
)



# ساخت جدول هدف‌ها

init_goals()



NOTES_FILE = "saeed_notes.txt"



# =========================
# زمان
# =========================

def get_time():

    now = datetime.datetime.now()

    return (
        "زمان فعلی: "
        +
        now.strftime("%Y-%m-%d %H:%M:%S")
    )



# =========================
# یادداشت
# =========================

def save_note(note):

    with open(
        NOTES_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            note + "\n"
        )


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



# =========================
# اهداف
# =========================

def save_goal(goal):

    return add_goal(
        goal
    )



def show_goals():

    goals = get_goals()


    if not goals:

        return "هنوز هدفی ثبت نشده."


    result = "هدف‌های حسین:\n"


    for title, status, progress in goals:

        result += (
            f"- {title} | "
            f"{status} | "
            f"{progress}%\n"
        )


    return result



# =========================
# انتخاب ابزار
# =========================

def use_tool(text):


    if "ساعت" in text or "زمان" in text:

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



    if "هدف من" in text or "هدفم" in text:

        goal = text.replace(
            "هدف من",
            ""
        )

        goal = goal.replace(
            "هدفم",
            ""
        )


        return save_goal(
            goal.strip()
        )



    if "هدف ها" in text or "هدف‌ها" in text:

        return show_goals()



    return None
