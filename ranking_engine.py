def rank_solutions(
        solutions,
        preference_scores):
    ranked = []

    for solution in solutions:
        score = preference_scores.get(
            solution,
            0.5
        )

        ranked.append({
            "solution_id": solution,
            "score": score
        })
    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )
    return ranked