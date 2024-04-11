import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6737613081:AAGwZd1WYOBEoPSg9BjzHhiDHpaH64a7A8g")
    API_ID = int(os.environ.get("API_ID", 20810825))
    API_HASH = os.environ.get("API_HASH", "707e67f53b4593a3e9b6b424311f84d0")
    DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://peter26526:4150YmFscJpMeCkO@cluster0.gjaypdd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
