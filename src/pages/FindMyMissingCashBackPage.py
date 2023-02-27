import itertools
import re
import time

from selenium.webdriver import Keys

from src.utils.elementoperator import BasePage
from selenium.webdriver.common.by import By
from src.page_element.FindMyMissingCashBackPageEle import FindMyMissingCashBackElement
from src.utils.sqloperator import execute_sql
from src.utils.timeoperator import timeoperator
from config.config_init import Email, PassWord


class FindMyMissingCashBackPageOperation(BasePage):

    def open_url(self, url):
        self.get_url(url)

    def get_current_url(self):
        link = self.get_current_link()
        return link

    '------------------------------My Missing Cash Back----------------------------------'

    def check_mmcb_page_title(self):
        self.logger.info("进入Find My Missing Cash Back页面，检查页面title")
        text = self.get_text(FindMyMissingCashBackElement.MY_MISSING_CASH_BACK_TITLE,
                             model="My Missing Cash Back页面title")
        return text

    def check_mmcb_decscription(self):
        self.logger.info("检查My Missing Cash Back模块描述")
        text = self.get_text(FindMyMissingCashBackElement.MMCB_DESC, model="My Missing Cash Back模块描述")
        return text

    def click_mmcb_button(self):
        self.logger.info("点击提交My Missing Cash Back按钮")
        self.click_element(FindMyMissingCashBackElement.SUBMIT_BUTTON, model="Find My MissingCashBack提交按钮")
        self.implicitly_wait_second(10)

    '------------------------------Missing Cash Back----------------------------------'

    def check_mcb_title(self):
        self.logger.info("检查Missing Cash Back页面title")
        text = self.get_text(FindMyMissingCashBackElement.MCB_TITLE, model="Missing Cash Back页面title")
        return text

    def check_mcb_notice(self):
        self.logger.info("检查Missing Cash Back页面notice")
        text = self.get_text(FindMyMissingCashBackElement.MCB_NOTICE, model="Missing Cash Back页面notice")
        return text

    def input_stores(self, domain):
        self.logger.info(f"输入Stores：{domain}")
        self.input_text(FindMyMissingCashBackElement.MCB_STORES_INPUT, domain, model="Stores输入框")

    def input_order_date(self, date):
        self.logger.info(f"输入Order Date：{date}")
        date_picker = self.input_text(FindMyMissingCashBackElement.MCB_ORDER_DATE_INPUT, date, model="Order Date输入框")
        date = timeoperator.now2
        script = f"arguments[0].value='{date}';"
        self.execute_script(script, date_picker)

    def input_order_number(self, number):
        self.logger.info(f"输入Order Number：{number}")
        self.input_text(FindMyMissingCashBackElement.MCB_ORDER_NUMBER_INPUT, number, model="Order Number输入框")

    def input_order_subtotal(self, num):
        self.logger.info(f"输入Order Subtotal：{num}")
        self.input_text(FindMyMissingCashBackElement.MCB_ORDER_SUBTOTAL_INPUT, num, model="Order Subtotal输入框")

    def input_img_path(self, img):
        self.logger.info(f"上传Profile Attach：{img}")
        self.input_text(FindMyMissingCashBackElement.MCB_PROFILE_ATTACH_INPUT, img, model="上传Profile Attach")

    def input_comments(self, content):
        self.logger.info(f"输入Comments：{content}")
        self.input_text(FindMyMissingCashBackElement.MCB_COMMENTS, content, model="输入Comments")

    def check_button_text(self):
        self.logger.info("检查按钮上的文案")
        text = self.get_text(FindMyMissingCashBackElement.MCB_BUTTON_TEXT, model="按钮文案")
        return text

    def click_fmcb_button(self):
        self.logger.info("点击Find My Cash Back按钮")
        self.click_element(FindMyMissingCashBackElement.MCB_SUBMIT_BUTTON, model="Find My Cash Back按钮")

    def get_mcb_record_id(self):
        self.logger.info("获取mcb提交记录ID")
        sql = f"SELECT id from user_missing_cashback_record where user_email = '{Email}' ORDER BY submit_time Desc LIMIT 1;"
        re_path = f"'id':\s*(\d+)"
        res = self.execute_sql_re_for_result(sql, re_path)
        return res

    def check_mcb_record_status(self):
        self.logger.info("检查missing cash back提交状态")
        ...

    """--------------------------------Missing Cash Back History--------------------------------"""

    def check_history_title(self):
        self.logger.info("检查Missing Cash Back History页面title")
        text = self.get_text(FindMyMissingCashBackElement.MISSING_CASH_BACK_HISTORY_TITLE,
                             model="Missing Cash Back History页面title")
        return text

    def input_domain(self, domain):
        self.logger.info(f"输入domain:{domain}")
        self.input_text(FindMyMissingCashBackElement.DOMAIN_INPUT, domain, model="domain输入框")

    def click_query(self):
        self.logger.info(f"点击query按钮")
        self.click_element(FindMyMissingCashBackElement.QUERY_BUTTON, model="query按钮")
        self.implicitly_wait_second(10)

    def get_history_record_id(self):
        self.logger.info(f"获取历史记录中的记录ID")
        self.get_text(FindMyMissingCashBackElement.MCB_ID, model="获取id")

    def get_history_record_domain(self):
        self.logger.info(f"获取历史记录中的记录domain")
        self.get_text(FindMyMissingCashBackElement.QUERY_DOMAIN, model="获取domain")

    def click_view_details_button(self):
        self.logger.info(f"点击View details按钮")
        self.click_element(FindMyMissingCashBackElement.VIEW_DETAIL, model="viewDetails")

    """--------------------------------Missing Cash Back Result--------------------------------"""

    def result_page_title(self):
        self.logger.info(f"获取Missing Cash Back Result页面title")
        text = self.get_text(FindMyMissingCashBackElement.RESULT_TITLE, model="Missing Cash Back Result页面title")
        return text

    def result_notice(self):
        self.logger.info(f"获取Missing Cash Back Result页面notice")
        text = self.get_text(FindMyMissingCashBackElement.RESULT_NOTICE_TEXT, model="Missing Cash Back Result页面notice")
        return text

    def result_stores(self):
        self.logger.info(f"获取Stores")
        text = self.get_text(FindMyMissingCashBackElement.RESULT_STORES, model="Stores")
        return text

    def result_order_date(self):
        self.logger.info(f"获取Order Date")
        text = self.get_text(FindMyMissingCashBackElement.RESULT_ORDER_DATE, model="Order Date")
        return text

    def result_order_number(self):
        self.logger.info(f"获取Order Number")
        text = self.get_text(FindMyMissingCashBackElement.RESULT_ORDER_NUMBER, model="Order Number")
        return text

    def result_order_subtotal(self):
        self.logger.info(f"获取Order Subtotal")
        text = self.get_text(FindMyMissingCashBackElement.RESULT_ORDER_SUBTOTAL, model="Order Subtotal")
        return text

    def result_comments(self):
        self.logger.info(f"获取Comments")
        text = self.get_text(FindMyMissingCashBackElement.RESULT_ORDER_COMMENTS, model="Comments")
        return text

    def get_history_record(self, rid):
        self.logger.info(f"获取id为{rid}的记录在数据库中的参数")
        sql = f"SELECT * from user_missing_cashback_record where id = {rid};"
        res = self.execute_sql_re_for_result(sql)
        domain = res[0]['Domain']
        order_time = res[0]['order_time']
        order_number = res[0]['OrderNumber']
        order_subtotal = res[0]['OrderSubtotal']
        comments = res[0]['Comments']
        return domain, order_time, order_number, order_subtotal, comments







