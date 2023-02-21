import time
import pytest
import allure
from src.utils.allureoperator import compose
from src.pages.WithdrawPage import WithdrawPageOperation


@compose(feature="提现页面", story="提现", title='验证码邮箱验证')
@pytest.mark.Withdraw_Money
def test_withdraw_email(drivers):
    withdraw = WithdrawPageOperation(drivers)
    withdraw.open_url('https://www.coupert.com/user/withdraw')
    time.sleep(30)
    with allure.step('开始验证码邮箱验证'):
        withdraw.open_url('https://www.coupert.com/user/task')
        # 进入提现页面
        withdraw.entry_withdraw_process()
        # 进入下一步
        withdraw.click_next_button()
        # 确认邮箱
        account_email = withdraw.get_account_email()
        verify_email = withdraw.get_code_email()
        with allure.step(f'断言邮箱信息是否正确，当前账户邮箱{account_email}，收取验证码邮箱{verify_email}'):
            assert verify_email == account_email
