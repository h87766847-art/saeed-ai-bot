# upgrade_commands.py
# Saeed Core v9.9
# Upgrade Command Controller



from version_manager import (
    current_version
)



from auto_upgrade_agent import (
    check_upgrade_status
)



from safe_upgrade_commands import (
    command_safe_upgrade_start,
    command_safe_upgrade_status
)








def command_version():


    return {


        "system":

        "Saeed Core",


        "version":

        current_version()

    }









def command_upgrade_check():


    return check_upgrade_status()









def command_upgrade_start():


    return command_safe_upgrade_start()









def command_upgrade_status():


    return command_safe_upgrade_status()
