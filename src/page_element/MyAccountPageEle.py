from selenium.webdriver.common.by import By


class MyAccountElement:

    """--------------------------------My Cash Back Account--------------------------------"""

    ACCOUNT = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div/div[1]')
    BALANCE = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div/div[2]/div[1]/span')
    BALANCE_TIPS = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div/img')
    BALANCE_TIPS_TEXT = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div')
    BALANCE_TIPS_LINK = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/a')
    BALANCE_LINK_TEXT = (By.XPATH, '//*[@id="post-145"]/footer[1]/h1')

    WITHDRAWABLE = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div/div[2]/div[2]/span/div')
    WITHDRAWABLE_TIPS = (By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div')
    WITHDRAWABLE_LINK_TEXT = (By.XPATH, '//*[@id="post-397"]/footer[1]/h1')
    WITHDRAW_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div/div[2]/div[3]/div')

    BALANCE_HELP_LINK = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div/div[3]/a')
    HELP_LINK_TEXT = (By.XPATH, '//*[@id="post-379"]/footer[1]/h1')

    BALANCE_HISTORY = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div/div[3]/i')
    BALANCE_HISTORY_DETAIL = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div/div[4]/div/div/div/div/div/table/tbody/tr[1]/td[3]')

    """--------------------------------Recommended Stores--------------------------------"""

    RECOMMENDED = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[1]')
    RECOMMENDED_STORES = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[2]')
    # CASHBACK_RATE = (By.CLASS_NAME, 'account_store_info__bubVi')
    # CASHBACK_RATE = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[2]/a[1]')

    """--------------------------------My Cash Back Activation Record--------------------------------"""

    CASHBACK_RECORD = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[3]/div[1]')
    CASHBACK_RECORD_TIPS = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[3]/div[1]/img')
    CASHBACK_RECORD_TIPS_LINK = (By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div/a')

    """--------------------------------Exclusive Offers--------------------------------"""

    EXCLUSIVE_OFFERS = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[4]/div[1]')
    COPY_CODE_BUTTON = (By.CLASS_NAME, 'account_store_btn_copy__kS7p4')
    RATE_SUCCESS = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[4]/ul/li[1]/div[2]/div/span')
    # SHOP_NOW = (By.CLASS_NAME, 'account_Link_color__CfmT6')
    SHOP_NOW = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[4]/ul/li[1]/div[3]/a')
