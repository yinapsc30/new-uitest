import time
import pytest
import allure
from config.assert_message import AssertMessage as AM
from src.utils.allureoperator import compose
from src.pages.WithdrawPage import WithdrawPageOperation
from src.pages.LoginPage import LoginPageOperation


@compose(feature="提现页面", story="提现", title='giftcard正常提现')
@pytest.mark.Withdraw_Money
def test_withdraw_giftcard_success(hand_driver):
    withdraw = WithdrawPageOperation(hand_driver)
    with allure.step('开始GiftCard提现'):
        withdraw.open_url('https://www.coupert.com/user/withdraw')
        # 进入提现页面
        withdraw.entry_withdraw_process()
        # 选择Giftcard提现
        withdraw.select_giftcard()
        # 选择国家
        withdraw.choose_country()
        # 选择礼品卡商家
        withdraw.choose_giftcard()
        # 确认礼品卡
        withdraw.click_giftcard_checkbox()
        # 进入下一步
        withdraw.click_next_giftcard()
        # 点击发送验证码
        withdraw.click_verify_code_button()
        # 数据库获取验证码
        ...
        # 输入验证码
        withdraw.input_verify_code(1234)
        # 点击提现
        withdraw.click_withdraw_button()
        # 获取失败提示文案
        error_text = withdraw.get_verify_wrong_text()
        # 断言提现失败文案是否与预期一致
        assert error_text == AM.VERIFY_WRONG_MESSAGE
        # # 获取提现弹窗信息
        # success_text = withdraw.success_text()
        # if success_text:
        #     with allure.step(f'断言提现成功弹窗，弹窗消息{success_text}'):
        #         assert success_text == 'Your withdrawal was submitted for review'
        # # 点击提现成功弹窗
        # withdraw.success_pop_button(success_text)
        # # 查看提现后余额
        # balance = withdraw.check_balance()
        # with allure.step(f'断言提现后余额变化，提现前{balance_unoperated}，提现后{balance}'):
        #     assert balance == 0


# @compose(feature="提现页面", story="提现", title='PayPal提现验证码错误')
# @pytest.mark.Withdraw_Money
# def test_withdraw_money_success(hand_driver):
#     withdraw = WithdrawPageOperation(hand_driver)
#     # login = LoginPageOperation(drivers)
#     # with allure.step(f"手动验证登录开始！"):
#     #     withdraw.open_url('https://www.coupert.com/user/login')
#     email = 'burtontest@test.com'
#     #     password = 123456
#     #     login.input_email(email)
#     #     login.input_password(password)
#     #     login.visible_account_email()
#     #     time.sleep(5)
#     with allure.step('开始PayPal提现'):
#         withdraw.open_url('https://www.coupert.com/user/withdraw')
#         # 进入提现页面
#         withdraw.entry_withdraw_process()
#         # 选择Paypal提现
#         withdraw.select_paypal()
#         # paypal账号勾选确认
#         withdraw.click_confirm_check(email)
#         # 进入下一步
#         withdraw.click_next_button()
#         # 发送验证码
#         withdraw.click_verify_code_button()
#         # 点击发送验证码
#         withdraw.click_verify_code_button()
#         # 数据库获取验证码
#         ...
#         # 输入验证码
#         withdraw.input_verify_code(1234)
#         # 点击提现
#         withdraw.click_withdraw_button()
#         # 获取失败提示文案
#         error_text = withdraw.get_verify_wrong_text()
#         # 断言提现失败文案是否与预期一致
#         assert error_text == AM.VERIFY_WRONG_MESSAGE


if __name__ == '__main__':
    pytest.main(['-v', '-s', '/Users/soar/PycharmProjects/soar_uitest/src/case/test_withdraw_giftcard.py::test_withdraw_money_success'])