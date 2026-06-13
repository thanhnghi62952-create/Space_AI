import json

def load_relationships():
    with open("data/relationship.json", "r") as f:
        relationships = json.load(f)
    return relationships