class ReasoningAgent:

    def __init__(
            self,
            reasoning_engine,
            redis_handler,
            llm):

        self.reasoning_engine = reasoning_engine
        self.redis_handler = redis_handler
        self.llm = llm


    def run(
            self,
            state):

        cache_key = state["goal_id"]

        cached_result = self.redis_handler.get(
            cache_key
        )

        if cached_result:

            state["recommendations"] = cached_result

            return state


        recommendations = self.reasoning_engine.reason(

            memory=state["memory"],

            graph=state["graph"]

        )

        self.redis_handler.set(

            cache_key,

            recommendations

        )

        state["recommendations"] = recommendations

        return state