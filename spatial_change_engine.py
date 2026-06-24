def generate_spatial_changes(solutions):

    changes = []

    mapping = {
        "blackout_curtains": "Install blackout curtains",
        "warm_lighting": "Use warm ambient lighting",
        "white_noise_machine": "Add a white noise machine"
    }
    for solution in solutions:
        if solution in mapping:
            changes.append(mapping[solution])
    return changes