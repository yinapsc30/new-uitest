import itertools
import time
from src.utils.elementoperator import BasePage
from selenium.webdriver.common.by import By
from src.page_element.LoginEle import LoginElement


class LoginPageOperation(BasePage):

    def input_email(self, email):
        self.logger.info(f"--输入Email:{email}--")
        self.input_text(LoginElement.EMAIL, email, model='输入Email')

    def input_password(self, password):
        self.logger.info(f"--输入Password:{password}--")
        self.input_text(LoginElement.PASSWORD, password, model='输入Password')

    def visible_account_email(self):
        self.logger.info("--判断是否点击登录，页面完成跳转--")
        try:
            self.wait_eleVisible(LoginElement.ACCOUNT_EMAIL, model='判断是否进入个人中心')
        except:
            raise
