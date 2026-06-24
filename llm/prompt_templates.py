def build_reasoning_prompt(context):
    return f"""
User goal: {context['goal']}
Budget: {context['budget']}
Preferred style:{context['style']}
Suggest suitable solutions.
"""