import datetime

try:
    from upgrade_controller import UpgradeController
except Exception:
    UpgradeController = None


class GithubUpgradeBridge:

    def __init__(self):
        self.controller = UpgradeController()


    def check_new_version(self, current, latest):

        print("Checking version...")

        if current == latest:
            return {
                "status": "up_to_date",
                "message": "Saeed is already updated"
            }


        return {
            "status": "new_version",
            "current": current,
            "latest": latest,
            "time": str(datetime.datetime.now())
        }



    def approve_upgrade(self):

        print(
            "Sending upgrade to safety check..."
        )

        return self.controller.prepare_upgrade()



if __name__ == "__main__":

    bridge = GithubUpgradeBridge()

    print(
        bridge.check_new_version(
            "1.0",
            "1.1"
        )
    )

    print(
        bridge.approve_upgrade()
    )
