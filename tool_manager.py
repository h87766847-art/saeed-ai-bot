# tool_manager.py
# Saeed AI v2.9
# Tool Execution System


import json
import os
import datetime





TOOL_FILE = "saeed_tools_log.json"








def load_logs():


    if not os.path.exists(TOOL_FILE):

        return []



    with open(

        TOOL_FILE,

        "r",

        encoding="utf-8"

    ) as file:


        return json.load(file)









def save_logs(data):


    with open(

        TOOL_FILE,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            data,

            file,

            ensure_ascii=False,

            indent=4

        )









def register_action(

    action,

    result

):


    logs = load_logs()



    record = {


        "action": action,


        "result": result,


        "time":

        str(datetime.datetime.now())

    }




    logs.append(

        record

    )



    save_logs(

        logs

    )



    return record







def available_tools():


    return [

        "memory",

        "planner",

        "decision",

        "profile"

    ]









def execute_tool(

    tool_name,

    data

):


    result = ""



    if tool_name == "memory":


        result = (

            "دسترسی به حافظه انجام شد"

        )





    elif tool_name == "planner":


        result = (

            "برنامه‌ریزی انجام شد"

        )





    elif tool_name == "decision":


        result = (

            "تحلیل تصمیم انجام شد"

        )





    elif tool_name == "profile":


        result = (

            "پروفایل کاربر بررسی شد"

        )





    else:


        result = (

            "ابزار ناشناخته است"

        )





    register_action(

        tool_name,

        result

    )



    return result
