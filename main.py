from graph_loader import load_relationships
from reasoning_engine import reason
from explanation_engine import explain
from gpt_explainer import generate_explanation

def main():
    # Load relationships graph
    relationships = load_relationships()
    print(relationships)
    # Goal người dùng chọn
    goal_id = "sleep"
    # Reasoning
    result = reason(goal_id, relationships)
    explanation = generate_explanation(result)
    print(explanation)
    print(result)
    # Explain result
    explanation = explain(result)
    print(explanation)
    # in kết quả
    print(":\n===== RESULT =====")

    print("\nOutcome:")
    for outcome in result["outcomes"]:
        print("-", outcome)
    
    print("\nFactors:")
    for factor in result ["factors"]:
        print("-", factor)

    print("\nStrategies:")
    for strategy in result["strategies"]:
        print("-", strategy)

    print("\nSolutions:")
    for solution in result["solutions"]:
        print("-", solution)

if __name__ == "__main__":
    main()