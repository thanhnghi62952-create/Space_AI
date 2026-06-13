def build_prompt(plan):
    return f"""
bedroom,
{plan['lighting']},
{plan['color']},
{plan['layout']}
"""