import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class smoking_test(unittest.TestCase):

    def setUp(self):
        # chrome_options = Options()
        # # chrome_options.add_argument('--headless')
        # # width, height = pyautogui.size()
        # # chrome_options.add_argument('--window-size=%sx%s' % (width, height))
        # chrome_options.add_argument("--window-size=1920,1080")
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # chrome_options.add_experimental_option('useAutomationExtension', False)
        # chrome_options.add_argument(
        #     "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
        # self.driver = webdriver.Chrome(options=chrome_options)
        # # self.driver = webdriver.Chrome
        # self.driver.implicitly_wait(100)
        # self.chrome_options = Options()
        # self.chrome_options.add_argument(
        #     "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
        # self.chrome_options.debugger_address = 'localhost:9222'
        # # driver就是当前浏览器窗口
        # self.chrome_driver = "/usr/local/bin/chromedriver"
        # self.driver = webdriver.Chrome(options=self.chrome_options)
        # # self.driver.get('https://www.coupert.com/user/login')
        # self.driver.implicitly_wait(100)

        self.options = Options()
        # self.options.add_argument('--headless')
        self.firefox_services = Service(executable_path='firefoxdriver', port=3000,
                                        service_args=['--marionette-port', '2828', '--connect-existing'])
        self.driver = webdriver.Firefox(service=self.firefox_services, options=self.options)
        self.actions = ActionChains(self.driver)
        self.driver.implicitly_wait(100)
        self.domain = 'https://www.coupert.com'

        # self.driver = webdriver.Firefox(executable_path=self.firefox_driver, options=self.options)

    def test_smokeing(self):
        driver = self.driver
        path_list = ['/',
                     '/user/account',
                     '/user/gold-order',
                     '/user/offers',
                     '/user/gift-cards',
                     '/user/missing-cashback',
                     '/user/withdraw',
                     '/user/task',
                     '/user/cashback-trips',
                     '/user/droplist',
                     '/user/invite',
                     '/how-it-works',
                     '/user/account-settings',
                     '/user/service-preferences',
                     '/change/email',
                     '/change/password',
                     '/change/paypal',
                     '/search/result',
                     '/static/ios_start_step',
                     '/user/missing-cashback-commit',
                     '/user/withdraw_money',
                     '/blackfriday',
                     '/company',
                     '/eula',
                     '/p/fe4c3c9cf6180751d14f725daffdc97c?domain=amazon.com&pid=fe4c3c9cf6180751d14f725daffdc97c&source=extension']
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

        driver.get(self.domain)
        self.driver.implicitly_wait(100)
        el_ = '//*[@id="__div_id_header"]/div[1]/div[3]/div/div[1]/div/div[2]'
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, el_)))
            # 在元素可见之后，就可以对它进行操作了
            username = driver.find_element(By.XPATH, el_).text
            assert username == '潘燚'
        except:
            pass

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

    def test_baidu(self):
        driver = self.driver
        driver.get("https://www.baidu.com/")
        driver.get_screenshot_as_file("baidu.png")
        el = driver.find_element(By.XPATH, "//input[@id='su']").get_attribute('value')
        print(el)

    def test_withdraw(self):
        driver = self.driver
        actions = self.actions
        driver.get('https://dev.coupert.com/user/account')
        # driver.find_element_by_xpath('//*[@id="__next"]/div/div/main/div[2]/div[2]/div/div[3]/div/div/div/div/input')
        withdraw = '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div'
        # actions.move_to_element(withdraw).click().perform()
        driver.find_element(By.XPATH, withdraw).click()
        paypal_des = '//*[@id="__next"]/main/div/div[2]/div/div[2]/div/div[2]/div/div[1]/h3'
        text = driver.find_element(By.XPATH, paypal_des).text
        assert text in ['将返利转到PayPal', 'Get Cash Back to PayPal']
        paypal = '//*[@id="__next"]/main/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div'
        driver.find_element(By.XPATH, paypal).click()

        paypal_email = '//*[@id="basic_email"]'
        driver.find_element(By.XPATH, paypal_email).send_keys('yinapsc30@gmail.com')
        # paypal_button = '//*[@id="basic"]/div[2]/div/div/div/div/div/button[2]'
        # driver.find_element(By.XPATH, paypal_button).click()
        back_button = '//*[@id="basic"]/div[2]/div/div/div/div/div/button[1]'
        driver.find_element(By.XPATH, back_button).click()

    def tearDown(self):
        driver = self.driver
        driver.quit()


if __name__ == '__main__':
    unittest.main()
