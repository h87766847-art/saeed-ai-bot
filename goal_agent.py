from goals import get_goals
from habits import show_habits



def analyze_goals():


    goals = get_goals()


    habits = show_habits()



    result = """

تحلیل وضعیت حسین:

"""


    if goals:

        result += "\nهدف‌های فعلی:\n"


        for goal in goals:

            result += (
                "- "
                +
                goal[0]
                +
                "\n"
            )


    else:

        result += "\nهدف فعالی ثبت نشده.\n"




    result += """

ماموریت‌های فعلی:

"""


    result += habits



    result += """

پیشنهاد:

- یک قدم کوچک مشخص کن.
- پیشرفت را ثبت کن.
- به صورت مداوم ادامه بده.

"""



    return result
