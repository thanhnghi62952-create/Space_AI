def build_prompt(goal_id, spatial_changes):
    prompt = f"""
A beautiful room optimized for { goal_id}.

Recommended changes:
"""
    for change in spatial_changes:
        prompt += f"\n- {change}"
    prompt += """
Style: Jpandi

Lighting: Warm ambient lighting

Mood: Peaceful and relaxing
"""
    return prompt