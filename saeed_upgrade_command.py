from github_upgrade_bridge import GithubUpgradeBridge


bridge = GithubUpgradeBridge()


def upgrade_command():

    print(
        "Saeed received upgrade request..."
    )


    approved = bridge.approve_upgrade()


    if approved:

        return {
            "status": "approved",
            "message": "Upgrade passed safety checks"
        }


    return {
        "status": "blocked",
        "message": "Upgrade stopped because test failed"
    }



if __name__ == "__main__":

    result = upgrade_command()

    print(result)
