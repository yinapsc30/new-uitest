import time
import pytest
import allure
from src.utils.allureoperator import compose
from src.pages.IndexPage import IndexPageOperation


@compose(feature="任务中心", story="签到任务", title='签到功能校验')
@pytest.mark.Tack_Center
def test_check_in(drivers):
    index = IndexPageOperation(drivers)
    index.open_url('https://www.coupert.com/user/login')
    time.sleep(30)
    with allure.step('开始签到'):
        index.open_url('https://www.coupert.com/user/task')
        # 查看当前任务金币
        task_gold_uncheck = index.get_task_gold()
        # 开始签到，获取当前任务奖励
        check_gold = index.check_in_bonus()
        # 再次获取任务金币
        task_gold_checkin = index.get_task_gold()
        with allure.step(f'断言签到后金币数量，签到前{task_gold_uncheck}，签到后{task_gold_checkin}'):
            assert task_gold_checkin == task_gold_uncheck + check_gold
