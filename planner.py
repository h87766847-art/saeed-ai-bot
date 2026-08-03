def analyze_goal(text):

    goals = [
        "میخوام",
        "می‌خواهم",
        "هدفم",
        "بسازم",
        "یاد بگیرم",
        "شروع کنم"
    ]

    for goal in goals:

        if goal in text:

            return {
                "has_goal": True,
                "goal": text
            }


    return {
        "has_goal": False,
        "goal": None
    }



def create_plan(goal):

    return f"""
هدف شناسایی شد:

{goal}

برنامه پیشنهادی:

مرحله ۱:
درک دقیق هدف و نیازها

مرحله ۲:
تقسیم هدف به کارهای کوچک‌تر

مرحله ۳:
شروع با ساده‌ترین قدم عملی

مرحله ۴:
بررسی نتیجه و بهبود

"""



def planning_context(text):

    result = analyze_goal(text)


    if result["has_goal"]:

        return create_plan(
            result["goal"]
        )


    return ""
