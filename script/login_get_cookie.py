import time

import requests
from selenium import webdriver

# 登录URL
login_url = 'https://dev.coupert.com/user/login'
login_api = 'https://dev.coupert.com/api/v3/user/signin'

# 模拟登录，发送 POST 请求
data = {
    "code": "123123123",
    "email": "testpan01@123.com",
    "password": "123456",
    "token": "suchot"
}
response = requests.post(login_api, data=data)
print('response:', response.status_code)
print('response:', response.text)

# 获取登录后的 cookie
cookie_dict = response.cookies.get_dict()
print('cookie_dict:', cookie_dict)

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
