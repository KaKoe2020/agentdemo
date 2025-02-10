import os

MODEL_CONFIG = {
    "OPEN_AI_KEY": os.getenv("OPEN_AI_API_KEY"),
    "OPEN_AI_ENDPOINT": os.getenv("DEPLOYMENT_ENDPOINT"),
    "OPEN_AI_MODEL": os.getenv("DEPLOYMENT_NAME"),
    "temperature": 0.7,
    "max_tokens": 500
}