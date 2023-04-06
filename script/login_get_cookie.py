import time

import requests
from selenium import webdriver

# 登录URL
login_url = 'https://dev.coupert.com/user/login'
login_api = 'https://dev.coupert.com/api/v3/user/signin'

# 模拟登录，发送 POST 请求
datas = {
    "email": "yinapsc30@gmail.com",
    "password": "",

}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
}

response = requests.post(login_api, data=datas, headers=headers)
print('code:', response.status_code)
print('response:', response.json())

# # 获取登录后的 cookie
# cookie_dict = response.cookies.get_dict()
# print('cookie_dict:', cookie_dict)





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
