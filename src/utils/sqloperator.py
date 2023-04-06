import re

import pymysql
from sshtunnel import SSHTunnelForwarder


class Database:
    def __init__(self, ssh_host, ssh_user, ssh_password, database_host, database_user, database_password,
                 database_name):
        self.ssh_host = ssh_host
        self.ssh_user = ssh_user
        self.ssh_password = ssh_password
        self.database_host = database_host
        self.database_user = database_user
        self.database_password = database_password
        self.database_name = database_name
        self.server = None
        self.conn = None

    def __enter__(self):
        # 设置SSH隧道信息
        self.server = SSHTunnelForwarder(
            ssh_address_or_host=(self.ssh_host, 10086),
            ssh_username=self.ssh_user,
            ssh_password=self.ssh_password,
            remote_bind_address=(self.database_host, 3306),
            local_bind_address=('0.0.0.0', 3306),
        )

        # 启动SSH隧道
        self.server.start()

        # 使用 PyMySQL 连接到数据库
        self.conn = pymysql.connect(
            host='0.0.0.0',
            port=3306,
            user=self.database_user,
            password=self.database_password,
            database=self.database_name,
            charset='utf8',
            local_infile=1,
            cursorclass=pymysql.cursors.DictCursor
        )

        return self.conn

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # 关闭连接
        self.conn.close()
        # 关闭SSH隧道
        self.server.stop()

def execute_sql(sql):
    # 执行SQL语句，获取查询结果
    with Database(
            ssh_host=ssh_host,
            ssh_user=ssh_user,
            ssh_password=ssh_password,
            database_host=database_host,
            database_user=database_user,
            database_password=database_password,
            database_name=database_name
    ) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
