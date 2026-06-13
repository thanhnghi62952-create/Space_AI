import json

def load_spatial_changes():

    with open("data/spatial_changes.json","r",encoding="utf-8") as f:
        return json.load(f)
    
def get_changes(solution_id):
    spatial_data = load_spatial_changes()

    for item in spatial_data:

        if item["solution_id"] == solution_id:
            return item["changes"]
    return []