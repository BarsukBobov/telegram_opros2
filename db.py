import sqlite3
from loguru import logger


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def post_sigh(self, user_data):
        l=[]
        l1 = []
        for key in user_data:
            l.append(user_data[key])
            l1.append(key)
        l=tuple(l)
        l1 = tuple(l1)
        with self.connection:
            self.cursor.execute(f"INSERT INTO sigh {l1} VALUES {l}")

    def count_sigh(self):
        with  self.connection:
            result=self.cursor.execute("SELECT COUNT(*) FROM sigh").fetchone()[0]
            return result

    def get_sigh(self,i):
        with  self.connection:
            # OFFSET = i - 1.txt
            result=self.cursor.execute(f"SELECT * FROM sigh LIMIT 1 OFFSET {i}").fetchone()
            logger.info(result)
            return result


    def get_all_sigh(self):
        with self.connection:
            result=[]
            var = self.cursor.execute(f"SELECT * FROM sigh").fetchall()
            logger.info(var)
            stroka2 = "Список записей:\n"
            i = 1
            for results in var:
                stroka2 = stroka2 + f"{i}. {results}\n"
                i = i + 1
            stroka2=stroka2+"\nНапишите номер записи, котурую хотите удалить?"
            return stroka2


    def delete_sigh(self, nomer):
        delE = self.cursor.execute(f"DELETE FROM sigh WHERE id = ?", (nomer,))
        logger.info(delE)

    def delete_sigh2(self, rowid):
        with self.connection:
            self.cursor.execute(f"DELETE FROM sigh WHERE rowid = ?", (rowid,))

    def status(self, nomer):
        with self.connection:
            result = self.cursor.execute(f"SELECT rowid FROM sigh").fetchall()
            logger.info(result)
            if len(result) >= nomer > 0:
                index = result[nomer - 1]
                logger.info(index)
                rowid = index[0]
                self.cursor.execute(f"UPDATE sigh SET status=0  WHERE rowid = ?", (rowid,))
            else:
                return False

    def get_status(self):
        with self.connection:
            result = self.cursor.execute(f"SELECT rowid,id FROM sigh WHERE status = 0").fetchone()
            return result
