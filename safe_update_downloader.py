import os
import shutil
import datetime


UPDATE_FOLDER = "saeed_updates"


def prepare_update_folder():

    if not os.path.exists(UPDATE_FOLDER):
        os.makedirs(UPDATE_FOLDER)



def save_update_file(source_file):

    prepare_update_folder()

    if not os.path.exists(source_file):
        return False


    name = datetime.datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    destination = os.path.join(
        UPDATE_FOLDER,
        name + "_" + source_file
    )

    shutil.copy(
        source_file,
        destination
    )

    return destination



def update_status():

    if not os.path.exists(UPDATE_FOLDER):
        return []

    return os.listdir(UPDATE_FOLDER)



if __name__ == "__main__":

    prepare_update_folder()

    print(
        "Update storage ready ✅"
    )
