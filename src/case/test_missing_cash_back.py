import time
import pytest
import allure
from src.utils.constant import IMG_PATH
from src.utils.allureoperator import compose
from src.pages.FindMyMissingCashBackPage import FindMyMissingCashBackPageOperation


class TestFindMyMissingCashBack:

    def __init__(self, drivers):
        self.missing_cashback = FindMyMissingCashBackPageOperation(drivers)

    @compose(feature="Find My Missing Cash Back", story="Missing Cash Back", title='My Missing Cash Back页面正常展示')
    @pytest.mark.MissingCashBack
    def test_mmcb_page_title(self):
        # 获取title
        with allure.step('获取My Missing Cash Back页面title'):
            text = self.missing_cashback.check_mmcb_page_title()
            assert text == 'My Missing Cash Back'
