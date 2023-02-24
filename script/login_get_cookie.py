import time

import requests
from selenium import webdriver

# 登录URL
login_url = 'https://dev.coupert.com/user/login'
login_api = 'https://dev.coupert.com/api/v3/user/signin'

# 模拟登录，发送 POST 请求
data = {
    "email": "yinapsc30@gmail.com",
    "password": "123456",
    "code": "123123123",
    "token": "suchot"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'authority': 'www.coupert.com',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/x-www-form-urlencoded',
    'referer': 'https://dev.coupert.com/user/login'
}

response = requests.post('https://dev.coupert.com/api/v3/user/signin', data=data, headers=headers)
print('code:', response.status_code)
print('response:', response.text)

# 获取登录后的 cookie
cookie_dict = response.cookies.get_dict()
print('cookie_dict:', cookie_dict)


import urllib.parse
import urllib.request

data = urllib.parse.urlencode(data).encode('utf-8')  # 将数据编码为urlencode形式，再转为bytes类型


req = urllib.request.Request(login_api, data)  # 创建请求对象
response1 = urllib.request.urlopen(req)  # 发送请求，获取响应

print(response1.read().decode('utf-8'))  # 打印响应内容

# time.sleep(10)


# # 启动 selenium，添加登录后的 cookie
# options = webdriver.ChromeOptions()
# options.add_argument('start-maximized')
# driver = webdriver.Chrome(options=options)
# driver.get('https://coupert.com')
# for key, value in cookie_dict.items():
#     print("key:", key, ",value:", value)
#     driver.add_cookie({'name': key, 'value': value})
#
# # 刷新页面，即可实现免登录
# driver.refresh()
#
# driver.get('https://coupert.com/user/accunt')
# time.sleep(10)
# driver.close()
