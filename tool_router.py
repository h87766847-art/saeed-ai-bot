from tools import use_tool



def check_tools(user_message):

    result = use_tool(
        user_message
    )


    if result:

        return {
            "used": True,
            "result": result
        }


    return {
        "used": False,
        "result": None
    }
