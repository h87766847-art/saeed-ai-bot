# personality_engine.py
# Saeed Core v6.5
# Personality Engine


import random



PERSONALITY = {

    "name": "Saeed",

    "style": "friendly",

    "language": "fa",

    "confidence": "balanced",

    "emotions": True

}





FRIENDLY_PREFIX = [

    "باشه،",

    "حتماً،",

    "خوبه،",

    "متوجه شدم،"

]





def get_personality():

    return PERSONALITY





def add_personality(text):


    prefix = random.choice(
        FRIENDLY_PREFIX
    )


    return prefix + " " + text





def set_personality(
        key,
        value
):

    if key in PERSONALITY:

        PERSONALITY[key] = value

        return True


    return False





def get_style():

    return PERSONALITY["style"]
