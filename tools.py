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


init_goals()
init_habits()


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



# =====================
# Goals
# =====================

def save_goal(goal):

    return add_goal(goal)



def show_goal_list():

    goals = get_goals()


    if not goals:

        return "هدف ثبت نشده."


    result = "هدف‌های حسین:\n"


    for title,status,progress in goals:

        result += (
            f"- {title} | "
            f"{progress}%\n"
        )


    return result



# =====================
# Habits
# =====================

def save_habit(habit):

    return add_habit(
        habit
    )



def complete_task(task):

    return complete_habit(
        task
    )



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



    if "هدفم" in text or "هدف من" in text:

        goal = text.replace(
            "هدفم",
            ""
        )

        goal = goal.replace(
            "هدف من",
            ""
        )


        return save_goal(
            goal.strip()
        )



    if "هدف ها" in text or "هدف‌ها" in text:

        return show_goal_list()



    if "ماموریت" in text or "کار امروز" in text:

        habit = text.replace(
            "ماموریت",
            ""
        )

        habit = habit.replace(
            "کار امروز",
            ""
        )


        return save_habit(
            habit.strip()
        )



    if "انجام شد" in text:

        task = text.replace(
            "انجام شد",
            ""
        )


        return complete_task(
            task.strip()
        )



    if "ماموریت ها" in text or "ماموریت‌ها" in text:

        return show_habits()



    return None
