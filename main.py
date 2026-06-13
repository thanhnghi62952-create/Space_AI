from goal_engine import understand_goal
from design_engine import generate_design
from prompt_builder import build_prompt

goal = understand_goal(
    "better sleep"
)
plan = generate_design(goal)

prompt = build_prompt(plan)

print(plan)
print(prompt)