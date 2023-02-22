import time
import pytest
import allure
from src.utils.allureoperator import compose
from src.pages.WithdrawPage import WithdrawPageOperation


@compose(feature="MyAccount", story="Account", title='Account页面正常展示')
@pytest.mark.MyAccount
def test_account_title(drivers):
    pass


def test_recommended(drivers):
    pass
    # eles = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[2]')
    # # for i in eles:
    # #     text = i.text
    # #     print("text:", text.split('\n'))
    # b = len([i.text.split('\n') for i in eles][0])
    # assert len([i for i in eles]) % 3 == 0


def test_exclusive_offers(drivers):
    pass
    # eles = driver.find_elements(By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[4]/ul')
    # # for el in eles:
    # #     text = el.text
    # #     print("text:", text.split('\n'))
    # b = [i.text.split('\n') for i in eles][0]
    # assert "undefined" not in b
    # assert len(b) % 4 == 0
