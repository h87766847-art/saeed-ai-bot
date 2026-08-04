# ==========================================
# Saeed AI - Memory Intelligence
# Compatibility Version
# ==========================================

from datetime import datetime


def analyze_memory(text):
    """
    تحلیل متن برای تشخیص اطلاعات مهم
    """

    if not text:
        return {
            "important": False,
            "category": "empty",
            "content": ""
        }


    important_words = [
        "من",
        "اسمم",
        "دوست دارم",
        "علاقه",
        "هدف",
        "پروژه",
        "کار",
        "یاد بگیر",
        "میخوام",
        "می‌خوام"
    ]


    important = False

    for word in important_words:
        if word in text:
            important = True
            break


    if important:

        category = "personal"

    else:

        category = "general"



    return {
        "important": important,
        "category": category,
        "content": text,
        "created_at": str(datetime.now())
    }



def extract_memory(text):
    """
    استخراج اطلاعات قابل ذخیره
    """

    result = analyze_memory(text)

    if result["important"]:
        return result

    return None



def calculate_memory_score(text):
    """
    امتیاز اهمیت حافظه
    """

    if not text:
        return 0


    score = 0


    keywords = [
        "هدف",
        "علاقه",
        "پروژه",
        "دوست دارم",
        "اسمم"
    ]


    for word in keywords:

        if word in text:
            score += 1


    return score



def is_memory_worthy(text):
    """
    آیا این پیام ارزش ذخیره دارد؟
    """

    return calculate_memory_score(text) > 0
