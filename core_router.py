# core_router.py
# Saeed Core
# Advanced Central Intelligence Router


from memory_manager import (
    get_best_memory
)


from context_intelligence import (
    get_context_information
)


from planner_intelligence import (
    get_active_plans
)


from decision_intelligence import (
    get_decisions
)


import datetime





def safe_call(function, default=None, *args):

    try:

        return function(*args)

    except Exception:

        return default







def analyze_request(text):


    context = safe_call(
        get_context_information,
        {},
        text
    )



    memories = safe_call(
        get_best_memory,
        [],
        text
    )



    plans = safe_call(
        get_active_plans,
        [],
    )



    decisions = safe_call(
        get_decisions,
        [],
        text
    )




    route = {

        "input": text,


        "context": context,


        "memory": memories,


        "plans": plans,


        "decisions": decisions,



        "route_time":
        str(
            datetime.datetime.now()
        )

    }



    return route







def choose_path(route):


    decision = route.get(
        "decisions",
        {}
    )



    if decision:

        return "decision"



    if route.get(
        "memory"
    ):

        return "memory"



    if route.get(
        "plans"
    ):

        return "planning"



    return "conversation"







def build_context(text):


    route = analyze_request(
        text
    )



    route["selected_path"] = choose_path(
        route
    )



    return route
