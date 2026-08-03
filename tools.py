import datetime


# =========================
# ابزار زمان
# =========================

def get_time():

    now = datetime.datetime.now()

    return (
        "زمان فعلی: "
        +
        now.strftime("%Y-%m-%d %H:%M:%S")
    )



# =========================
# ابزار یادداشت ساده
# =========================

NOTES_FILE = "saeed_notes.txt"



def save_note(note):

    with open(
        NOTES_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            note + "\n"
        )


    return "یادداشت ذخیره شد."



def read_notes():

    try:

        with open(
            NOTES_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()


    except:

        return "هنوز یادداشتی وجود ندارد."



# =========================
# تشخیص ابزار
# =========================

def use_tool(text):


    if "ساعت" in text or "زمان" in text:

        return get_time()



    if "یادداشت کن" in text:

        note = text.replace(
            "یادداشت کن",
            ""
        )

        return save_note(
            note.strip()
        )



    if "یادداشت ها" in text:

        return read_notes()



    return None
