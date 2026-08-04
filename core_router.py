# core_router.py
# Saeed Core v7.0
# Central Intelligence Router


from brain import process_brain





try:

    from memory_manager import get_best_memory

except Exception:

    get_best_memory = None





try:

    from context_intelligence import get_context_information

except Exception:

    get_context_information = None





try:

    from planner_intelligence import get_active_plans

except Exception:

    get_active_plans = None





try:

    from decision_intelligence import get_decisions

except Exception:

    get_decisions = None






ROUTER_VERSION = "7.0"









def analyze_request(

        text

):


    result = {


        "input":

        text,


        "router":

        ROUTER_VERSION

    }





    if get_context_information:


        try:

            result["context"] = get_context_information(

                text

            )

        except Exception:

            result["context"] = None







    if get_best_memory:


        try:

            result["memory"] = get_best_memory(

                text

            )

        except Exception:

            result["memory"] = []







    if get_active_plans:


        try:

            result["plans"] = get_active_plans()

        except Exception:

            result["plans"] = []







    if get_decisions:


        try:

            result["decisions"] = get_decisions(

                text

            )

        except Exception:

            result["decisions"] = []







    try:


        result["brain"] = process_brain(

            text

        )


    except Exception as e:


        result["brain"] = {


            "status":

            "error",


            "message":

            str(e)

        }






    return result







def route_message(

        text

):


    return analyze_request(

        text

    )








def router_status():


    return {


        "name":

        "Saeed Router",


        "version":

        ROUTER_VERSION,


        "status":

        "online"

    }
