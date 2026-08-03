from memory import (
    save_memory,
    get_memories,
    save_message,
    get_recent_messages,
    save_profile,
    get_profile
)



# =========================
# تشخیص اطلاعات مهم
# =========================

def remember_important_information(text):

    important_patterns = [

        "اسم من",
        "من حسین",
        "علاقه دارم",
        "دوست دارم",
        "هدفم",
        "میخوام",
        "می‌خوام",
        "می خواهم",
        "کار من",
        "پروژه من"

    ]


    for pattern in important_patterns:

        if pattern in text:


            save_memory(

                "important",

                text

            )


            return True



    return False



# =========================
# ساخت حافظه برای AI
# =========================

def build_memory_context():


    memories = get_memories()

    profile = get_profile()


    result = ""



    if profile:

        result += "\nپروفایل حسین:\n"


        for key, value in profile:

            result += (
                f"{key}: {value}\n"
            )



    if memories:


        result += "\nخاطرات مهم:\n"


        for category, content in memories:


            result += (
                "- "
                +
                content
                +
                "\n"
            )


    if not result:

        result = (
            "هنوز اطلاعات مهمی ذخیره نشده."
        )


    return result



# =========================
# ذخیره گفتگو
# =========================

def save_conversation(
    role,
    text
):

    save_message(

        role,

        text

    )



# =========================
# دریافت گفتگوهای اخیر
# =========================

def get_context_messages():


    data = get_recent_messages()


    messages = []



    for role, content in data:


        messages.append(

            {

                "role": role,

                "content": content

            }

        )



    return messages
