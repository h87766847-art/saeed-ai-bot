# upgrade_learning.py
# Saeed Core v11.1
# Learning From Upgrade History


from saeed_memory import (
    add_memory,
    search_memory
)

import datetime





LEARNING_LOG = []








def learn_from_upgrade(

    version,

    result,

    errors=None

):


    errors = errors or []



    memory_result = add_memory(

        "upgrade",

        "upgrade_" + version,

        {

            "success":

            result == "success",


            "errors":

            errors

        }

    )





    learning = {


        "version":

        version,


        "result":

        result,


        "errors":

        errors,


        "time":

        str(datetime.datetime.now()),


        "memory_saved":

        True

    }





    LEARNING_LOG.append(

        learning

    )



    return learning









def find_upgrade_experience(

    keyword

):


    return search_memory(

        keyword

    )









def learning_status():


    return {


        "learned_events":

        len(

            LEARNING_LOG

        ),


        "status":

        "active"

    }
