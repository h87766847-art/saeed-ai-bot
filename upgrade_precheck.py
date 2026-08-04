import os
import py_compile


def check_files():

    errors = []

    for file in os.listdir("."):

        if file.endswith(".py"):

            try:
                py_compile.compile(
                    file,
                    doraise=True
                )

            except Exception as e:

                errors.append({
                    "file": file,
                    "error": str(e)
                })

    return errors



def run_precheck():

    print("Saeed Upgrade Precheck Started...")

    errors = check_files()


    if errors:

        print("❌ Upgrade blocked")

        for error in errors:
            print(error)

        return False


    print("✅ Upgrade precheck passed")

    return True



if __name__ == "__main__":

    run_precheck()
