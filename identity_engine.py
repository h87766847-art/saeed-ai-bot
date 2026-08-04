# identity_engine.py
# Saeed Core
# Advanced Identity Management System


import datetime
import json
import os





IDENTITY_FILE = "saeed_identity.json"







DEFAULT_IDENTITY = {


    "name":

    "Saeed",


    "role":

    "AI Assistant",


    "personality":

    {


        "helpful":

        True,


        "creative":

        True,


        "logical":

        True,


        "patient":

        True

    },


    "communication":

    {


        "language":

        "fa",


        "style":

        "friendly"

    },


    "created":

    None

}







def save_identity(

        data

):


    with open(

        IDENTITY_FILE,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            data,

            file,

            ensure_ascii=False,

            indent=4

        )







def load_identity():


    if not os.path.exists(

        IDENTITY_FILE

    ):


        save_identity(

            DEFAULT_IDENTITY

        )



    with open(

        IDENTITY_FILE,

        "r",

        encoding="utf-8"

    ) as file:


        return json.load(

            file

        )









def update_identity(

        key,

        value

):


    identity = load_identity()



    identity[key] = value



    save_identity(

        identity

    )



    return True







def get_identity(

        key=None

):


    identity = load_identity()



    if key:


        return identity.get(

            key

        )



    return identity







def personality_report():


    identity = load_identity()



    return {


        "name":

        identity["name"],


        "role":

        identity["role"],


        "personality":

        identity["personality"],


        "status":

        "active",


        "time":

        str(

            datetime.datetime.now()

        )

    }








load_identity()
