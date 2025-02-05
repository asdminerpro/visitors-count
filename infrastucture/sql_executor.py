import sqlite3
from os.path import isfile


class SQLExecutor:
    def __init__(self, database_name="database.db"):
        self.database_name = database_name
        self._exist_or_create()

    def execute(self, sql_string):
        with sqlite3.connect(self.database_name) as connection:
            cursor = connection.cursor()
            result = list(cursor.execute(sql_string))
            cursor.fetchall()
            cursor.close()
        return result

    def try_insert(self, table, **kwargs):
        sql = f"INSERT OR IGNORE INTO {table} " \
              f"({', '.join(kwargs.keys())}) " \
              f"VALUES ({', '.join(map(str, kwargs.values()))})"
        return self.execute(sql)

    def _exist_or_create(self):
        if isfile(self.database_name):
            return
        conn = sqlite3.connect(self.database_name)
        conn.close()
        table_users = """CREATE TABLE visits (
                    page_id INTEGER,
                    client_id TEXT,
                    visit_time TEXT
                );"""
        self.execute(table_users)

    def select_for_days(self, period, page_id):
        sql = f"SELECT client_id FROM visits " \
              f"WHERE visit_time " \
              f"BETWEEN datetime('now', '{period}') " \
              f"AND datetime('now', 'localtime')" \
              f"AND page_id ={page_id};"
        return self.execute(sql)

    def count_all(self, page_id, period, unique=False):
        selection = self.select_for_days(period, page_id)
        if not selection:
            return 0
        if not unique:
            return len(selection)
        return len(set(map(lambda x: x[0], selection)))
