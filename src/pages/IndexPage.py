import itertools
import time

from src.utils.elementoperator import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from src.page_element.IndexPageEle import IndexElement


class IndexPageOperation(BasePage):

    def open_url(self, url):
        self.get_url(url)

    def task_center(self):
        """进入Task Center页面"""
        self.logger.info("--进入Task Center--")
        time.sleep(30)
        self.wait_eleVisible(IndexElement.TASK_CENTER)
        self.click_element(IndexElement.TASK_CENTER, model='Task Center')

    def get_task_gold(self):
        """查看未签到前的任务金币数量"""
        task_gold = int(self.get_text(IndexElement.TASK_GOLD, model='任务金币'))
        self.logger.info(f"--获取当前任务金币:{task_gold}--")
        return task_gold

    def check_in_bonus(self):
        """点击签到按钮，并返回当前任务奖励的金币数量"""
        locs = self.find_elements(IndexElement.CHECK_ICON, model='点击签到')
        self.driver.implicitly_wait(10)
        days = {'day 1': 10, 'day 2': 30, 'day 3': 15, 'day 4': 20, 'day 5': 25, 'day 6': 30, 'day 7': 35}
        loc_list = []
        for loc in locs:
            res = loc.get_attribute('innerText')
            loc_list.append(res)
        res = list(list(itertools.chain.from_iterable(loc_list[i].split('\n') for i in range(len(loc_list)))))
        today = "".join(set(list(days.keys())).difference(res))
        bonus = days[today]
        for i in range(7):
            locs[i].click()
            time.sleep(0.5)
        self.logger.info(f"--签到完成，当前签到日为{today}，签到奖励为{bonus}--")
        return bonus

    def get_task_list(self):
        """"""
        task_list_eles = self.driver.execute_script(
            f"return document.getElementsByClassName({IndexElement.TASK_LIST})")
        task_list = []
        for task in task_list_eles:
            res = task.get_attribute('innerText')
            res = res.split('\n')
            task_list.append(res)
        return task_list
