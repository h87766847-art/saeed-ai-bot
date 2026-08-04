# event_engine.py
# Saeed Core
# Advanced Event Management System


import datetime
import uuid





EVENT_HANDLERS = {}

EVENT_HISTORY = {}







def register_event(

        event_name,

        handler

):


    if event_name not in EVENT_HANDLERS:


        EVENT_HANDLERS[event_name] = []



    EVENT_HANDLERS[event_name].append(

        handler

    )



    return True







def emit_event(

        event_name,

        data=None

):


    event_id = str(

        uuid.uuid4()

    )



    event = {


        "id":

        event_id,


        "name":

        event_name,


        "data":

        data,


        "time":

        str(

            datetime.datetime.now()

        )

    }



    EVENT_HISTORY[event_id] = event



    handlers = EVENT_HANDLERS.get(

        event_name,

        []

    )



    results = []



    for handler in handlers:


        try:


            result = handler(

                data

            )


            results.append(

                result

            )



        except Exception as e:


            results.append(

                str(e)

            )



    return {


        "event":

        event,


        "results":

        results

    }









def get_event_history(

        limit=50

):


    events = list(

        EVENT_HISTORY.values()

    )



    return events[-limit:]








def remove_event_handler(

        event_name,

        handler

):


    if event_name in EVENT_HANDLERS:


        if handler in EVENT_HANDLERS[event_name]:


            EVENT_HANDLERS[event_name].remove(

                handler

            )


            return True



    return False







def event_status():


    return {


        "events":

        len(EVENT_HISTORY),


        "types":

        len(EVENT_HANDLERS),


        "status":

        "online"

    }
