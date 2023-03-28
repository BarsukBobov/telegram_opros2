import sqlite3
from loguru import logger


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def create_database(self):
        with self.connection:
            res = self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS users
            (id integer PRIMARY KEY AUTOINCREMENT,
            chat_id BIGINT UNIQUE,
            name text, 
            email TEXT,
            result INT)
            ''')
            return res

    def post_result(self, chat_id, name, email, result):
        l = (chat_id, name, email, result)
        try:
            with self.connection:
                self.cursor.execute(f"INSERT INTO users (chat_id, name, email, result) VALUES {l}")
        except:
            with self.connection:
                self.cursor.execute(f"UPDATE users SET name=?, email=?, result =? WHERE chat_id={chat_id}", (name, email, result))
