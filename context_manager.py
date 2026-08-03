import json
import os
import datetime


FILE = "saeed_context.json"



DEFAULT_CONTEXT = {

    "main_topic": "",

    "sub_topic": "",

    "goal": "",

    "last_update": ""

}





def init_context():

    if not os.path.exists(FILE):

        save_context(
            DEFAULT_CONTEXT
        )





def save_context(data):

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





def get_context():

    try:

        with open(
            FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)


    except:

        init_context()

        return DEFAULT_CONTEXT





def update_context(
    topic,
    subtopic,
    goal
):

    data = {

        "main_topic": topic,

        "sub_topic": subtopic,

        "goal": goal,

        "last_update":
        str(datetime.datetime.now())

    }


    save_context(
        data
    )





def context_prompt():


    data = get_context()


    return f"""

موضوع فعلی گفتگو:

{data["main_topic"]}


زیرموضوع:

{data["sub_topic"]}


هدف:

{data["goal"]}

"""
