def build_prompt(changes):
    prompt = """
    Modern minimalist bedroom optimized for sleep.
    """ 

    for change in changes:

        prompt += change["action"] + ", "
    return prompt