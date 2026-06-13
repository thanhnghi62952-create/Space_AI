import openai

# use openai.OpenAI() to create the client; some environments/reporting tools
# expect the top-level import rather than a direct symbol import.
client = openai.OpenAI()

def generate_explanation(result):

    prompt = f"""
    Goal factors: 
    {result["factors"]}

    Strategies: 
    {result["strategies"]}

    Solutions:
    {result["solutions"]}

    Explain naturally for the user.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    return response.output_text