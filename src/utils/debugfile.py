import json
import jsonpath
import re
import pymysql
from sshtunnel import SSHTunnelForwarder

# 设置SSH隧道信息
server = SSHTunnelForwarder(
    ssh_address_or_host=('44.242.9.67', 10086),
    ssh_username='suchotsu',
    ssh_password='3b82ed78B4C947369d!!!',
    remote_bind_address=('172.16.13.96', 3306),
    local_bind_address=('0.0.0.0', 3306),
)

# 启动SSH隧道
server.start()

# 使用 PyMySQL 连接到数据库
conn = pymysql.connect(
    host='0.0.0.0',
    port=3306,
    user='coupert',
    password='5fToKatrb+Y',
    database='coupert_base',
    charset='utf8',
    local_infile=1,
    cursorclass=pymysql.cursors.DictCursor
)
cursor = conn.cursor()

# 执行SQL语句
cursor.execute("SELECT code FROM user_verification_code where type='withdraw' and user_id=5231600;")
result = cursor.fetchall()

# 通过正则获取验证码
pattern = re.compile(r"'code'\s*:\s*'(\w+)'")
text = re.search(pattern, str(result))

if text:
    print(text.group(1))

# result = json.dumps(result[0])
# result = jsonpath.jsonpath(result, '$.code')
# print(result)

# 关闭连接
cursor.close()
conn.close()

# 关闭SSH隧道
server.stop()
