# config_manager.py
# Saeed Core
# Advanced Configuration Management System


import json
import os
import datetime





CONFIG_FILE = "saeed_config.json"







DEFAULT_CONFIG = {


    "name":

    "Saeed",


    "language":

    "fa",


    "version":

    "6.3",


    "learning":

    True,


    "memory":

    True,


    "auto_mode":

    True,


    "debug":

    False

}







def create_config():


    if not os.path.exists(

        CONFIG_FILE

    ):


        save_config(

            DEFAULT_CONFIG

        )





def save_config(

        config

):


    with open(

        CONFIG_FILE,

        "w",

        encoding="utf-8"

    ) as file:


        json.dump(

            config,

            file,

            ensure_ascii=False,

            indent=4

        )



    return True







def load_config():


    try:


        with open(

            CONFIG_FILE,

            "r",

            encoding="utf-8"

        ) as file:


            return json.load(

                file

            )



    except Exception:


        return DEFAULT_CONFIG







def update_config(

        key,

        value

):


    config = load_config()



    config[key] = value



    save_config(

        config

    )



    return True








def get_config(

        key,

        default=None

):


    config = load_config()



    return config.get(

        key,

        default

    )








def config_status():


    return {


        "file":

        CONFIG_FILE,


        "settings":

        load_config(),


        "time":

        str(

            datetime.datetime.now()

        )

    }







create_config()
