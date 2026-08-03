# =========================
# Saeed Planner
# =========================


def analyze_goal(text):

    goal_words = [

        "میخوام",
        "می‌خوام",
        "می خواهم",
        "هدفم",
        "شروع کنم",
        "بسازم",
        "یاد بگیرم",
        "برنامه",
        "کمک کن"

    ]


    for word in goal_words:

        if word in text:

            return {
                "goal": True,
                "text": text
            }


    return {
        "goal": False,
        "text": ""
    }



def create_plan(goal):

    return f"""

هدف شناسایی شده:

{goal}


روش پیشنهادی:

مرحله ۱:
مشخص کردن نتیجه نهایی


مرحله ۲:
تقسیم هدف به کارهای کوچک‌تر


مرحله ۳:
شروع با اولین قدم عملی


مرحله ۴:
بررسی نتیجه و اصلاح مسیر


مرحله ۵:
بهبود تدریجی


"""



def planning_context(text):


    result = analyze_goal(text)


    if result["goal"]:

        return create_plan(
            result["text"]
        )


    return ""
