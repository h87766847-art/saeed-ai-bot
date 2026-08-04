import json
import os
import datetime



FILE = "saeed_evaluations.json"





def load_evaluations():


    if not os.path.exists(FILE):

        return []


    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)







def save_evaluations(data):


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







def evaluate(

    task,

    result,

    score

):


    data = load_evaluations()



    evaluation = {

        "task": task,

        "result": result,

        "score": score,

        "time":

        str(datetime.datetime.now())

    }



    data.append(

        evaluation

    )


    save_evaluations(

        data

    )


    return evaluation







def get_evaluations():


    return load_evaluations()
