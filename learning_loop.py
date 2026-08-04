import json
import os
import datetime



FILE = "saeed_learning.json"





def load_learning():


    if not os.path.exists(FILE):

        return []


    with open(

        FILE,

        "r",

        encoding="utf-8"

    ) as f:

        return json.load(f)







def save_learning(data):


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







def add_experience(
    situation,
    result,
    feedback
):


    data = load_learning()



    experience = {


        "situation": situation,


        "result": result,


        "feedback": feedback,


        "time":

        str(datetime.datetime.now())


    }



    data.append(

        experience

    )



    save_learning(

        data

    )



    return experience







def get_experiences():


    return load_learning()
