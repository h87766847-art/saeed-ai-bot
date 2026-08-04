# analytics_engine.py
# Saeed Core
# Advanced Analytics Engine


import datetime
import json





EVENTS = []






def record_event(

        event_type,

        data=None

):


    if data is None:

        data = {}



    event = {


        "type":

        event_type,


        "data":

        data,


        "time":

        str(

            datetime.datetime.now()

        )

    }



    EVENTS.append(

        event

    )



    return True







def get_events(

        limit=50

):


    return EVENTS[-limit:]








def count_events(

        event_type=None

):


    if event_type is None:


        return len(EVENTS)





    count = 0



    for event in EVENTS:


        if event["type"] == event_type:


            count += 1




    return count







def analyze_activity():


    types = {}



    for event in EVENTS:


        name = event["type"]



        if name not in types:


            types[name] = 0



        types[name] += 1





    return {


        "total_events":

        len(EVENTS),


        "event_types":

        types,


        "status":

        "active",


        "time":

        str(

            datetime.datetime.now()

        )

    }








def export_analytics():


    return json.dumps(

        analyze_activity(),

        ensure_ascii=False,

        indent=2

    )








def clear_analytics():


    global EVENTS


    EVENTS = []


    return True
