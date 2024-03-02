import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6737613081:AAEIRA_f_oo9IQ5DUwVybbUHF4rrzI9slrU")
    API_ID = int(os.environ.get("API_ID", 20810825))
    API_HASH = os.environ.get("API_HASH", "707e67f53b4593a3e9b6b424311f84d0")
    DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://daniel811802:0wQNzmwMkUiqOZa1@cluster0.8jaksiw.mongodb.net/?retryWrites=true&w=majority")
