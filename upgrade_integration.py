# upgrade_integration.py
# Saeed Core v8.4
# Upgrade Integration Layer


from upgrade_bootstrap import (
    initialize_upgrade_system
)


from upgrade_commands import (
    command_version,
    command_upgrade_check,
    command_upgrade_start,
    command_upgrade_status
)






def initialize_saeed_upgrade():


    try:


        result = initialize_upgrade_system()



        return {


            "upgrade_system":

            "ready",


            "result":

            result

        }





    except Exception as e:


        return {


            "upgrade_system":

            "error",


            "message":

            str(e)

        }









def handle_upgrade_command(

    command

):


    if command == "/version":


        return command_version()





    elif command == "/upgrade_check":


        return command_upgrade_check()





    elif command == "/upgrade_start":


        return command_upgrade_start()





    elif command == "/upgrade_status":


        return command_upgrade_status()





    else:


        return {


            "error":

            "unknown upgrade command"

        }
