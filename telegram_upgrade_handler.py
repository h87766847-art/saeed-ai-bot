# telegram_upgrade_handler.py
# Saeed Core v9.3
# Telegram Upgrade Command Handler


from upgrade_commands import (
    command_version,
    command_upgrade_check,
    command_upgrade_start,
    command_upgrade_status
)





def handle_upgrade_command(command):


    commands = {


        "/version":

        command_version,


        "/upgrade_check":

        command_upgrade_check,


        "/upgrade_start":

        command_upgrade_start,


        "/upgrade_status":

        command_upgrade_status

    }





    if command in commands:


        return commands[command]()




    return {


        "status":

        "unknown_command",


        "message":

        "فرمان ارتقا شناخته نشد"

    }









def format_upgrade_response(data):


    if isinstance(data, dict):


        text = ""



        for key, value in data.items():


            text += f"{key}: {value}\n"




        return text




    return str(data)
