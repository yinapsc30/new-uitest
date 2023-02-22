import time
import pytest
import allure
from src.utils.allureoperator import compose
from src.pages.MyAccountPage import MyAccountPageOperation


class TestMyAccount:

    def __init__(self, drivers):
        self.account = MyAccountPageOperation(drivers)

    @compose(feature="MyAccount", story="Account", title='Account页面正常展示')
    @pytest.mark.MyAccount
    def test_account_title(self):
        # 获取title
        with allure.step('获取Account页面title'):
            text = self.account.get_account_title()
            assert text == 'My Cash Back Account'

    @compose(feature="MyAccount", story="Account", title='检查余额TIPS')
    @pytest.mark.MyAccount
    def test_balance_tips(self):
        # 检查余额TIPS
        with allure.step('检查余额TIPS'):
            flag = self.account.check_balance_tips()
            assert flag is True

    @compose(feature="MyAccount", story="Account", title='检查提现额度TIPS')
    @pytest.mark.MyAccount
    def test_withdrawable_tips(self):
        # 检查提现额度TIPS
        with allure.step('检查提现额度TIPS'):
            flag = self.account.check_withdrawable_tips()
            assert flag is True

    @compose(feature="MyAccount", story="Account", title='检查满足提现条件，提现按钮是否可见')
    @pytest.mark.MyAccount
    def test_withdraw_button_enable(self):
        # 检查满足提现条件，提现按钮是否可见
        with allure.step('检查满足提现条件，提现按钮是否可见'):
            withdrawable = self.account.get_withdrawable()
            if withdrawable > 0:
                flag = self.account.withdraw_button()
                assert flag is True
            else:
                flag = self.account.withdraw_button()
                assert flag is False

    @compose(feature="MyAccount", story="Account", title='检查Gold received but balance not updating?链接跳转')
    @pytest.mark.MyAccount
    def test_balance_help_link(self):
        # 检查Gold received but balance not updating?链接跳转是否正常
        with allure.step('检查链接跳转是否正常'):
            res = self.account.click_balance_help_link()
            assert res[0] == 'Why did I receive Gold but my balance didn’t update?'
            assert res[1] == 'https://help.coupert.com/coupert-gold/why-did-i-receive-gold-but-my-balance-didnt-update/'

    @compose(feature="MyAccount", story="Account", title='检查余额历史显示')
    @pytest.mark.MyAccount
    def test_balance_history(self):
        # 检查余额历史显示是否正常
        with allure.step('检查余额历史显示是否正常'):
            balance = self.account.get_balance()
            history = self.account.click_view_balance_history()
            assert balance == history

    @compose(feature="MyAccount", story="Account", title='检查Recommended模块title')
    @pytest.mark.MyAccount
    def test_recommended_title(self):
        # 检查Recommended模块title
        with allure.step('检查Recommended模块title'):
            title = self.account.move_to_recommended_title()
            assert title == 'Recommended Stores'

    @compose(feature="MyAccount", story="Account", title='检查Recommended商家的cb rate')
    @pytest.mark.MyAccount
    def test_recommended_cb_rate(self):
        # 检查Recommended商家的cb rate
        with allure.step('检查Recommended商家的cb rate'):
            res = self.account.check_cb_not_null()
            assert len(res) % 3 == 0

    @compose(feature="MyAccount", story="Account", title='检查My Cash Back Activation Record模块title')
    @pytest.mark.MyAccount
    def test_active_record_title(self):
        # 检查My Cash Back Activation Record模块title
        with allure.step('检查My Cash Back Activation Record模块title'):
            title = self.account.get_active_record_title()
            assert title == 'My Cash Back Activation Record'

    @compose(feature="MyAccount", story="Account", title='检查My Cash Back Activation Record模块title tips')
    @pytest.mark.MyAccount
    def test_active_record_title_tips(self):
        # 检查My Cash Back Activation Record模块title tips
        with allure.step('检查My Cash Back Activation Record模块title tips'):
            flag = self.account.check_active_record_tips()
            assert flag is True

    @compose(feature="MyAccount", story="Account", title='检查Exclusive Offers模块title')
    @pytest.mark.MyAccount
    def test_exclusive_offers_title(self):
        # 检查Exclusive Offers模块title
        with allure.step('检查Exclusive Offers模块title'):
            title = self.account.move_to_exclusive_offers_title()
            assert title == 'Exclusive Offers'

    @compose(feature="MyAccount", story="Account", title='查看Exclusive Offers模块的offers')
    @pytest.mark.MyAccount
    def test_exclusive_offers_title(self):
        # 查看Exclusive Offers模块的offers
        with allure.step('查看Exclusive Offers模块的offers'):
            res = self.account.check_offers_status()
            assert "undefined" not in res
            assert len(res) % 4 == 0
