# bot_upgrade_router.py
# Saeed Core v9.4
# Bot Upgrade Router


from telegram_upgrade_handler import (
    handle_upgrade_command,
    format_upgrade_response
)





UPGRADE_COMMANDS = [

    "/version",

    "/upgrade_check",

    "/upgrade_start",

    "/upgrade_status"

]







def is_upgrade_command(text):


    if not text:

        return False



    return text.strip() in UPGRADE_COMMANDS









def process_upgrade_message(text):


    if not is_upgrade_command(text):

        return None






    result = handle_upgrade_command(

        text.strip()

    )



    return format_upgrade_response(

        result

    )
