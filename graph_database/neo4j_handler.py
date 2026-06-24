from neo4j import GraphDatabase
URL = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "0399662952"
driver = GraphDatabase.driver(URL, auth=(USERNAME, PASSWORD))

def test_connection():
    with driver.session() as session:
        return session.run(
            "RETURN 'Space AI connected successfully'"
        ).single()[0]
  

def create_user_node(user_id):
    with driver.session() as session:
        session.run(
            """
            MERGE (u:User {user_id:$user_id})
            """,
            user_id = user_id
        )

def create_goal_node(goal_id):
    with driver,session() as session:
        session.run(
            """
            MERGE (g:Goal {goal_id:$goal_id})
            """,
            goal_id=goal_id
        )

def create_solution_node(solution_name):
    with driver.session() as session:
        session.run(
            """
            MERGE (s:Solution { name:$solution_name})
            """,
            solution_name=solution_name
        )

def create_style_node(style_name): # tôi muốn tạo ham định nghĩa mới là style
    with driver.session() as session: # mở một phiên làm việc với neo4j kết nois với neo4j
        session.run( # hãy thực hiện lệnh sau trong database 
            """
            MERGE (s:Style {
            name:$style_name})
            """,
            style_name=style_name # lấy giá trị style ở bên ngoài đưa vào trong câu lệnh neo4j
        )# tiếng cypher nếu style chưa tồn tại thì hãy tạo nó 
        #merge nghĩa là nếu chưa có thì tạo nếu có rồi thì dùng lại

def create_room_node(room_size):
    with driver.session() as session:
        session.run(
            """
            MERGE (r:Room {size:$room_size})
            """,
            room_size=room_size
        )
# TẠO QUAN HỆ SOLUTIONS
def connect_solution_to_goal(solution_name, goal_id):
    with driver.session() as session:
        session.run(
            """
            MATCH (g:Goal {goal_id:$goal_id})
            MERGE (s)-[:SOLVES]->(g)
            """,
            solution_name=solution_name,
            goal_id=goal_id
        )
    
def connect_user_to_solution(user_id, solution_name):
    with driver.session() as session:
        session.run(
            """
            MATCH (u:User {user_id:$user_id})
            MATCH (s:Solution {name:$solution_name})
            MERGE (u)-[:USED]->(s)
            """,
            user_id=user_id,
            solution_name=solution_name
        )

def connect_user_to_style(user_id, style_name): # tạo hàm kết nối user với style user001 thích jazz
    with driver.session() as session:#kết nối với neo4j
        session.run( # thực hiện câu lệnh cypher (đoạn 1: tìm người có dòng user id tương ứng đoạn 2: tim style tương ứng, đoạn 3:  tiếng cypher tạo quan hệ nếu chưa tồn tại thì khởi tạo nó)
            """ 
            MATCH (u:User {user_id:$user_id})   
            MATCH (s:Style {name:$style_name})
            MERGE (u)-[:LIKES]->(s)
            """,
            user_id=user_id, # truyền user id vào query
            style_name=style_name # truyền style name vào quẻy
        )

def connect_user_to_room(
user_id,
room_size):
    with driver.session() as session:

      session.run(

        """

        MATCH (u:User {

            user_id:$user_id

        })

        MATCH (r:Room {

            size:$room_size

        })

        MERGE (u)-[:HAS_ROOM]->(r)

        """,

        user_id=user_id,
        room_size=room_size

    )
      
def connect_goal_similarity(
goal_1,
goal_2):

 with driver.session() as session:

    session.run(

        """

        MATCH (g1:Goal {

            goal_id:$goal_1

        })

        MATCH (g2:Goal {

            goal_id:$goal_2

        })

        MERGE (g1)-[:SIMILAR_TO]->(g2)

        MERGE (g2)-[:SIMILAR_TO]->(g1)

        """,

        goal_1=goal_1,

        goal_2=goal_2

    )

def connect_solution_similarity(
solution_1,
solution_2):

 with driver.session() as session:

    session.run(

        """

        MATCH (s1:Solution {

            name:$solution_1

        })

        MATCH (s2:Solution {

            name:$solution_2

        })

        MERGE (s1)-[:SIMILAR_TO]->(s2)

        MERGE (s2)-[:SIMILAR_TO]->(s1)

        """,

        solution_1=solution_1,

        solution_2=solution_2

    )

def get_user_solutions(
user_id):

 with driver.session() as session:

    result = session.run(

        """

        MATCH

        (u:User)-[:USED]->

        (s:Solution)

        WHERE

        u.user_id=$user_id

        RETURN s.name

        """,

        user_id=user_id

    )

    return [

        record["s.name"]

        for record in result

    ]
 
 def get_goal_from_solution(
solution_name):

   with driver.session() as session:

    result = session.run(

        """

        MATCH

        (s:Solution)-[:SOLVES]->

        (g:Goal)

        WHERE

        s.name=$solution_name

        RETURN g.goal_id

        """,

        solution_name=solution_name

    )

    return [

        record["g.goal_id"]

        for record in result

    ]
   
def get_similar_goals(
goal_id):

  with driver.session() as session:

    result = session.run(

        """

        MATCH

        (g1:Goal)-[:SIMILAR_TO]->

        (g2:Goal)

        WHERE

        g1.goal_id=$goal_id

        RETURN g2.goal_id

        """,

        goal_id=goal_id

    )

    return [

        record["g2.goal_id"]

        for record in result

    ]
  
def graph_reasoning(
user_id):

  with driver.session() as session:

    result = session.run(

        """

        MATCH

        (u:User)-[:USED]->

        (s1:Solution)-[:SOLVES]->

        (g1:Goal)-[:SIMILAR_TO]->

        (g2:Goal)<-[:SOLVES]-

        (s2:Solution)

        WHERE

        u.user_id=$user_id

        AND

        s1<>s2

        RETURN DISTINCT

        s2.name

        """,

        user_id=user_id

    )

    return [

        record["s2.name"]

        for record in result

    ]
  
class Neo4jHandler:
   ...


gragh_db = Neo4jHandler(
   url="neo4j://127.0.0.1:7687",
   username="neo4j",
   password="0399662952"
)