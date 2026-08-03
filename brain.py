from memory import (
    get_memories,
    save_message,
    get_recent_messages,
    get_profile
)

from smart_memory import smart_remember



# =========================
# حافظه هوشمند
# =========================

def remember_important_information(text):

    return smart_remember(
        text
    )



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
            "اطلاعات مهمی ذخیره نشده."
        )


    return result



# =========================
# گفتگو
# =========================

def save_conversation(
    role,
    text
):

    save_message(
        role,
        text
    )



def get_context_messages():

    data = get_recent_messages(
        30
    )


    messages = []


    for role, content in data:

        messages.append(

            {
                "role": role,
                "content": content
            }

        )


    return messages
