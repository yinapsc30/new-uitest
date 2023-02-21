from selenium.webdriver.common.by import By


class IndexElement:

    # 任务中心
    TASK_CENTER = (By.XPATH, '//*[@id="userMenus"]/li[4]/span/div')

    """--------------------------------签到功能元素--------------------------------"""
    # 签到icon
    CHECK_ICON = (By.CLASS_NAME, 'task_checkinItem__w7eiV')
    # 任务获得金币
    TASK_GOLD = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/span[2]')
    # 签到天数
    CHECK_DAYS = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/span[1]/span')
    # 签到总天数
    CHECK_TOTAL_DAYS = (By.XPATH, '//*[@id="__next"]/main/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/span[2]/span')

    """--------------------------------任务列表元素--------------------------------"""
    # 任务列表
    TASK_LIST = 'jsx-320462669 task_listItem__Kujxn'
