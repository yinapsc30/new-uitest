import time
import pytest
import allure
from src.utils.constant import IMG_PATH
from src.utils.allureoperator import compose
from src.pages.FindMyMissingCashBackPage import FindMyMissingCashBackPageOperation
from src.utils.timeoperator import timeoperator


class TestFindMyMissingCashBack:

    def __init__(self, drivers):
        self.missing_cashback = FindMyMissingCashBackPageOperation(drivers)

    @compose(feature="Find My Missing Cash Back", story="Missing Cash Back", title='My Missing Cash Back页面正常展示')
    @pytest.mark.MissingCashBack
    def test_mmcb_page_title(self):
        with allure.step('获取My Missing Cash Back页面title'):
            text = self.missing_cashback.check_mmcb_page_title()
            assert text == 'My Missing Cash Back'

    @compose(feature="Find My Missing Cash Back", story="Missing Cash Back", title='页面description正常展示')
    @pytest.mark.MissingCashBack
    def test_mmcb_page_description(self):
        with allure.step('获取My Missing Cash Back页面description'):
            text = self.missing_cashback.check_mmcb_description()
            assert text == 'Cash Back Gold will be added when Coupert receives order information from stores, ' \
                           'usually within 2-3 days. Don’t see Cash Back in your account after 3 days? Let’s figure it out. '

    @compose(feature="Find My Missing Cash Back", story="Missing Cash Back", title='检查Missing Cash Back页面title')
    @pytest.mark.MissingCashBack
    def test_mcb_title(self):
        with allure.step('点击SUBMIT按钮，进入Missing Cash Back页面'):
            self.missing_cashback.click_mmcb_button()
            text = self.missing_cashback.check_mcb_title()
            assert text == 'Missing Cash Back'

    @compose(feature="Find My Missing Cash Back", story="Missing Cash Back", title='检查Missing Cash Back页面notice')
    @pytest.mark.MissingCashBack
    def test_mcb_title(self):
        with allure.step('检查Missing Cash Back页面notice'):
            text = self.missing_cashback.check_mcb_notice()
            assert text == 'Please notice that if the following conditions exist, your Cash Back my be lost '

    @compose(feature="Find My Missing Cash Back", story="Missing Cash Back", title='正常提交MCB记录')
    @pytest.mark.MissingCashBack
    def test_submit_mcb_record(self):
        date = timeoperator.now2
        with allure.step('输入表单信息'):
            self.missing_cashback.input_stores('shein.com')
            self.missing_cashback.input_order_date(date)
            self.missing_cashback.input_order_number('123456789')
            self.missing_cashback.input_order_subtotal('10')
            self.missing_cashback.input_img_path(IMG_PATH + '/Paypal.png')
            self.missing_cashback.input_comments('test message')
        with allure.step('点击提交按钮，并获取记录id'):
            self.missing_cashback.click_fmcb_button()
            re_date = self.missing_cashback.get_mcb_record_id()[1]
            assert date == re_date

    @compose(feature="Find My Missing Cash Back", story="Missing Cash Back", title='检查Missing Cash Back History页面title')
    @pytest.mark.MissingCashBack
    def test_mcb_title(self):
        with allure.step('检查Missing Cash Back History页面title'):
            if 'commit' in self.missing_cashback.get_current_url():
                self.missing_cashback.get_url(r'https://www.coupert.com/user/missing-cashback')
            text = self.missing_cashback.check_history_title()
            assert text == 'Missing Cash Back History'

    @compose(feature="Find My Missing Cash Back", story="Missing Cash Back", title='检查Missing Cash Back History页面筛选功能')
    @pytest.mark.MissingCashBack
    def test_check_query(self):
        with allure.step('检查Missing Cash Back History页面筛选功能'):
            if 'commit' in self.missing_cashback.get_current_url():
                self.missing_cashback.get_url(r'https://www.coupert.com/user/missing-cashback')
            else:
                self.missing_cashback.input_domain('shein.com')
                self.missing_cashback.click_query()
                text = self.missing_cashback.get_history_record_domain()
                assert text == 'shein.com'

    def test_check_mcb_detail(self):
        with allure.step('检查View details页面中内容与数据库是否一致'):
            if 'commit' in self.missing_cashback.get_current_url():
                self.missing_cashback.get_url(r'https://www.coupert.com/user/missing-cashback')
            else:
                rid = self.missing_cashback.get_history_record_id()
                self.missing_cashback.click_view_details_button()
                stores = self.missing_cashback.result_stores()
                order_date = self.missing_cashback.result_order_date()
                order_number = self.missing_cashback.result_order_number()
                order_subtotal = self.missing_cashback.result_order_subtotal()
                order_comments = self.missing_cashback.result_comments()
                res = self.missing_cashback.get_history_record(rid)
                assert stores == res[0]
                assert order_date == res[1]
                assert order_number == res[2]
                assert order_subtotal == res[3]
                assert order_comments == res[4]




