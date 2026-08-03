import json
import os



FILE = "memory_categories.json"



DEFAULT_MEMORY = {

    "user": [],

    "projects": [],

    "knowledge": [],

    "preferences": [],

    "goals": []

}





def init_memory_manager():

    if not os.path.exists(FILE):

        save_memory(DEFAULT_MEMORY)





def save_memory(data):

    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )





def load_memory():

    try:

        with open(
            FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    except:

        init_memory_manager()

        return DEFAULT_MEMORY





def add_memory(category, text):

    memory = load_memory()


    if category in memory:

        memory[category].append(text)


    save_memory(memory)





def get_memory(category):

    memory = load_memory()


    return memory.get(
        category,
        []
    )
