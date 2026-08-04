# memory_optimizer.py
# Saeed Core
# Advanced Memory Optimization System


import datetime





def calculate_memory_value(

        importance,

        access_count,

        age_factor=1

):


    value = (

        importance * 5

    ) + (

        access_count * 2

    ) - age_factor



    return max(

        value,

        0

    )









def rank_memories(

        memories

):


    ranked = []



    for memory in memories:


        try:


            value = calculate_memory_value(

                memory.get(

                    "importance",

                    1

                ),

                memory.get(

                    "accessed",

                    0

                )

            )



            ranked.append(

                {


                    "memory":

                    memory,


                    "value":

                    value

                }

            )



        except Exception:


            continue






    ranked.sort(

        key=lambda x: x["value"],

        reverse=True

    )



    return ranked







def select_important_memories(

        memories,

        limit=10

):


    ranked = rank_memories(

        memories

    )



    return ranked[:limit]








def memory_health(

        memories

):


    total = len(

        memories

    )



    important = 0



    for memory in memories:


        if memory.get(

            "importance",

            0

        ) >= 5:


            important += 1





    return {


        "total":

        total,


        "important":

        important,


        "health":

        "good" if total > 0 else "empty",


        "checked":

        str(

            datetime.datetime.now()

        )

    }
