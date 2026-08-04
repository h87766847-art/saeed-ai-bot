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






def analyze_request(text):


    request_data = {


        "text": text,


        "router_version": ROUTER_VERSION

    }



    if get_context_information:

        try:

            request_data["context"] = get_context_information(text)

        except Exception:

            request_data["context"] = None





    if get_best_memory:

        try:

            request_data["memory"] = get_best_memory(text)

        except Exception:

            request_data["memory"] = None





    if get_active_plans:

        try:

            request_data["plans"] = get_active_plans()

        except Exception:

            request_data["plans"] = []





    if get_decisions:

        try:

            request_data["decisions"] = get_decisions(text)

        except Exception:

            request_data["decisions"] = None






    brain_response = process_brain(text)



    request_data["brain"] = brain_response



    return request_data







def route_message(text):


    return analyze_request(text)







def router_status():


    return {


        "name": "Saeed Router",


        "version": ROUTER_VERSION,


        "status": "online"

            }
