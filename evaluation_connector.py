from self_evaluator import evaluate
from learning_connector import remember_result





def evaluate_and_learn(
    situation,
    result,
    feedback,
    score
):


    evaluation = evaluate(

        situation,

        result,

        score

    )



    remember_result(

        situation,

        result,

        feedback

    )



    return evaluation
