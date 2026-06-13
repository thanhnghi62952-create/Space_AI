def get_targets(source_id, relation, relationships): 
    targets = []

    for edge in relationships:
        if (edge["source_id"] == source_id
            and edge["relation"] == relation):
            targets.append(edge["target_id"])
    return targets