import sqlite3
from loguru import logger


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def create_table(self):
        with self.connection:
            res = self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS users
            (id integer PRIMARY KEY AUTOINCREMENT,
            chat_id BIGINT UNIQUE,
            name text, 
            email TEXT,
            mob_tel BIGINT,
            result  VARCHAR(4),
            result_e INT,
            result_s INT,
            result_t INT,
            result_j INT,
            result_sum INT
            )
            ''')
            return res

    def post_result(self, *args):
        l = (args)
        keys="(chat_id, name, email, mob_tel, result, result_e, result_s, result_t, result_j, result_sum)"
        print(l)
        try:
            with self.connection:
                self.cursor.execute(f"INSERT INTO users {keys} VALUES {l}")
        except:
            new_l=(args[1:])
            string=''
            res = keys[1:-1].split(", ")
            new_keys=(res[1:])
            for elem in new_keys:
                string+=f'{elem}=?, '
            print(string[:-2])
            with self.connection:
                self.cursor.execute(f"UPDATE users SET {string[:-2]} WHERE chat_id={l[0]}", new_l)

    #Optional
    def drop_table(self):
        with self.connection:
            res = self.cursor.execute(f'''DROP TABLE users''')
            return res
