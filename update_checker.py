from github_update_source import get_latest_version
from version_compare import compare_versions


CURRENT_VERSION = "6.2"


def check_for_update():

    try:
        latest = get_latest_version()

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


    result = compare_versions(
        CURRENT_VERSION,
        latest
    )


    if result == "newer":

        return {
            "status": "update_available",
            "current": CURRENT_VERSION,
            "latest": latest
        }


    return {
        "status": "up_to_date",
        "current": CURRENT_VERSION,
        "latest": latest
    }



if __name__ == "__main__":

    print(
        check_for_update()
    )
