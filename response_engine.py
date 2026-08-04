from brain import (
    build_memory_context,
    get_context_messages
)


from context_intelligence import (
    get_context_information
)





def search_memory(user_text, memory):


    keywords = user_text.split()



    found = []



    for word in keywords:


        if word in memory:


            found.append(word)





    if found:


        return "اطلاعات مرتبط پیدا شد: " + ", ".join(found)



    return "اطلاعات مرتبط قبلی پیدا نشد"








def generate_response(user_text):


    # دریافت حافظه

    memory = build_memory_context()



    # دریافت زمینه گفتگو

    context = get_context_information()



    # دریافت پیام‌های قبلی

    messages = get_context_messages()





    # جستجو در حافظه

    memory_result = search_memory(

        user_text,

        memory

    )







    response = (

        "🧠 سعید AI v2.1\n\n"

        "پیام جدید:\n"

        +

        user_text

        +

        "\n\n"

        "📚 بررسی حافظه:\n"

        +

        memory_result

        +

        "\n\n"

        "🗂 سابقه گفتگو:\n"

        +

        memory

        +

        "\n"

        +

        "\n🔎 زمینه فعلی:\n"

        +

        str(context)

    )





    return response
