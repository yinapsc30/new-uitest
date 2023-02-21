import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import pyautogui
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckAccount:

    def __init__(self):
        self.options = Options()
        # self.options.add_argument('--headless')
        self.firefox_services = Service(executable_path='firefoxdriver', port=3000,
                                        service_args=['--marionette-port', '2828', '--connect-existing'])
        self.driver = webdriver.Firefox(service=self.firefox_services, options=self.options)
        self.actions = ActionChains(self.driver)
        self.driver.implicitly_wait(100)
        self.domain = 'https://www.coupert.com'

    def test_check(self):
        driver = self.driver
        rules = {'/': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/user/account': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/user/gold-order': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/user/offers': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/user/gift-cards': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/user/missing-cashback': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/user/withdraw': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/user/task': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/user/cashback-trips': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/user/droplist': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/user/invite': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/how-it-works': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/user/account-settings': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/user/service-preferences': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/change/email': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/change/password': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/change/paypal': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/search/result': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 # '/static/ios_start_step': '18',
                 '/user/missing-cashback-commit': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/user/withdraw_money': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/blackfriday': '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]',
                 '/company': '/html/body/header/div/div[1]/div[3]/div/span',
                 '/eula': '/html/body/header/div/div[1]/div[3]/div/span',
                 '/p/fe4c3c9cf6180751d14f725daffdc97c?domain=amazon.com&pid=fe4c3c9cf6180751d14f725daffdc97c&source=extension':
                     '//*[@id="__div_id_header"]/div/div[3]/div/div[1]/div/div[2]'}

        while True:
            for path, el_ in rules.items():
                driver.get(self.domain + path)
                self.driver.implicitly_wait(100)

                try:
                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, el_)))
                    # 在元素可见之后，就可以对它进行操作了
                    username = driver.find_element(By.XPATH, el_).text
                    assert username == '潘燚'
                    print(f'页面{path}用户信息正常')
                finally:
                    time.sleep(2)


if __name__ == '__main__':
    ac = CheckAccount()
    ac.test_check()