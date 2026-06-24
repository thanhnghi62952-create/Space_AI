def build_context(
        user_id,
        goal_id,
        favorite_style,
        room_size,
        budget_level,
        recommended_solutions
):
    return {
        "user_id": user_id,
        "goal_id": goal_id,
        "favorite_style": favorite_style,
        "room_size": room_size,
        "budget_level": budget_level,
        "recommended_solutions": recommended_solutions
    }