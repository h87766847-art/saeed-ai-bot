from memory import save_profile, get_profile



def detect_preferences(text):

    preferences = []


    if "کامل" in text or "جزئیات" in text:

        preferences.append(
            ("response_style", "کامل و توضیحی")
        )


    if "کوتاه" in text:

        preferences.append(
            ("response_style", "کوتاه و مستقیم")
        )


    if "مثال" in text:

        preferences.append(
            ("examples", "با مثال توضیح بده")
        )


    if "ساده" in text:

        preferences.append(
            ("language_style", "ساده و قابل فهم")
        )



    for key, value in preferences:

        save_profile(
            key,
            value
        )



    return preferences



def get_preferences():

    return get_profile()
