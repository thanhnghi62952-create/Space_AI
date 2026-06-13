from openai import OpenAI

client = OpenAI()

def generate_image(prompt):

    response = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1536x1024"
    )
    return response.data[0].b64_json