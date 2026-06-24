from reasoning_engine import reason
from graph_loader import load_relationships
from spatial_change_engine import generate_spatial_changes
from prompt_builder import build_prompt
from image_generator import generate_image

relationships = load_relationships()


def run_space_ai(user_id, goal_id):
    result = reason(goal_id, relationships)
    spatial_changes = generate_spatial_changes(result["solutions"])
    prompt = build_prompt(goal_id, spatial_changes)
    image_url = generate_image(prompt)

    return {
        "result": result,
        "spatial_changes": spatial_changes,
        "prompt": prompt,
        "image_url": image_url,
    }