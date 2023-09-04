# 创建一个MySQL连接对象
from util.mysql_connect import MySQLConnection


if __name__ == "__main__":
    mysql_conn = MySQLConnection("localhost", "root", "Yzl1234567", "stock_data")

    # 执行查询并获取结果
    results = mysql_conn.execute_query("SELECT * FROM t_600633")
    for row in results:
        print(row)

    # 执行不返回结果的查询（例如更新操作）
    # mysql_conn.execute_query_no_result("UPDATE 600633 SET column1 = 'new value' WHERE condition")