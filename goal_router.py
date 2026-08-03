from goal_agent import analyze_goals



def check_goal_request(text):


    keywords = [

        "هدف",

        "برنامه",

        "پیشرفت",

        "چطور بهتر",

        "مسیر",

        "کمکم کن",

        "برنامه ریزی"

    ]



    for word in keywords:


        if word in text:


            return {

                "used": True,

                "data": analyze_goals()

            }



    return {

        "used": False,

        "data": None

    }
