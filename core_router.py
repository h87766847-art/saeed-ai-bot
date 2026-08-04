# core_router.py
# Saeed Core v6.3

from brain import process_brain

from memory_manager import get_best_memory
from context_intelligence import get_context_information
from planner_intelligence import get_active_plans
from decision_intelligence import get_decisions


def analyze_request(text):

    context = get_context_information(text)
    memory = get_best_memory(text)
    plans = get_active_plans()
    decisions = get_decisions()

    result = process_brain(
        text,
        context,
        memory,
        plans,
        decisions
    )

    return result
