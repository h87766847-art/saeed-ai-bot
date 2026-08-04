# saeed_memory.py
# Saeed Core v11.0
# Memory & Learning System


import json
import os
import datetime





MEMORY_FILE = "saeed_memory.json"







def load_memory():


    if not os.path.exists(

        MEMORY_FILE

    ):


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









def add_memory(

    category,

    event,

    result

):


    memory = load_memory()



    item = {


        "category":

        category,


        "event":

        event,


        "result":

        result,


        "time":

        str(datetime.datetime.now())

    }



    memory.append(

        item

    )



    save_memory(

        memory

    )



    return item









def search_memory(

    keyword

):


    memory = load_memory()



    results = []



    for item in memory:


        text = (

            item["category"]

            +

            " "

            +

            item["event"]

            +

            " "

            +

            item["result"]

        )



        if keyword.lower() in text.lower():


            results.append(

                item

            )



    return results









def memory_status():


    return {


        "memories":

        len(

            load_memory()

        ),


        "status":

        "active"

  }
