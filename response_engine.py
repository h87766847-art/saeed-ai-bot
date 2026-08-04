from brain import (
    build_memory_context,
    get_context_messages
)

from context_intelligence import (
    get_context_information
)



def generate_response(user_text):


    # گرفتن حافظه کوتاه مکالمه

    memory = build_memory_context()



    # گرفتن وضعیت زمینه

    context = get_context_information()



    # گرفتن پیام‌های قبلی

    messages = get_context_messages()



    response = (

        "🧠 سعید AI\n\n"

        "پیام تو دریافت شد:\n"

        + user_text

        +

        "\n\n"

        "📚 حافظه مرتبط:\n"

        +

        memory

        +

        "\n\n"

        "🔎 وضعیت زمینه:\n"

        +

        str(context)

    )



    return response
