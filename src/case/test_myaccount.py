import time
import pytest
import allure
from src.utils.allureoperator import compose
from src.pages.WithdrawPage import WithdrawPageOperation


@compose(feature="MyAccount", story="Account", title='Account页面正常展示')
@pytest.mark.MyAccount
def test_account_title(drivers):
    pass
