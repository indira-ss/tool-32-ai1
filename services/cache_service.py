import redis
import hashlib
import json

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

TTL_SECONDS = 900


def generate_cache_key(text):
    return hashlib.sha256(text.encode()).hexdigest()


def get_cached_response(text):

    key = generate_cache_key(text)

    cached_data = redis_client.get(key)

    if cached_data:
        return json.loads(cached_data)

    return None


def set_cached_response(text, data):

    key = generate_cache_key(text)

    redis_client.setex(
        key,
        TTL_SECONDS,
        json.dumps(data)
    )