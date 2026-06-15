def personalize(
        ranked_solutions,
        profile):
    personalized = []

    for item in ranked_solutions:
        score = item["score"]

        if (profile["budget_level"] == "low" and item["solution_id"] == "smart_glass_window"):
            score -= 0.5
        personalized.append({
            "solution_id": item["solution_id"],
            "score": score
        })
    personalized.sort(
        key=lambda x: x["score"],
        reverse=True
    )
    return personalized