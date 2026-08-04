# message_upgrade_bridge.py
# Saeed Core v9.5
# Message Upgrade Bridge


from bot_upgrade_router import (
    process_upgrade_message
)





def check_upgrade_message(

    message_text

):


    result = process_upgrade_message(

        message_text

    )



    if result:


        return {


            "handled":

            True,


            "response":

            result

        }






    return {


        "handled":

        False,


        "response":

        None

    }
