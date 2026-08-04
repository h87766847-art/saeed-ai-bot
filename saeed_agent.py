# saeed_agent.py
# Saeed AI v3.0
# Core Agent System


from memory_manager import (
    get_best_memory
)


from user_profile import (
    get_profile
)


from planner_intelligence import (
    get_active_plans
)


from decision_intelligence import (
    get_decisions
)


from tool_manager import (
    available_tools
)








def analyze_state(user_text):


    memory = get_best_memory(

        user_text

    )



    profile = get_profile()



    plans = get_active_plans()



    decisions = get_decisions()



    tools = available_tools()





    return {


        "memory":

        memory,


        "profile":

        profile,


        "plans":

        plans,


        "decisions":

        decisions,


        "tools":

        tools

    }









def create_agent_response(

    user_text

):


    state = analyze_state(

        user_text

    )



    response = (

        "🤖 Saeed AI v3.0\n\n"

        "وضعیت تحلیل شد.\n\n"

        "📌 پیام:\n"

        +

        user_text

        +

        "\n\n"

        "🧠 حافظه مرتبط:\n"

        +

        str(state["memory"])

        +

        "\n\n"

        "👤 پروفایل:\n"

        +

        str(state["profile"])

        +

        "\n\n"

        "🎯 برنامه‌های فعال:\n"

        +

        str(state["plans"])

        +

        "\n\n"

        "⚖️ تصمیم‌های ثبت شده:\n"

        +

        str(state["decisions"])

        +

        "\n\n"

        "🛠 ابزارهای موجود:\n"

        +

        str(state["tools"])

    )





    return response
