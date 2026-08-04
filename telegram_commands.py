from telegram_upgrade_hook import handle_upgrade_command


def process_command(command):

    if command == "/upgrade_check":

        return handle_upgrade_command()

    return None
