# tool_manager.py
# Saeed Core
# Advanced Tool Management System


import datetime
import traceback





TOOLS = {}





TOOL_LOG = []








def register_tool(

        name,

        function,

        description=""

):


    TOOLS[name] = {


        "function":

        function,


        "description":

        description,


        "created":

        str(

            datetime.datetime.now()

        )

    }



    return True







def remove_tool(

        name

):


    if name in TOOLS:


        del TOOLS[name]


        return True



    return False








def list_tools():


    result = []



    for name, data in TOOLS.items():


        result.append(

            {


            "name":

            name,


            "description":

            data["description"]


            }

        )



    return result








def execute_tool(

        name,

        *args,

        **kwargs

):


    try:


        if name not in TOOLS:


            return {


                "status":

                "error",


                "message":

                "Tool not found"

            }






        result = TOOLS[name]["function"](

            *args,

            **kwargs

        )





        TOOL_LOG.append(

            {


            "tool":

            name,


            "status":

            "success",


            "time":

            str(

                datetime.datetime.now()

            )

            }

        )





        return {


            "status":

            "success",


            "result":

            result

        }





    except Exception as e:



        TOOL_LOG.append(

            {


            "tool":

            name,


            "status":

            "failed",


            "error":

            str(e)

            }

        )




        return {


            "status":

            "error",


            "error":

            str(e),


            "trace":

            traceback.format_exc()

        }








def get_tool_logs():


    return TOOL_LOG
