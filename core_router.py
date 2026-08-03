from tool_router import check_tools
from decision_router import check_decision



def route_message(text):


    # بررسی ابزارها

    tool = check_tools(text)


    if tool["used"]:

        return {

            "type": "tool",

            "data": tool["result"]

        }



    # بررسی تصمیم

    decision = check_decision(text)


    if decision["used"]:

        return {

            "type": "decision",

            "data": decision["prompt"]

        }



    return {

        "type": "chat",

        "data": None

    }
