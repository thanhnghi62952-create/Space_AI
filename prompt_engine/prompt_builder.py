def build_prompt(context):
    style = context["favorite_style"]
    room_size = context["room_size"]
    budget = context["budget_level"]
    solutions = ", ".join(context["recommended_solutions"])

    prompt = f"""
Design a beautiful {style} room.
Room size: {room_size}
Budget level: {budget}
Suggested elements: {solutions}
"""
    return prompt