import json

with open("design_rules.json") as f:
   
    RULES = json.load(f)
def generate_design(goal):

    return RULES[goal]