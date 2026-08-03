from memory import (
    save_memory,
    get_memories,
    save_message,
    get_recent_messages
)


def remember_important_information(text):

    keywords = [
        "اسم من",
        "من هستم",
        "علاقه دارم",
        "دوست دارم",
        "هدفم",
        "می‌خواهم",
        "میخوام"
    ]

    for key in keywords:

        if key in text:

            save_memory(
                "important",
                text
            )

            return True

    return False



def build_memory_context():

    memories = get_memories()

    if not memories:
        return "اطلاعات مهمی ذخیره نشده."

    result = "اطلاعات مهم درباره حسین:\n"

    for item in memories:

        result += (
            "- "
            + item[1]
            + "\n"
        )

    return result



def save_conversation(
    role,
    text
):

    save_message(
        role,
        text
    )



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
