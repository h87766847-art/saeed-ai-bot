from tool_router import check_tools

from decision_router import check_decision

from goal_router import check_goal_request

from decision_intelligence import (
    detect_decision_request,
    create_decision_analysis
)




def route_message(text):


    # ابزارها

    tool = check_tools(text)


    if tool["used"]:

        return {

            "type": "tool",

            "data": tool["result"]

        }





    # تصمیم‌گیری قدیمی

    decision = check_decision(text)


    if decision["used"]:

        return {

            "type": "decision",

            "data": decision["prompt"]

        }





    # تصمیم‌گیری هوشمند

    if detect_decision_request(text):


        return {

            "type": "decision_analysis",

            "data": create_decision_analysis(text)

        }





    # هدف‌ها

    goal = check_goal_request(text)


    if goal["used"]:

        return {

            "type": "goal",

            "data": goal["data"]

        }





    return {

        "type": "chat",

        "data": None

    }
