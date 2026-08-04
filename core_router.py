# core_router.py
# Saeed Core v6.3
# Central Intelligence Router


from brain import process_brain


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





def analyze_request(text):


    memory = get_best_memory(

        text

    )


    context = get_context_information()



    plans = get_active_plans()



    decisions = get_decisions()





    return {

        "text": text,

        "memory": memory,

        "context": context,

        "plans": plans,

        "decisions": decisions

    }








def route_message(text):


    data = analyze_request(

        text

    )





    if text.startswith("/"):


        return {

            "type": "command",

            "data": text

        }






    if (

        "هدف" in text

        or

        "برنامه" in text

    ):


        return {

            "type": "planner",

            "data": data

        }






    if (

        "تصمیم" in text

        or

        "انتخاب" in text

    ):


        return {

            "type": "decision",

            "data": data

        }







    return {

        "type": "chat",

        "data": data

    }









def send_to_brain(text):


    routed_data = route_message(

        text

    )



    return process_brain(

        routed_data

    )
