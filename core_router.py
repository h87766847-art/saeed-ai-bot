from tool_router import check_tools

from decision_router import check_decision

from goal_router import check_goal_request





def route_message(text):


    # ابزارها

    tool = check_tools(
        text
    )


    if tool["used"]:

        return {

            "type":"tool",

            "data":tool["result"]

        }





    # تصمیم گیری

    decision = check_decision(
        text
    )


    if decision["used"]:

        return {

            "type":"decision",

            "data":decision["prompt"]

        }






    # هدف و برنامه

    goal = check_goal_request(
        text
    )


    if goal["used"]:

        return {

            "type":"goal",

            "data":goal["data"]

        }






    # چت معمولی

    return {

        "type":"chat",

        "data":None

    }
