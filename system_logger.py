# system_logger.py
# Saeed Core v7.6
# Central Logging System


import datetime
import os





LOG_FOLDER = "saeed_logs"

LOG_FILE = "system.log"







def init_logger():


    if not os.path.exists(

        LOG_FOLDER

    ):


        os.makedirs(

            LOG_FOLDER

        )








def write_log(

        level,

        message

):


    init_logger()



    path = os.path.join(

        LOG_FOLDER,

        LOG_FILE

    )



    record = {


        "time":

        str(

            datetime.datetime.now()

        ),


        "level":

        level,


        "message":

        message

    }



    with open(

        path,

        "a",

        encoding="utf-8"

    ) as file:


        file.write(

            str(record)

            +

            "\n"

        )



    return record







def info(

        message

):


    return write_log(

        "INFO",

        message

    )









def warning(

        message

):


    return write_log(

        "WARNING",

        message

    )









def error(

        message

):


    return write_log(

        "ERROR",

        message

    )









def get_logs():


    init_logger()



    path = os.path.join(

        LOG_FOLDER,

        LOG_FILE

    )



    if not os.path.exists(

        path

    ):


        return []



    with open(

        path,

        "r",

        encoding="utf-8"

    ) as file:


        return file.readlines()







def logger_status():


    return {


        "folder":

        LOG_FOLDER,


        "status":

        "active"

    }
