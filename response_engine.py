# response_engine.py
# Saeed AI v2.5
# Memory Connected Response System


from brain import (
    build_memory_context,
    get_context_messages
)


from context_intelligence import (
    get_context_information
)


from memory_manager import (
    get_best_memory
)





def build_memory_prompt(user_text):


    memory = get_best_memory(

        user_text

    )



    if memory:


        return (

            "خاطره مرتبط:\n"

            +

            memory.get(

                "content",

                ""

            )

        )



    return "خاطره مرتبطی پیدا نشد."








def generate_response(user_text):


    # حافظه قدیمی گفتگو

    memory_context = build_memory_context()



    # زمینه فعلی

    context = get_context_information()



    # پیام‌های قبلی

    messages = get_context_messages()



    # حافظه هوشمند

    smart_memory = build_memory_prompt(

        user_text

    )







    response = (

        "🧠 سعید AI v2.5\n\n"

        "پیام تو:\n"

        +

        user_text

        +

        "\n\n"

        "📌 حافظه مرتبط:\n"

        +

        smart_memory

        +

        "\n\n"

        "📚 تاریخچه گفتگو:\n"

        +

        str(memory_context)

        +

        "\n\n"

        "🔎 وضعیت فعلی:\n"

        +

        str(context)

    )





    return response
