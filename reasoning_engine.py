from graph_query import get_targets


def reason(goal_id, relationships):

    # Goal -> Outcome
    outcomes = get_targets(
        goal_id,
        "HAS_OUTCOME",
        relationships
    )

    # Outcome -> Factor
    factors = []

    for outcome in outcomes:

        factors.extend(
            get_targets(
                outcome,
                "AFFECTED_BY",
                relationships
            )
        )

    # Factor -> Strategy
    strategies = []

    for factor in factors:

        strategies.extend(
            get_targets(
                factor,
                "SOLVED_BY",
                relationships
            )
        )

    # Strategy -> Solution
    solutions = []

    for strategy in strategies:

        solutions.extend(
            get_targets(
                strategy,
                "IMPLEMENTED_BY",
                relationships
            )
        )

    # Loại bỏ phần tử trùng nhau
    return {
        "outcomes": list(set(outcomes)),
        "factors": list(set(factors)),
        "strategies": list(set(strategies)),
        "solutions": list(set(solutions))
    }