import itertools
import re
import time

from selenium.webdriver import Keys

from src.utils.elementoperator import BasePage
from selenium.webdriver.common.by import By
from src.page_element.GoldOrderDetailPageEle import GoldOrderDetailElement
from src.utils.sqloperator import execute_sql


class GoldOrderDetailPageOperation(BasePage):

    def open_url(self, url):
        self.get_url(url)

    '------------------------------Gold & Rewards----------------------------------'
    def check_gold_rewards_title(self):
        self.logger.info("--进入Gold & Rewards Detail--")
        text = self.get_text(GoldOrderDetailElement.GOLD_REWARDS, model="Gold & Rewards Detail页面title")
        return text

    def check_cash_back_gold(self):
        self.logger.info("--检查cash back gold--")
        cb = self.get_text(GoldOrderDetailElement.CASH_BACK_GOLD, model="Cash Back Gold")
        confirmed = self.get_text(GoldOrderDetailElement.CONFIRMED_GOLD, model="Cash Back Confirmed gold")
        pending = self.get_text(GoldOrderDetailElement.PENDING_GOLD, model="Cash Back Pending gold")
        return cb, confirmed, pending

    def check_task_gold(self):
        self.logger.info("--检查task gold--")
        task = self.get_text(GoldOrderDetailElement.TASK_GOLD, model="Task Gold")
        confirmed = self.get_text(GoldOrderDetailElement.CONFIRMED_TASK_GOLD, model="Task Confirmed gold")
        pending = self.get_text(GoldOrderDetailElement.PENDING_TASK_GOLD, model="Task Pending gold")
        return task, confirmed, pending

    '--------------------------------Gold Detail--------------------------------'
    def check_gold_detail_title(self):
        self.logger.info("--进入Gold & Rewards Detail--")
        text = self.get_text(GoldOrderDetailElement.GOLD_REWARDS, model="Gold & Rewards Detail页面title")
        return text

    def check_gold_detail_link(self):
        self.logger.info("--点击Gold received but balance not updating?链接，检查跳转是否正常--")
        handle = self.get_current_handle()
        self.click_element(GoldOrderDetailElement.GOLD_DETAIL_LINK, model="Gold received but balance not updating?链接")
        self.switch_window('new')
        text = self.get_text(GoldOrderDetailElement.HELP_PAGE_TITLE, model="help页面title")
        link = self.get_current_link()
        self.close_page()
        self.switch_window(handle)
        return text, link

    def input_merchant(self, merchant):
        self.logger.info("--Gold Detail筛选栏输入商家domain--")
        ele = self.find_element(GoldOrderDetailElement.MERCHANT_INPUT)
        ele.send_keys(merchant)
        ele.send_keys(Keys.ENTER)
        time.sleep(1)
        self.click_element(GoldOrderDetailElement.DETAIL_QUERY_BUTTON)
        time.sleep(1)
        domain = self.get_text(GoldOrderDetailElement.MERCHANT_TEXT)
        return domain

    def click_detail_query(self):
        self.logger.info("点击query按钮")
        self.click_element(GoldOrderDetailElement.DETAIL_QUERY_BUTTON, model="query按钮")
        self.implicitly_wait_second(3)

    def check_query_result(self):
        self.logger.info('查询结果中的domain')
        res = self.get_text(GoldOrderDetailElement.MERCHANT_TEXT, model="查询结果domain")
        return res

    def click_detail_button(self):
        self.logger.info('点击detail按钮')
        self.click_element(GoldOrderDetailElement.DETAIL_BUTTON, model='query按钮')
        self.implicitly_wait_second(3)

    def check_detail_box_text(self):
        self.logger.info('查看detail弹框底部tips')
        text = self.get_text(GoldOrderDetailElement.DETAIL_BOX_TEXT, model='弹框底部tips')
        return text

    def click_appeal_link(self):
        self.logger.info("发起金币申诉")
        self.click_element(GoldOrderDetailElement.APPEAL_LINK, model='金币申诉')
        self.implicitly_wait_second(10)

    def check_appeal_page_title(self):
        self.logger.info("检查金币申诉页面title")
        text = self.get_text(GoldOrderDetailElement.SUBMIT_PAGE_TITLE, model='Gold Appeal页面title')
        return text

    def check_appeal_page_tips(self):
        self.logger.info("检查金币申诉页面tips内容")
        text = self.get_text(GoldOrderDetailElement.SUBMIT_PAGE_TIPS, model='Gold Appeal页面tips')
        return text

    def input_appeal_event(self, issue):
        self.logger.info(f"输入Appeal Event内容:{issue}")
        pass

    def upload_order_img(self, img):
        self.logger.info(f"上传订单图片:{img}")
        self.upload_file(GoldOrderDetailElement.ADD_IMG_UPLOAD, img, model='上传图片')

    def input_comments(self, text):
        self.logger.info(f"输入comment内容:{text}")
        self.input_text(GoldOrderDetailElement.COMMENTS_TEXTAREA, text, model='comment输入框')

    def click_submit(self):
        self.logger.info(f"点击submit按钮，提交appeal")
        self.click_element(GoldOrderDetailElement.SUBMIT_BUTTON, model='submit按钮')

    def check_appealed(self):
        self.logger.info(f"查看申诉后appeal状态是否变化")
        text = self.get_text(GoldOrderDetailElement.APPEAL_LINK, model='appealed')
        return text

    '--------------------------------Appeal List--------------------------------'

    def move_to_appeal_list_title(self):
        self.logger.info("滑动页面到Appeal List模块，并获取title")
        self.scroll_page_to_element_visible(GoldOrderDetailElement.APPEAL_LIST, model="Appeal List模块")
        text = self.get_text(GoldOrderDetailElement.APPEAL_LIST, model="Appeal List模块title")
        return text

    def select_domain(self):
        pass

    def click_appeal_query(self):
        self.logger.info('点击query按钮')
        self.click_element(GoldOrderDetailElement.APPEAL_QUERY_BUTTON, model='query按钮')
        self.implicitly_wait_second(3)

    def check_appeal_query_result(self):
        self.logger.info('查看查询结果是否一致')
        text = self.get_text(GoldOrderDetailElement.DOMAIN_TEXT, model='domain')
        return text