def personalize( ranked_solutions, preferences):
    personalized = {
        "solutions": ranked_solutions,
        "lighting": preferences.get(
            "lighting",
            "neutral"
        ),
        "material": preferences.get(
            "style",
            "neutral"
        )
    }
    return personalized