import itertools
import re
import time
from src.utils.elementoperator import BasePage
from selenium.webdriver.common.by import By
from src.page_element.WithdrawPageEle import WithdrawElement
from src.utils.sqloperator import execute_sql


class WithdrawPageOperation(BasePage):

    def open_url(self, url):
        self.get_url(url)

    def implicitly_wait(self, times=30):
        self.driver.implicitly_wait(times)

    def withdraw_money(self):
        self.logger.info("--进入Withdraw Money--")
        time.sleep(30)
        self.wait_eleVisible(WithdrawElement.WITHDRAW_MONEY)
        self.click_element(WithdrawElement.WITHDRAW_MONEY, model='Withdraw Money')

    def check_balance(self):
        self.logger.info("--获取提现前余额--")
        balances = self.get_text(WithdrawElement.BALANCE, model='余额')
        balances = float(balances.strip('$'))
        return balances

    def entry_withdraw_process(self):
        self.logger.info("--点击开始提现按钮--")
        self.click_element(WithdrawElement.WITHDRAW_BUTTON, model='开始提现按钮')
        time.sleep(1)

    def get_account_email(self):
        email = self.get_text(WithdrawElement.ACCOUNT_EMAIL, model='账号邮箱')
        self.logger.info(f"--当前账号邮箱为：{email}")
        return email

    '------------------------------PayPal提现----------------------------------'

    def select_paypal(self):
        self.logger.info("--选择PayPal提现--")
        self.click_element(WithdrawElement.PAYPAL_ENTRY, model='PayPal提现')
        time.sleep(1)

    def check_paypal_email(self):
        ...

    def click_confirm_check(self, paypal_email=None):
        self.logger.info("--判断是否已绑定paypal邮箱--")
        flag = self.elements_is_exists(WithdrawElement.PAYPAL_CHANGE_CHECK, model='判断是否存在Paypal账号')
        if flag:
            self.logger.info("--点击PayPal账号确认单选框--")
            self.click_element(WithdrawElement.PAYPAL_CHECKBOX, model='确认单选框')
        else:
            self.input_text(WithdrawElement.INPUT_PAYPAL_EMAIL, paypal_email, model='输入Paypal账号')
            self.logger.info("--点击PayPal账号确认单选框--")
            self.click_element(WithdrawElement.PAYPAL_CHECKBOX, model='确认单选框')

    def click_next_button(self):
        self.logger.info("--点击下一步，进入验证码页面--")
        self.click_element(WithdrawElement.NEXT_BUTTON, model='下一步')

    def success_text(self):
        message = self.get_text(WithdrawElement.SUCCESS_TEXT, model='成功弹窗')
        self.logger.info("--体现成功弹窗信息--")
        return message

    def success_pop_button(self, success_text):
        if success_text:
            self.logger.info("--点击弹窗按钮")
            self.click_element(WithdrawElement.SUCCESS_BUTTON, model='弹窗按钮')
        else:
            self.open_url('https://www.coupert.com/user/withdraw')

    '------------------------------礼品卡提现----------------------------------'

    def select_giftcard(self):
        self.logger.info("--选择礼品卡提现--")
        self.click_element(WithdrawElement.GIFTCARD_ENTRY, model='礼品卡提现')
        time.sleep(1)

    def choose_country(self):
        self.logger.info("--选择国家-美国--")
        self.click_element(WithdrawElement.CHOOSE_COUNTRY, model='选择国家')
        time.sleep(1)
        self.move_to_click(WithdrawElement.US, model='美国')
        time.sleep(1)

    def choose_giftcard(self):
        self.logger.info("--选择礼品卡商家-AMAZON--")
        self.click_element(WithdrawElement.AMAZON, model='AMAZON')
        time.sleep(0.5)

    def click_giftcard_checkbox(self):
        self.logger.info("--点击确认单选框--")
        self.click_element(WithdrawElement.GIFTCARD_TIPS_CHECKBOX, model='礼品卡确认')

    def click_next_giftcard(self):
        self.logger.info("--点击下一步--")
        self.click_element(WithdrawElement.SELECT_NEXT_BUTTON, model='下一步')

    '------------------------------最终提现页面----------------------------------'

    def get_code_email(self):
        email = self.get_text(WithdrawElement.WITHDRAW_EMAIL, model='验证码邮箱')
        self.logger.info(f"--获取收验证码的邮箱：{email}--")
        return email

    def click_verify_code_button(self):
        self.logger.info("--点击发送验证码--")
        self.click_element(WithdrawElement.SEND_VERIFY_CODE_BUTTON, model='发送验证码')
        time.sleep(3)

    def get_verify_code_from_db(self, email):
        self.logger.info(f"--查询{email}收到的验证码--")
        try:
            sql = f"SELECT code FROM user_verification_code where type='withdraw' and email={email};"
            result = execute_sql(sql)
            # 通过正则获取验证码
            pattern = re.compile(r"'code'\s*:\s*'(\w+)'")
            text = re.search(pattern, str(result))
            if text:
                code = text.group(1)
                return code
        except Exception as e:
            self.logger.info(f"--未查询到验证码，报错信息：{e}--")

    def input_verify_code(self, code):
        self.logger.info(f"--输入验证码:{code}--")
        self.input_text(WithdrawElement.VERIFY_CODE_INPUT, code, model='输入验证码')

    def click_withdraw_button(self):
        self.logger.info("--点击提现按钮--")
        self.click_element(WithdrawElement.WITHDRAW_CONFIRM_BUTTON, model='提现按钮')
        time.sleep(1)

    def get_verify_wrong_text(self):
        text = self.get_text(WithdrawElement.VERIFY_WRONG_TEXT, model='错误验证码提示文案')
        self.logger.info(f"--获取错误验证码文案:{text}--")
        return text
