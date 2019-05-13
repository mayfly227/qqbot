import sqlite3

from log import botLog


class DbUtils():

    def __init__(self):
        self._conn = None
        self._cursor = None
    def __enter__(self):
        try:
            self._conn = sqlite3.connect("D:\Programing\python\qqbot\qqbot.db")
            self._cursor = self._conn.cursor()
            return self._conn.cursor()
        except Exception as e:
            botLog.error(e)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            # 发生错误，rollback
            if exc_type is not None:
                botLog.error("error type is {}".format(exc_type))
                self._conn.rollback()
            else:
                self._conn.commit()
            if exc_val is not None or exc_tb is not None:
                pass
        except Exception as e:
            botLog.error(e)
        finally:
            self._cursor.close()
            self._conn.close()
            botLog.info("successful close db connection!")
            return True
