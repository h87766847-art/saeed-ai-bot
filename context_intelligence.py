from context_manager import (
    init_context,
    update_context,
    context_prompt
)



init_context()





def detect_context(text):


    topic = "گفتگو عمومی"

    subtopic = ""

    goal = ""




    if "سعید" in text or "ربات" in text:

        topic = "پروژه سعید"



    if "حافظه" in text:

        subtopic = "سیستم حافظه"




    if "کد" in text or "برنامه" in text:

        subtopic = "توسعه نرم افزار"




    if "هدف" in text or "میخواهم" in text or "می‌خواهم" in text:

        goal = text





    update_context(

        topic,

        subtopic,

        goal

    )


    return True





def get_context_information():

    return context_prompt()
