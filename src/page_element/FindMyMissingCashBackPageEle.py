from selenium.webdriver.common.by import By


class FindMyMissingCashBackElement:
    """--------------------------------My Missing Cash Back--------------------------------"""

    MY_MISSING_CASH_BACK_TITLE = (By.XPATH, '//*[@id="rc-tabs-3-panel-missing-cashback"]/div[1]/div[1]')
    MMCB_DESC = (By.XPATH, '//*[@id="rc-tabs-3-panel-missing-cashback"]/div[1]/div[2]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="rc-tabs-3-panel-missing-cashback"]/div[1]/div[3]')

    """--------------------------------Missing Cash Back--------------------------------"""

    MCB_TITLE = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div[1]')
    MCB_NOTICE = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div[2]/span')
    MCB_STORES_INPUT = (By.XPATH, '//*[@id="domain"]')
    MCB_ORDER_DATE_INPUT = (By.XPATH, '//*[@id="orderTime"]')
    MCB_ORDER_NUMBER_INPUT = (By.XPATH, '//*[@id="__mcb_wrap"]/form/div[3]/div/div[2]/div/div/input')
    MCB_ORDER_SUBTOTAL_INPUT = (By.XPATH, '//*[@id="subtotal"]')
    MCB_PROFILE_ATTACH_INPUT = (By.XPATH, '//*[@id="photoNames"]')
    MCB_COMMENTS = (By.XPATH, '//*[@id="comment"]')
    MCB_SUBMIT_BUTTON = (By.XPATH, '//*[@id="__mcb_wrap"]/div[1]/div/div/div/div/button')
    MCB_BUTTON_TEXT = (By.XPATH, '//*[@id="__mcb_wrap"]/div[1]/div/div/div/div/button/span')

    """--------------------------------Missing Cash Back History--------------------------------"""

    MISSING_CASH_BACK_HISTORY_TITLE = (By.XPATH, '//*[@id="rc-tabs-3-panel-missing-cashback"]/div[2]/div[1]')
    DOMAIN_INPUT = (By.XPATH, '//*[@id="rc_select_10"]')
    QUERY_BUTTON = (By.XPATH, '//*[@id="missing_cashback_search"]/div[1]/div[2]/button')
    QUERY_DOMAIN = (
        By.XPATH,
        '//*[@id="rc-tabs-3-panel-missing-cashback"]/div[2]/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[3]')
    MCB_ID = (
        By.XPATH,
        '//*[@id="rc-tabs-3-panel-missing-cashback"]/div[2]/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[2]')
    VIEW_DETAIL = (
        By.XPATH,
        '//*[@id="rc-tabs-0-panel-missing-cashback"]/div[2]/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[5]/a')

    """--------------------------------Missing Cash Back Result--------------------------------"""

    RESULT_TITLE = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div[1]')
    RESULT_NOTICE_TEXT = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div[2]/span')
    RESULT_STORES = (By.XPATH, '//*[@id="domain"]')
    RESULT_ORDER_DATE = (By.XPATH, '//*[@id="orderTime"]')
    RESULT_ORDER_NUMBER = (By.XPATH, '//*[@id="__mcb_wrap"]/form/div[3]/div/div[2]/div/div/input')
    RESULT_ORDER_SUBTOTAL = (By.XPATH, '//*[@id="subtotal"]')
    RESULT_ORDER_COMMENTS = (By.XPATH, '//*[@id="comment"]')

    RESULT_NOTICE_TEXT_JS = 'document.querySelector("#__next > main > div > div.ant-col.userContentLeft_' \
                            'colMarginAndPadding__Z3GqL.ant-col-xs-20.ant-col-sm-20.ant-col-md-20.ant-col-lg-14.' \
                            'ant-col-xl-14.ant-col-xxl-14 > div.queryInfoMinssingCashBack_query_warp__omS1S > ' \
                            'div.queryInfoMinssingCashBack_waring_title__CUqa7 > span")'
    RESULT_STORES_JS = 'document.querySelector("#domain")'
    RESULT_ORDER_DATE_JS = 'document.querySelector("#orderTime")'
    RESULT_ORDER_NUMBER_JS = 'document.querySelector("#__mcb_wrap > form > div:nth-child(3) > div > ' \
                             'div.ant-col.ant-form-item-control > div > div > input")'
    RESULT_ORDER_SUBTOTAL_JS = 'document.querySelector("#subtotal")'
    RESULT_ORDER_COMMENTS_JS = 'document.querySelector("#comment")'
