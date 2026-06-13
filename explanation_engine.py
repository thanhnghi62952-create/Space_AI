def explain(result):

    text = ""

    text += "Factors affecting the goal:\n"

    for factor in result["factors"]:
        text += f"- {factor}\n"

    text += "\nRecommended solutions:\n"

    for solution in result["solutions"]:
        text += f"- {solution}\n"

    return text