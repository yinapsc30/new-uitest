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