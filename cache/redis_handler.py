import redis
class RedisHandler:
    def __init__(self):
        self.client = redis.Redis(
            host="localhost",
            port=6379,
            decode_responses=True
        )
    
def set(self, key, value):
    self.client.set(key, value)

def get(self, key):
    return self.client.get(key)

redis_handler = RedisHandler()
redis_handler.set(
    "goal",
    "sleep better"
)
print(redis_handler.get("goal"))
