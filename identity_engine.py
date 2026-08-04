# identity_engine.py
# Saeed Core v7.5
# Identity + Capability Connection


import json
import os
import datetime





IDENTITY_FILE = "saeed_identity.json"





try:

    from capability_manager import (
        add_capability,
        get_capabilities
    )

except Exception:

    add_capability = None
    get_capabilities = None








DEFAULT_IDENTITY = {


    "name":

    "Saeed",


    "version":

    "7.5",


    "role":

    "AI Core Assistant",


    "created":

    str(

        datetime.datetime.now()

    ),


    "personality":

    {


        "logical":

        True,


        "creative":

        True,


        "adaptive":

        True

    }

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


    data = load_identity()



    data[key] = value



    save_identity(

        data

    )


    return True







def get_identity(

        key=None

):


    data = load_identity()



    if key:


        return data.get(

            key

        )


    return data







def register_default_capabilities():


    if add_capability:


        capabilities = [


            (

                "memory",

                "Memory management system"

            ),


            (

                "learning",

                "Learning engine"

            ),


            (

                "upgrade",

                "Upgrade management"

            ),


            (

                "security",

                "Security protection"

            )


        ]



        for name, desc in capabilities:


            try:

                add_capability(

                    name,

                    desc

                )

            except Exception:

                pass



    return True







def identity_status():


    data = load_identity()



    return {


        "name":

        data["name"],


        "version":

        data["version"],


        "capabilities":

        get_capabilities()

        if get_capabilities

        else {},


        "status":

        "active"

    }







register_default_capabilities()
