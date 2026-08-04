# user_profile.py
# Saeed AI v2.6
# User Personality & Profile System


import json
import os
import datetime





PROFILE_FILE = "saeed_user_profile.json"








def load_profile():


    if not os.path.exists(PROFILE_FILE):

        return {

            "name": "",

            "interests": [],

            "projects": [],

            "goals": [],

            "preferences": [],

            "created":

            str(datetime.datetime.now())

        }




    with open(

        PROFILE_FILE,

        "r",

        encoding="utf-8"

    ) as file:


        return json.load(file)









def save_profile(profile):


    with open(

        PROFILE_FILE,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            profile,

            file,

            ensure_ascii=False,

            indent=4

        )









def update_profile(

    category,

    value

):


    profile = load_profile()



    if category in profile:


        if value not in profile[category]:


            profile[category].append(

                value

            )



    save_profile(

        profile

    )



    return profile







def get_profile():


    return load_profile()









def detect_profile_data(text):


    text = text.lower()



    updates = []





    if "پروژه" in text:


        updates.append(

            (

                "projects",

                text

            )

        )





    if (

        "علاقه" in text

        or

        "دوست دارم" in text

        or

        "عاشق" in text

    ):


        updates.append(

            (

                "interests",

                text

            )

        )





    if (

        "هدف" in text

        or

        "میخواهم" in text

    ):


        updates.append(

            (

                "goals",

                text

            )

        )





    return updates
