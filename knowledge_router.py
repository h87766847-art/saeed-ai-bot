from vector_memory import (
    init_vectors,
    save_vector,
    search_vector
)


init_vectors()



def remember_knowledge(text):

    save_vector(
        text
    )

    return True




def retrieve_knowledge(query):

    results = search_vector(
        query
    )


    if not results:

        return ""


    context = ""


    for score,text in results:

        if score > 0:

            context += (
                text
                +
                "\n"
            )


    return context
