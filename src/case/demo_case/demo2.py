import itertools
import time
import unittest

import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains as AC


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
        self.firefox_services = Service(executable_path='firefoxdriver', port=3000,
                                        service_args=['--marionette-port', '2828', '--connect-existing'])
        self.driver = webdriver.Firefox(service=self.firefox_services)
        # self.driver = webdriver.Chrome()
        self.actions = ActionChains(self.driver)
        self.driver.implicitly_wait(100)
        # self.driver = webdriver.Firefox(executable_path=self.firefox_driver, options=self.options)

    def test_smokeing(self):
        driver = self.driver
        # driver.get('https://www.coupert.com/user/login')
        # time.sleep(30)
        # driver.get('https://www.coupert.com/user/account')
        driver.get('https://www.coupert.com/user/task')
        driver.implicitly_wait(100)

        # driver.find_element_by_xpath('//*[@id="__next"]/div/div/main/div[2]/div[2]/div/div[3]/div/div/div/div/input')
        # task_center = '//*[@id="userMenus"]/li[4]/span/div'
        # driver.find_element(By.XPATH, task_center).click()
        # self.driver.implicitly_wait(10)

        gold = '//*[@id="__next"]/main/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/span[2]'
        golds = driver.find_element(By.XPATH, gold).text
        golds = int(golds.strip())
        print(golds)
        #
        # # check_icon = '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div[2]/div[2]/div/ul/li[1]'
        # # loc = driver.find_element(By.XPATH, check_icon)
        # check_icon = 'task_checkinItem__w7eiV'
        # loc = driver.find_elements(By.CLASS_NAME, check_icon)
        # print(loc)
        # driver.implicitly_wait(10)
        # for i in range(7):
        #     loc[i].click()
        #     time.sleep(0.5)
        #
        # golds_new = driver.find_element(By.XPATH, gold).text
        # golds_new = int(golds_new.strip())
        # print(golds_new)
        # sss = '/html/body/div/main/div/div[2]/div[2]/div[2]/div[2]/div[10]/div[1]/div[1]/span[1]'
        # tasks = 'jsx-320462669 task_listItem__Kujxn'
        # ele = driver.find_element(By.XPATH, sss)
        # driver.execute_script("arguments[0].scrollIntoView();", ele)
        # task_list_eles = driver.find_elements(By.CLASS_NAME, tasks)
        check_icon = 'task_checkinItem__w7eiV'
        locs = driver.find_elements(By.CLASS_NAME, check_icon)
        days = {'day 1': 10, 'day 2': 30, 'day 3': 15, 'day 4': 20, 'day 5': 25, 'day 6': 30, 'day 7': 35}
        loc_list = []
        for loc in locs:
            res = loc.get_attribute('innerText')
            loc_list.append(res)
        res = list(list(itertools.chain.from_iterable(loc_list[i].split('\n') for i in range(len(loc_list)))))
        print(res)
        today = "".join(set(list(days.keys())).difference(res))
        print(today)

        task_list_eles = driver.execute_script(
            "return document.getElementsByClassName('jsx-320462669 task_listItem__Kujxn')")
        print(task_list_eles)
        task_list = []
        for task in task_list_eles:
            res = task.get_attribute('innerText')
            # res = task.innerText
            res = res.split('\n')
            task_list.append(res)
        print(task_list)

        assert 1 == 1

        # driver.get_screenshot_as_file("coupert.png")
        # el=driver.find_element_by_xpath("//a[contains(text(),'返利如何运')]")
        # print(el)

    def test_withdraw(self):
        driver = self.driver
        # driver.get('https://www.coupert.com/user/withdraw')
        driver.get('https://www.coupert.com/user/withdraw_money?source=web')
        driver.implicitly_wait(100)

        # balance = '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div/div[2]/div[1]/span'
        # balances = driver.find_element(By.XPATH, balance).text
        # balances = float(balances.strip('$'))
        # print(balances)

        withdraw_button = '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div'
        # driver.find_element(By.XPATH, withdraw_button).click()

        time.sleep(1)
        paypal = '/html/body/div/main/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div'
        loc = driver.find_element(By.XPATH, paypal)
        # js = f"document.evaluate('{paypal}', document).iterateNext().click();"
        # print(js)
        loc.click()

        PAYPAL_CHECKBOX = '//*[@id="basic"]/p[2]/input'
        driver.find_element(By.XPATH, PAYPAL_CHECKBOX).click()

        click_next_button = '//*[@id="basic"]/div[2]/div/div/div/div/div/button[2]'
        driver.find_element(By.XPATH, click_next_button).click()

        WITHDRAW_EMAIL = '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[2]/div/div[2]/p/span'
        email = driver.find_element(By.XPATH, WITHDRAW_EMAIL).text
        print(email)

        SEND_VERIFY_CODE_BUTTON = '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[2]/div/div[2]/div/button'
        driver.find_element(By.XPATH, SEND_VERIFY_CODE_BUTTON).click()

        VERIFY_CODE_INPUT = '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[2]/div/div[2]/div/input'
        driver.find_element(By.XPATH, VERIFY_CODE_INPUT).send_keys(1234)

        WITHDRAW_BACK_BUTTON = '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[2]/div/div[3]/button[1]'
        driver.find_element(By.XPATH, WITHDRAW_BACK_BUTTON).click()

    def test_gift_card(self):
        driver = self.driver
        # driver.get('https://www.coupert.com/user/withdraw')
        driver.get('https://www.coupert.com/user/withdraw_money?wpage=2')
        driver.implicitly_wait(100)

        # 选择国家
        CHOOSE_COUNTRY = '//*[@id="rc_select_2"]'
        US = '//*[@id="__countryChooseSelect"]/div[2]/div/div/div/div/ul/li[1]'
        # 选择礼品卡
        AMAZON = '//*[@id="__next"]/main/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/dl[1]/dt'
        check = '//*[@id="__next"]/main/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/div/div/div/p/input'
        next_button = '//*[@id="__next"]/main/div/div[2]/div[2]/div[2]/div[2]/div/div[4]/button[2]'

        driver.find_element(By.XPATH, CHOOSE_COUNTRY).click()
        time.sleep(1)
        country = driver.find_element(By.XPATH, US)
        AC(driver).move_to_element(country).click().perform()
        time.sleep(1)
        driver.find_element(By.XPATH, AMAZON).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, check).click()
        driver.find_element(By.XPATH, next_button).click()

    def test_account(self):
        driver = self.driver

        driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div/div[3]/a').click()
        current = driver.current_window_handle
        print("current1：", current)
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])
        link = driver.current_url
        print("link：", link)
        text = driver.find_element(By.XPATH, '//*[@id="post-379"]/footer[1]/h1').text
        print("text:", text)
        time.sleep(3)
        driver.close()
        driver.switch_to.window(current)
        current = driver.current_window_handle
        print("current2:", current)

        balance = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div/div[2]/div[1]/span').text
        print("balance:", balance)
        driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div/div[3]/i').click()
        text = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div/div[4]/div/div/div/div/div/table/tbody/tr[1]/td[3]').text
        print("text:", text)

        assert balance == text  # pass

        ele = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[1]')
        # ele = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[4]/div[1]')
        driver.execute_script("arguments[0].scrollIntoView();", ele)
        text = ele.text
        print("text:", text)

        eles = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[2]')
        # for i in eles:
        #     text = i.text
        #     print("text:", text.split('\n'))
        b = len([i.text.split('\n') for i in eles][0])
        assert len([i for i in eles]) // 3 == 0

        # text = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[2]/a[1]').text
        # print("text:", text.split('\n'))

    def test_baidu(self):
        driver = self.driver
        driver.get("https://www.baidu.com/")
        driver.get_screenshot_as_file("baidu.png")
        el = driver.find_element(By.XPATH, "//input[@id='su']").get_attribute('value')
        print(el)

    def test_withdrawss(self):
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
