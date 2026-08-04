# memory_manager.py
# Saeed AI v2.3
# Smart Memory Retrieval System


import json
import os




MEMORY_FILE = "saeed_smart_memory.json"







def load_memory():


    if not os.path.exists(MEMORY_FILE):

        return []



    with open(

        MEMORY_FILE,

        "r",

        encoding="utf-8"

    ) as file:


        return json.load(file)









def save_memory(data):


    with open(

        MEMORY_FILE,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            data,

            file,

            ensure_ascii=False,

            indent=4

        )









def add_memory(memory):


    data = load_memory()



    data.append(

        memory

    )



    save_memory(

        data

    )



    return memory







def search_memory(query):


    memories = load_memory()



    results = []



    words = query.split()



    for memory in memories:


        content = memory.get(

            "content",

            ""

        )



        score = 0



        for word in words:


            if word in content:


                score += 1





        if score > 0:


            memory["score"] = score


            results.append(

                memory

            )





    results.sort(

        key=lambda x: x.get(

            "importance",

            0

        ),

        reverse=True

    )



    return results







def get_best_memory(query):


    results = search_memory(

        query

    )



    if results:


        return results[0]



    return None
