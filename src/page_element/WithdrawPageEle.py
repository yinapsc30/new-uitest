from selenium.webdriver.common.by import By


class WithdrawElement:
    # Withdraw Money
    WITHDRAW_MONEY = (By.XPATH, '//*[@id="userMenus"]/li[4]/span/div')
    # 余额
    BALANCE = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div/div[2]/div[1]/span')
    # 提现按钮
    WITHDRAW_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div/div[2]/div[2]/div')
    # 账号email
    ACCOUNT_EMAIL = (By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[1]/div[3]/span[2]')

    '--------------------------------礼品卡提现元素--------------------------------'
    # 提现入口
    GIFTCARD_ENTRY = (By.XPATH, '/html/body/div/main/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div')
    # 选择国家
    # CHOOSE_COUNTRY = (By.XPATH, '//*[@id="rc_select_2"]')
    CHOOSE_COUNTRY = (By.XPATH, "//div[@id='__countryChooseSelect']/div[1]/div/span[1]/input")
    US = (By.XPATH, '//*[@id="__countryChooseSelect"]/div[2]/div/div/div/div/ul/li[1]')
    # 选择礼品卡
    AMAZON = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/dl[1]/dt')
    CHOOSE_GIFTCARD = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div/div/dl[1]')
    # 礼品卡提示文案
    GIFTCARD_TIPS = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div/p/span')
    # 提示确认勾选框
    GIFTCARD_TIPS_CHECKBOX = (
        By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/div/div/div/p/input')
    # 返回按钮
    SELECT_BACK_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[2]/div/div[4]/button[1]')
    # 下一步按钮
    SELECT_NEXT_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[2]/div[2]/div/div[4]/button[2]')

    '--------------------------------PayPal提现元素--------------------------------'
    # 提现入口
    PAYPAL_ENTRY = (By.XPATH, '/html/body/div/main/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div')
    # PayPal账号
    PAYPAL_ACCOUNT = (By.XPATH, '//*[@id="basic"]/div[1]/span')
    # Paypal邮箱检查
    PAYPAL_CHANGE_CHECK = (By.XPATH, '//*[@id="basic"]/div[1]/a')
    # 输入Paypal账号
    INPUT_PAYPAL_EMAIL = (By.XPATH, '//*[@id="basic_email"]')
    # paypal账号确认单选框
    PAYPAL_CHECKBOX = (By.XPATH, '//*[@id="basic"]/p[2]/input')
    # 返回按钮
    BACK_BUTTON = (By.XPATH, '//*[@id="basic"]/div[2]/div/div/div/div/div/button[1]')
    # 下一步按钮
    NEXT_BUTTON = (By.XPATH, '//*[@id="basic"]/div[2]/div/div/div/div/div/button[2]')
    # 提现成功文案
    SUCCESS_TEXT = (By.XPATH, '//*[@id="__coueprt_withdraw_paypal_giftCard"]/div/div[2]/div/div[2]/div/div[2]/p')
    # 提现成功弹窗按钮
    SUCCESS_BUTTON = (By.XPATH, '//*[@id="__coueprt_withdraw_paypal_giftCard"]/div/div[2]/div/div[2]/div/button')

    '-----------------------------------最终提现页面元素------------------------------'
    # 提现验证邮箱
    WITHDRAW_EMAIL = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/p/span')
    # 验证码输入框
    VERIFY_CODE_INPUT = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/input')
    # 发送验证码按钮
    SEND_VERIFY_CODE_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/button')
    # 返回按钮
    WITHDRAW_BACK_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/button[1]')
    # 确认提现按钮
    WITHDRAW_CONFIRM_BUTTON = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div[2]/div[2]/div/div[3]/button[2]')
    # 验证码错误文案
    VERIFY_WRONG_TEXT = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div[2]/div[2]/div/div[3]')

