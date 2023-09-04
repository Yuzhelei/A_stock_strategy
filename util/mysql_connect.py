import pymysql


class MySQLConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        try:
            connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("成功连接到MySQL数据库")
            return connection
        except pymysql.Error as e:
            print(f"连接MySQL数据库失败: {e}")

    def execute_query(self, query):
        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return result

    def execute_query_no_result(self, query):
        connection = self.connect()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query)
            cursor.close()
            connection.close()
            return None