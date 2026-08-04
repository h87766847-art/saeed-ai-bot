# memory_intelligence.py
# Saeed AI v2.4
# Advanced Memory Scoring System


import datetime






def create_memory_record(

    content,

    memory_type,

    importance

):


    return {

        "content": content,

        "type": memory_type,

        "importance": importance,

        "created":

        str(datetime.datetime.now()),

        "access_count": 0

    }








def increase_memory_usage(memory):


    memory["access_count"] = (

        memory.get(

            "access_count",

            0

        )

        +

        1

    )


    return memory









def calculate_memory_score(memory):


    importance = memory.get(

        "importance",

        1

    )


    usage = memory.get(

        "access_count",

        0

    )



    score = (

        importance * 10

    ) + usage



    return score









def rank_memories(memories):


    for memory in memories:


        memory["score"] = calculate_memory_score(

            memory

        )



    memories.sort(

        key=lambda x: x["score"],

        reverse=True

    )



    return memories









def get_best_memories(

    memories,

    limit=5

):


    ranked = rank_memories(

        memories

    )



    return ranked[:limit]
