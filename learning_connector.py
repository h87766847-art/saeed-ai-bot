from learning_loop import (
    add_experience,
    get_experiences
)





def remember_result(
    situation,
    response,
    feedback
):


    return add_experience(

        situation,

        response,

        feedback

    )







def get_learning_context():


    experiences = get_experiences()


    context = ""



    for item in experiences[-5:]:


        context += (

            "موقعیت: "

            +

            item["situation"]

            +

            "\nنتیجه: "

            +

            item["result"]

            +

            "\nبازخورد: "

            +

            item["feedback"]

            +

            "\n\n"

        )



    return context
