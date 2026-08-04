import os
import shutil
import datetime


BACKUP_DIR = "saeed_backups"


def create_backup():

    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    name = datetime.datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    folder = os.path.join(
        BACKUP_DIR,
        name
    )

    os.makedirs(folder)

    files = [
        "main.py",
        "requirements.txt",
        "auto_upgrade_agent.py",
        "version_compare.py",
        "github_update_source.py",
        "saeed_memory.py"
    ]

    for file in files:
        if os.path.exists(file):
            shutil.copy(
                file,
                folder
            )

    return folder


def list_backups():

    if not os.path.exists(BACKUP_DIR):
        return []

    return os.listdir(BACKUP_DIR)


def rollback(backup_name):

    folder = os.path.join(
        BACKUP_DIR,
        backup_name
    )

    if not os.path.exists(folder):
        return False


    for file in os.listdir(folder):
        shutil.copy(
            os.path.join(folder,file),
            file
        )

    return True
