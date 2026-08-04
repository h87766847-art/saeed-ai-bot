# upgrade_commands.py
# Saeed Core v8.3
# Telegram Upgrade Control


from version_manager import (
    current_version
)


from auto_upgrade_agent import (
    check_upgrade_status,
    start_auto_upgrade
)


from upgrade_bootstrap import (
    get_boot_status
)






def command_version():


    return {


        "version":

        current_version(),


        "system":

        "Saeed Core"

    }









def command_upgrade_check():


    return check_upgrade_status()







def command_upgrade_start():


    return start_auto_upgrade()







def command_upgrade_status():


    return {


        "bootstrap":

        get_boot_status(),


        "version":

        current_version()

    }
