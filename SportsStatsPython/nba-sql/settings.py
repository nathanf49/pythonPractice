import os
from dotenv import load_dotenv
from peewee import *
load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_user = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')


class settings:
    def __init__(self):
        self.db = MySQLDatabase(DB_NAME, host=DB_HOST, user=DB_user, passwd=DB_PASSWORD, charset='utf8mb4')
        self.user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"