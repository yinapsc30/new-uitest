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
