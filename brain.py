from memory import (
    get_memories,
    save_message,
    get_recent_messages,
    get_profile
)

from smart_memory import smart_remember

from preferences import detect_preferences



# =========================
# Smart Memory
# =========================

def remember_important_information(text):

    smart_remember(text)

    detect_preferences(text)



# =========================
# Memory Context
# =========================

def build_memory_context():

    memories = get_memories()

    profile = get_profile()


    result = ""



    if profile:

        result += "\nترجیحات و اطلاعات حسین:\n"


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
            "حافظه خالی است."
        )


    return result



# =========================
# Conversation
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
