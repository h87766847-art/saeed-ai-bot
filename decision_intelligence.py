# decision_intelligence.py
# Saeed AI v2.8
# Decision Making System


import json
import os
import datetime





DECISION_FILE = "saeed_decisions.json"








def load_decisions():


    if not os.path.exists(DECISION_FILE):

        return []



    with open(

        DECISION_FILE,

        "r",

        encoding="utf-8"

    ) as file:


        return json.load(file)









def save_decisions(data):


    with open(

        DECISION_FILE,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            data,

            file,

            ensure_ascii=False,

            indent=4

        )









def analyze_options(options):


    results = []



    for option in options:


        score = 0



        if "ساده" in option:

            score += 2



        if "سریع" in option:

            score += 2



        if "بهتر" in option:

            score += 3



        results.append(

            {

                "option": option,

                "score": score

            }

        )





    results.sort(

        key=lambda x: x["score"],

        reverse=True

    )



    return results







def create_decision(

    problem,

    options

):


    analysis = analyze_options(

        options

    )



    decision = {


        "problem": problem,


        "options": analysis,


        "recommended":

        analysis[0]["option"]

        if analysis

        else None,


        "time":

        str(datetime.datetime.now())

    }



    data = load_decisions()



    data.append(

        decision

    )



    save_decisions(

        data

    )



    return decision









def get_decisions():


    return load_decisions()
