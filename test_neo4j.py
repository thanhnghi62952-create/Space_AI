from graph_database.neo4j_handler import create_user_node
from graph_database.neo4j_handler import test_connection
print(test_connection())

create_user_node("user_001")
print("User node created.")