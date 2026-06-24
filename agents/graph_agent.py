from graph_database.neo4j_handler import graph_db


class GraphAgent:

    def run(self, state):
        goal_id = state["goal_id"]

        graph_data = {"similar_goals":graph_db.get_similar_goals(goal_id),
                      "candidate_solutions":graph_db.get_goal_solutions(goal_id)
                      }
        state["graph"] = graph_data
        return state