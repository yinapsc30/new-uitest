import itertools
import re
import time
from src.utils.elementoperator import BasePage
from selenium.webdriver.common.by import By
from src.page_element.MyAccountPageEle import MyAccountElement
from src.utils.sqloperator import execute_sql


class GoldOrderDetailPageOperation(BasePage):

    def open_url(self, url):
        self.get_url(url)

    '------------------------------Gold & Rewards----------------------------------'
    def check_gold_rewards_title(self):
        pass

    def check_cash_back_gold(self):
        pass

    def check_task_gold(self):
        pass

    '--------------------------------Gold Detail--------------------------------'
    def check_gold_detail_title(self):
        pass

    def check_gold_detail_link(self):
        pass

    def input_merchant(self, merchant):
        pass

    def click_detail_query(self):
        pass

    def check_query_result(self):
        pass

    def click_detail_button(self):
        pass

    def check_detail_box_text(self):
        pass

    def click_appeal_link(self):
        pass

    def check_detail_appeal_page_title(self):
        pass

    '--------------------------------Appeal List--------------------------------'
    def check_appeal_list_title(self):
        pass

    def select_domain(self):
        pass

    def click_appeal_query(self):
        pass

    def check_appeal_query_result(self):
        pass
