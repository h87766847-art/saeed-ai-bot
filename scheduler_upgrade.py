import datetime


class UpgradeScheduler:

    def __init__(self):
        self.status = "ready"
        self.last_check = None


    def check_schedule(self, schedule_result):

        self.last_check = datetime.datetime.now()

        if not schedule_result:
            return False


        decision = schedule_result.get(
            "decision"
        )


        return decision in [
            "upgrade_now",
            "scheduled"
        ]



    def get_status(self):

        return {
            "system": "Saeed",
            "scheduler": self.status,
            "last_check": str(
                self.last_check
            )
        }



def run_scheduler_test():

    scheduler = UpgradeScheduler()

    test_result = {
        "decision": "scheduled"
    }


    return scheduler.check_schedule(
        test_result
    )



if __name__ == "__main__":

    print(
        run_scheduler_test()
    )
