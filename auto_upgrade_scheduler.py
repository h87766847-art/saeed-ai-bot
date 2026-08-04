import time
import datetime

from auto_upgrade_runner import run_auto_upgrade


CHECK_INTERVAL = 21600  # هر ۶ ساعت


def scheduler():

    print("Saeed Auto Upgrade Scheduler Started ✅")

    while True:

        try:
            print(
                "Checking updates:",
                datetime.datetime.now()
            )

            result = run_auto_upgrade()

            print(result)

        except Exception as e:

            print(
                "Upgrade Scheduler Error:",
                e
            )


        time.sleep(CHECK_INTERVAL)



if __name__ == "__main__":

    scheduler()
