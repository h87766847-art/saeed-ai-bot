# memory_intelligence.py
# Saeed Core v6.3
# Smart Memory Intelligence


import re



IMPORTANT_WORDS = [

    "اسم",
    "نام",
    "سن",
    "علاقه",
    "دوست دارم",
    "متنفرم",
    "کار",
    "هدف",
    "یاد بگیر",
    "به یاد داشته باش"

]





def analyze_memory(text):

    text = text.lower()


    score = 0


    found = []



    for word in IMPORTANT_WORDS:

        if word in text:

            score += 1
            found.append(word)



    return {

        "text": text,

        "importance_score": score,

        "important": score > 0,

        "keywords": found

    }





def extract_information(text):


    data = {}



    patterns = {


        "name":
        r"(?:اسم من|نام من)\s+(.+)",


        "age":
        r"(?:سن من|من)\s+(\d+)\s+سال",


        "interest":
        r"(?:علاقه دارم به|دوست دارم)\s+(.+)"


    }




    for key, pattern in patterns.items():


        result = re.search(
            pattern,
            text
        )


        if result:

            data[key] = result.group(1).strip()



    return data
