import json

def save_feedback(feedback):
    with open("data/user_feedback.json","r", encoding="utf-8") as f:
        data = json.load(f)
    data.append(feedback)
    with open("data/user_feedback.json","w",encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )
    
feedback = {
    "user_id": "default_user",
    "goal_id": "sleep",
    "style": "japandi",
    "rating": 5
}
save_feedback(feedback)