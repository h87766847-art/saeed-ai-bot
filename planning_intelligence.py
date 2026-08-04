from agent_planner import (
    create_plan,
    get_active_plans
)



def generate_steps(goal):


    steps = []


    if "یادگیری" in goal:

        steps = [

            "مشخص کردن سطح فعلی",

            "ساخت برنامه روزانه",

            "تمرین مداوم",

            "بررسی پیشرفت"

        ]


    elif "پروژه" in goal:

        steps = [

            "تحلیل نیازمندی‌ها",

            "طراحی معماری",

            "ساخت نسخه اولیه",

            "تست و بهبود"

        ]


    else:

        steps = [

            "بررسی هدف",

            "تقسیم هدف به مراحل کوچک",

            "شروع اولین مرحله",

            "ارزیابی نتیجه"

        ]


    return steps






def create_goal_plan(goal):


    steps = generate_steps(
        goal
    )


    return create_plan(

        goal,

        steps

    )






def show_plans():

    plans = get_active_plans()


    result = ""


    for plan in plans:

        result += (

            "هدف: "

            +

            plan["goal"]

            +

            "\nمراحل:\n"

        )


        for step in plan["steps"]:

            result += (

                "- "

                +

                step

                +

                "\n"

            )


        result += "\n"



    return result
