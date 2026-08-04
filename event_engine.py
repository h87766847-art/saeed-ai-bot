# event_engine.py
# Saeed Core v7.5
# Central Event System


import datetime
import uuid





EVENTS = {}








def emit_event(

        name,

        data=None

):


    event_id = str(

        uuid.uuid4()

    )



    EVENTS[event_id] = {


        "id":

        event_id,


        "name":

        name,


        "data":

        data,


        "time":

        str(

            datetime.datetime.now()

        )

    }



    return EVENTS[event_id]









def get_events(

        name=None

):


    if name:


        return [

            event

            for event in EVENTS.values()

            if event["name"] == name

        ]





    return list(

        EVENTS.values()

    )









def last_events(

        count=10

):


    events = list(

        EVENTS.values()

    )



    return events[-count:]









def clear_events():


    EVENTS.clear()



    return True







def event_status():


    return {


        "total":

        len(

            EVENTS

        ),


        "status":

        "active"

    }
