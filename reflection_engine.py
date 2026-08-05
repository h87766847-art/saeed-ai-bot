import json
import os
import datetime



FILE = "saeed_reflections.json"





def load_reflections():


    if not os.path.exists(FILE):

        return []


    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)







def save_reflections(data):


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







def create_reflection(

    task,

    success,

    improvements

):


    data = load_reflections()



    reflection = {


        "task": task,


        "success": success,


        "improvements": improvements,


        "time":

        str(datetime.datetime.now())


    }



    data.append(

        reflection

    )


    save_reflections(

        data

    )



    return reflection







def get_reflections():


    return load_reflections()
