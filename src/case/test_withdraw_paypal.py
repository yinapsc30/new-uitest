import time
import pytest
import allure
from src.utils.allureoperator import compose
from src.pages.WithdrawPage import WithdrawPageOperation


@compose(feature="提现页面", story="提现", title='PayPal正常提现')
@pytest.mark.Withdraw_Money
def test_withdraw_money_success(drivers):
    withdraw = WithdrawPageOperation(drivers)
    withdraw.open_url('https://www.coupert.com/user/login')
    time.sleep(30)
    with allure.step('开始PayPal提现'):
        withdraw.open_url('https://www.coupert.com/user/withdraw')
        # 查看提现前余额
        balance_unoperated = withdraw.check_balance()
        # 进入提现页面
        withdraw.entry_withdraw_process()
        # 选择Paypal提现
        withdraw.select_paypal()
        # paypal账号勾选确认
        withdraw.click_confirm_check()
        # 进入下一步
        withdraw.click_next_button()
        # 发送验证码
        withdraw.click_verify_code_button()
        # 收取验证码邮箱
        verify_email = withdraw.get_code_email()
        # 点击发送验证码
        withdraw.click_verify_code_button()
        # 数据库获取验证码
        code = withdraw.get_verify_code_from_db(verify_email)
        # 输入验证码
        withdraw.input_verify_code(code)
        # 点击提现
        withdraw.click_withdraw_button()
        # # 获取提现弹窗信息
        # success_text = withdraw.success_text()
        # if success_text:
        #     with allure.step(f'断言提现成功弹窗，弹窗消息{success_text}'):
        #         assert success_text == 'Your withdrawal was submitted for review'
        # # 点击提现成功弹窗
        # withdraw.success_pop_button(success_text)
        # drivers.implicitly_wait(20)
        # # 查看提现后余额
        # balance = withdraw.check_balance()
        # with allure.step(f'断言提现后余额变化，提现前{balance_unoperated}，提现后{balance}'):
        #     assert balance == 0


@compose(feature="提现页面", story="提现", title='PayPal提现验证码错误')
@pytest.mark.Withdraw_Money
def test_withdraw_money_success(drivers):
    withdraw = WithdrawPageOperation(drivers)
    withdraw.open_url('https://www.coupert.com/user/login')
    time.sleep(30)
    with allure.step('开始PayPal提现'):
        withdraw.open_url('https://www.coupert.com/user/withdraw')
        # 查看提现前余额
        balance_unoperated = withdraw.check_balance()
        # 进入提现页面
        withdraw.entry_withdraw_process()
        # 选择Paypal提现
        withdraw.select_paypal()
        # paypal账号勾选确认
        withdraw.click_confirm_check()
        # 进入下一步
        withdraw.click_next_button()
        # 发送验证码
        withdraw.click_verify_code_button()
        # 收取验证码邮箱
        withdraw.get_code_email()
        # 数据库获取验证码
        ...
        # 输入验证码
        withdraw.input_verify_code(1234)
        # 点击提现
        withdraw.click_withdraw_button()
