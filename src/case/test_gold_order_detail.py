import time
import pytest
import allure
from src.utils.constant import IMG_PATH
from src.utils.allureoperator import compose
from src.pages.GoldOrderDetailPage import GoldOrderDetailPageOperation


class TestMyAccount:

    def __init__(self, drivers):
        self.gold_order = GoldOrderDetailPageOperation(drivers)

    @compose(feature="Gold&Order Detail", story="Gold&Order", title='Gold&Order Detail页面正常展示')
    @pytest.mark.GoldOrderDetail
    def test_detail_page_title(self):
        # 获取title
        with allure.step('获取Gold&Order Detail页面title'):
            text = self.gold_order.check_gold_rewards_title()
            assert text == 'Gold & Rewards'

    @compose(feature="Gold&Order Detail", story="Gold&Order", title='Gold&Order Detail页面正常展示')
    @pytest.mark.GoldOrderDetail
    def test_balance_tips(self):
        ...

    @compose(feature="Gold&Order Detail", story="Gold&Order", title='Gold&Order申诉页面正常展示')
    @pytest.mark.GoldOrderDetail
    def test_gold_order_appeal_title(self):
        # Gold&Order申诉页面正常展示
        with allure.step('Gold&Order申诉页面正常展示'):
            self.gold_order.click_appeal_link()
            text = self.gold_order.check_appeal_page_title()
            assert text == 'Submit Appeal'

    @compose(feature="Gold&Order Detail", story="Gold&Order", title='检查金币申诉页面tips内容')
    @pytest.mark.GoldOrderDetail
    def test_appeal_tips(self):
        # 金币申诉页面顶部tips内容
        with allure.step('检查金币申诉页面tips内容'):
            text = self.gold_order.check_appeal_page_tips()
            assert text == 'If you disagree with the reason for the change of Gold, please submit a ticket and we ' \
                           'will process your request within 1-7 business days. '

    @compose(feature="Gold&Order Detail", story="Gold&Order", title='提交一次金币申诉')
    @pytest.mark.GoldOrderDetail
    def test_appeal_tips(self):
        # 提交一次金币申诉
        url = self.gold_order.get_current_url()
        gold_appeal_path = '/user/appeal_commit?id='
        if gold_appeal_path not in gold_appeal_path:
            self.gold_order.open_url('https://www.coupert.com/user/gold-order')
            self.gold_order.click_appeal_link()
        with allure.step('提交一次金币申诉'):
            self.gold_order.input_appeal_event('')
            self.gold_order.upload_order_img(IMG_PATH + r'\Paypal.png')
            self.gold_order.input_comments('test case for verify appeal submit')
            self.gold_order.click_submit()
            time.sleep(3)
            text = self.gold_order.check_appealed()
            assert text == 'Appealed'

    @compose(feature="Gold&Order Detail", story="Gold&Order", title='检查Appeal List模块title内容')
    @pytest.mark.GoldOrderDetail
    def test_appeal_list_title(self):
        # 检查Appeal List模块title内容
        with allure.step('检查Appeal List模块title内容'):
            text = self.gold_order.move_to_appeal_list_title()
            assert text == 'Appeal List'

    @compose(feature="Gold&Order Detail", story="Gold&Order", title='筛选Appeal List内容')
    @pytest.mark.GoldOrderDetail
    def test_appeal_list_title(self):
        # 筛选Appeal List内容
        with allure.step('筛选Appeal List内容'):
            query_domain = 'shein.com'
            self.gold_order.select_domain()
            self.gold_order.click_appeal_query()
            domain = self.gold_order.check_appeal_query_result()
<<<<<<< HEAD
            assert domain == query_domain
=======
            assert domain == query_domain
>>>>>>> cbc35016a7dc6b0d4a26f80f2d5056b3e60f5091
