import itertools
import re
import time
from src.utils.elementoperator import BasePage
from selenium.webdriver.common.by import By
from src.page_element.GoldOrderDetailPageEle import GoldOrderDetailElement
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
        self.logger.info('点击query按钮，查询筛选结果')
        self.click_element(GoldOrderDetailElement.APPEAL_QUERY_BUTTON, model='query按钮')
        self.implicitly_wait_second(3)

    def check_appeal_query_result(self):
        self.logger.info('')
        text = self.get_text(GoldOrderDetailElement.DOMAIN_TEXT, model='domain')
        return text
