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
    def check_account_title(self):
        pass

    def check_balacne(self):
        pass

    def check_balance_tips(self):
        pass

    def click_balance_tips_link(self):
        pass

    def check_withdrawable(self):
        pass

    def withdrawable_button(self):
        pass

    def check_withdrawable_tips(self):
        pass

    def click_withdrawable_tips_link(self):
        pass

    def click_balance_help_link(self):
        pass

    def click_view_balance_history(self):
        pass

    '--------------------------------Recommended Stores--------------------------------'
    def move_to_recommended_title(self):
        pass

    def check_cb_not_null(self):
        pass

    '--------------------------------My Cash Back Activation Record--------------------------------'
    def move_to_active_record_title(self):
        pass

    def check_active_record_tips(self):
        pass

    def click_active_record_tips_link(self):
        pass

    def check_active_record(self):
        pass

    '--------------------------------Exclusive Offers--------------------------------'
    def move_to_exclusive_offers_title(self):
        pass

    def check_rage_success(self):
        pass

    def check_shop_now(self):
        pass