from selenium.webdriver.common.by import By


class GoldOrderDetailElement:
    GOLD_REWARDS = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/h1')
    CASH_BACK_GOLD = (By.XPATH, '//*[@id="rc-tabs-1-panel-gold_order"]/div[1]/div[1]/div[1]/span')
    CONFIRMED_GOLD = (By.XPATH, '//*[@id="rc-tabs-1-panel-gold_order"]/div[1]/div[1]/div[2]/div[1]')
    PENDING_GOLD = (By.XPATH, '//*[@id="rc-tabs-1-panel-gold_order"]/div[1]/div[1]/div[2]/div[2]')

    TASK_GOLD = (By.XPATH, '//*[@id="rc-tabs-1-panel-gold_order"]/div[1]/div[1]/div[2]/div[2]')
    CONFIRMED_TASK_GOLD = (By.XPATH, '//*[@id="rc-tabs-1-panel-gold_order"]/div[1]/div[2]/div[2]/div[1]')
    PENDING_TASK_GOLD = (By.XPATH, '//*[@id="rc-tabs-1-panel-gold_order"]/div[1]/div[2]/div[2]/div[2]')

    '--------------------------------Gold Detail--------------------------------'
    GOLD_DETAIL = (By.XPATH, '//*[@id="rc-tabs-1-panel-gold_order"]/div[2]/div[1]')
    GOLD_DETAIL_LINK = (By.XPATH, '//*[@id="rc-tabs-1-panel-gold_order"]/div[2]/div[1]/a')
    HELP_PAGE_TITLE = (By.XPATH, '//*[@id="post-379"]/footer[1]/h1')

    MERCHANT_INPUT = (By.XPATH,
                      "//div[@id='__id_div_gold_search']/div[1]/div[1]/div/div/div[2]/div/div/div/div/span[1]/input")
    # DETAIL_QUERY_BUTTON = (By.XPATH, '/html[1]/body[1]/div[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]')
    DETAIL_QUERY_BUTTON = (By.XPATH, "//div[contains(text(),'Query')]")
    MERCHANT_TEXT = (By.XPATH,
                     '/html/body/div[1]/main/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[2]/td[2]')

    DETAIL_BUTTON = (By.XPATH,
                     '/html/body/div[1]/main/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[2]/td[8]/div/button')
    DETAIL_BOX_TEXT = (By.XPATH, "//div[@class='jsx-2717541934 rewards_operation_tips__z25vw']")

    APPEAL_LINK = (By.XPATH,
                   '//*[@id="rc-tabs-1-panel-gold_order"]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[2]/td[8]/div/div')
    APPEAL_PAGE_TITLE = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/h1')

    '--------------------------------Submit Appeal--------------------------------'

    SUBMIT_PAGE_TITLE = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/h1')
    SUBMIT_PAGE_TIPS = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div/ul/li')
    APPEAL_EVENT_INPUT = (By.XPATH, '//*[@id="SubmitAppeal_Cascader"]')
    ADD_IMG_UPLOAD = (By.XPATH, '//*[@id="SubmitAppeal_photoNames"]')
    COMMENTS_TEXTAREA = (By.XPATH, '//*[@id="SubmitAppeal_comment"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="SubmitAppeal"]/div[6]/div/div/div/div/button')

    '--------------------------------Appeal List--------------------------------'

    APPEAL_LIST = (By.XPATH, '//*[@id="appeal_list"]/div[1]')
    DOMAIN_INPUT = (By.XPATH, '//*[@id="appealList_search"]/div[1]/div[1]/div/div/div[2]/div/div/div/span/span/svg')
    SELECT_DOMAIN = (By.XPATH, '//*[@id="appealList_search"]/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]')
    APPEAL_QUERY_BUTTON = (By.XPATH, '//*[@id="appealList_search"]/div[1]/div[2]/button')
    DOMAIN_TEXT = (By.XPATH, '//*[@id="appeal_list"]/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[3]')