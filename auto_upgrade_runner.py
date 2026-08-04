from update_checker import check_for_update
from upgrade_precheck import run_precheck
from rollback_manager import create_backup


def run_auto_upgrade():

    print("Saeed Auto Upgrade Started...")


    # 1 - Check update
    update = check_for_update()

    print(update)


    if update.get("status") != "update_available":

        return {
            "status": "no_update"
        }


    # 2 - Backup
    backup = create_backup(
        "main.py"
    )


    if not backup:

        return {
            "status": "backup_failed"
        }


    # 3 - Safety test
    safe = run_precheck()


    if not safe:

        return {
            "status": "blocked_by_test"
        }


    return {
        "status": "ready",
        "message": "Update passed all checks"
    }



if __name__ == "__main__":

    print(
        run_auto_upgrade()
    )
