import itertools
import re
import time
from src.utils.elementoperator import BasePage
from selenium.webdriver.common.by import By
from src.page_element.MyAccountPageEle import MyAccountElement
from src.utils.sqloperator import execute_sql


class MyAccountPageOperation(BasePage):

    def open_url(self, url):
        self.get_url(url)

    '------------------------------My Cash Back Account----------------------------------'

    def get_account_title(self):
        self.logger.info("--进入My Cash Back Account--")
        text = self.get_text(MyAccountElement.ACCOUNT, model="Account页面title")
        return text

    def get_balance(self):
        self.logger.info("--获取当前账户Balance--")
        text = self.get_text(MyAccountElement.BALANCE, model="Balance")
        return text

    def check_balance_tips(self):
        self.logger.info("--检查余额TIPS--")
        flag = self.elements_is_exists(MyAccountElement.BALANCE_TIPS, model="余额TIPS")
        return flag

    def click_balance_tips_link(self):
        pass

    def get_withdrawable(self):
        self.logger.info("--获取当前账户withdrawable--")
        text = self.get_text(MyAccountElement.WITHDRAWABLE, model="withdrawable")
        return text

    def withdraw_button(self):
        self.logger.info("--判断提现按钮可点击--")
        flag = self.ele_is_enabled(MyAccountElement.WITHDRAW_BUTTON, model="提现按钮")
        return flag

    def check_withdrawable_tips(self):
        self.logger.info("--检查提现额度TIPS--")
        flag = self.elements_is_exists(MyAccountElement.WITHDRAWABLE_TIPS, model="提现额度TIPS")
        return flag

    def click_withdrawable_tips_link(self):
        pass

    def click_balance_help_link(self):
        self.logger.info("--点击Gold received but balance not updating?链接，检查跳转是否正常--")
        handle = self.get_current_handle()
        self.click_element(MyAccountElement.BALANCE_HELP_LINK, model="Gold received but balance not updating?链接")
        self.switch_window('new')
        text = self.get_text(MyAccountElement.HELP_LINK_TEXT, model="help页面title")
        link = self.get_current_link()
        self.close_page()
        self.switch_window(handle)
        return text, link

    def click_view_balance_history(self):
        self.logger.info("--检查余额历史表单是否正常--")
        self.click_element(MyAccountElement.BALANCE_HISTORY, model="余额历史表单")
        balance = self.get_text(MyAccountElement.BALANCE_HISTORY_DETAIL, model="表单信息中最新余额")
        return balance

    '--------------------------------Recommended Stores--------------------------------'

    def move_to_recommended_title(self):
        self.logger.info("滑动页面到Recommended模块，并获取title")
        self.scroll_page_to_element_visible(MyAccountElement.RECOMMENDED, model="Recommended模块")
        text = self.get_text(MyAccountElement.RECOMMENDED, model="recommended模块title")
        return text

    def check_cb_not_null(self):
        self.logger.info("查看Recommended商家的cb rate是否正常")
        eles = self.find_elements(MyAccountElement.RECOMMENDED_STORES, model="Recommended Stores")
        res = [i.text.split('\n') for i in eles][0]
        return res

    '--------------------------------My Cash Back Activation Record--------------------------------'

    def get_active_record_title(self):
        self.logger.info("获取Activation Record模块title")
        text = self.get_text(MyAccountElement.CASHBACK_RECORD, model="Activation Record模块title")
        return text

    def check_active_record_tips(self):
        self.logger.info("--Activation Record模块title旁TIPS--")
        flag = self.elements_is_exists(MyAccountElement.CASHBACK_RECORD_TIPS, model="Activation Record模块TIPS")
        return flag

    def click_active_record_tips_link(self):
        pass

    def check_active_record(self):
        pass

    '--------------------------------Exclusive Offers--------------------------------'

    def move_to_exclusive_offers_title(self):
        self.logger.info("滑动页面到Exclusive Offers模块，并获取title")
        self.scroll_page_to_element_visible(MyAccountElement.EXCLUSIVE, model="Exclusive Offers模块")
        text = self.get_text(MyAccountElement.EXCLUSIVE, model="Exclusive Offers模块title")
        return text

    def check_offers_status(self):
        self.logger.info("查看Exclusive Offers模块的offers是否正常")
        eles = self.find_elements(MyAccountElement.EXCLUSIVE_OFFERS, model="Exclusive Offers")
        res = [i.text.split('\n') for i in eles][0]
        return res

    def click_shop_now(self):
        pass