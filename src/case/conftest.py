import inspect
import os
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from config.config_init import Email,PassWord
# from src.pages.HomePage import HomePage
from src.utils.allureoperator import attach_png
from src.utils.constant import TEST_PIC
# from src.utils.dataoperator import DataOperator
# from src.utils.fileoperator import FileOperator
# from src.utils.jsonoperator import JsonOperator
# from src.utils.reportoperator import ReportOperator
from src.utils.logoperator import LogOperator
from src.utils.timeoperator import timeoperator
from src.utils.sendreport import send_report

logger = LogOperator(__name__)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    pytest 失败后执行
    :param item: 测试用例
    :param call: 测试步骤
    :return:
    """
    out = yield
    result = out.get_result()
    logger.info(f"测试报告:{result}")
    logger.info(f"执行耗时:{call.duration}")
    if result.outcome in ['failed', 'error']:
        for k, v in item.funcargs.items():
            try:
                if hasattr(v, 'driver'):
                    attach_png(f'{TEST_PIC}/{int(time.time())}.png', "失败截图", v)
                    break
            except Exception as e:
                logger.error(f"失败截图异常:{e}")


# def pytest_assume_fail(lineno, entry):
#     ...
#     # """
#     # assume 断言报错截图
#     # """
#     # print(entry)
#     # for i in inspect.stack():
#     #     if os.path.split(i.filename)[1].startswith('test_'):
#     #         try:
#     #             for k, v in i.frame.f_locals.items():
#     #                 if hasattr(v, 'driver'):
#     #                     attach_png(f'{TEST_PIC}/{int(time.time())}.png', f"失败截图_{int(time.time())}", v)
#     #                     break
#     #         except Exception:
#     #             pass


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    收集测试结果，并发送测试报告（发送报告功能还未完成，待完善）
    :param terminalreporter: 测试报告数据对象
    :param exitstatus:
    :param config:
    :return:
    """
    total = terminalreporter._numcollected
    stats = terminalreporter.stats
    failed_num = len(stats.get('failed', []))
    error_num = len(stats.get('error', []))
    # _sessionstarttime 会话开始时间
    duration = time.time() - terminalreporter._sessionstarttime
    result = {
        "total": f"总计:{total}",
        'passed': f"通过:{len(stats.get('passed', []))}",
        'failed': f"失败:{failed_num}",
        'error': f"异常:{error_num}",
        'skipped': f"跳过:{len(stats.get('skipped', []))}",
        'total times': f"总耗时:{duration}秒"
    }
    logger.info(f"总计:{total}")
    logger.info(f"通过:{len(stats.get('passed', []))}")
    logger.info(f"失败:{failed_num}")
    logger.info(f"异常:{error_num}")
    logger.info(f"跳过:{len(stats.get('skipped', []))}")
    logger.info(f"总耗时:{duration}秒")
    if result['failed'] or result['error']:
        send_report()


# def pytest_terminal_summary(terminalreporter, exitstatus, config):
#     """
#     统计测试结果
#     :param terminalreporter:测试报告数据对象
#     :param exitstatus:
#     :param config:
#     :return:
#     """
#     logger.info(f"总计:{terminalreporter._numcollected}")
#     stats = terminalreporter.stats
#     failed_num = len(stats.get('failed', []))
#     error_num = len(stats.get('error', []))
#     logger.info(f"通过:{len(stats.get('passed', []))}")
#     logger.info(f"失败:{failed_num}")
#     logger.info(f"异常:{error_num}")
#     logger.info(f"跳过:{len(stats.get('skipped', []))}")
#     duration = time.time() - terminalreporter._sessionstarttime
#     logger.info(f"总耗时:{duration}秒")
#     if not hasattr(config, "workerinput"):
#         jsonoperator = JsonOperator()
#         allure_results = jsonoperator.get_allure_result()
#         if failed_num + error_num > 0:
#             try:
#                 r = ReportOperator(hook=ROBOT.split(','))
#                 result_str = '\n'.join([
#                     f"通过:{len(stats.get('passed', []))}",
#                     f"失败:{len(stats.get('failed', []))}",
#                     f"异常:{len(stats.get('error', []))}",
#                     f"跳过:{len(stats.get('skipped', []))}",
#                     f"耗时:{duration:.2f}秒",
#                 ])
#                 try:
#                     passed_list, failed_list, error_list, skipped_list = r.change_run_detail(allure_results)
#                     if len(failed_list):
#                         result_str += '\n\n失败用例:\n'
#                         result_str += '\n'.join(failed_list)
#                     if len(error_list):
#                         result_str += '\n\n异常用例:\n'
#                         result_str += '\n'.join(error_list)
#                 except Exception as e:
#                     logger.error(e)
#                 r.send_msg(result_str)
#             except Exception as e:
#                 logger.error(e)


# def pytest_collection_modifyitems(session, items):
#     """
#     修改用例执行顺序
#     :param session: 会话信息
#     :param items: 用例列表
#     :return:
#     """
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode_escape")
#         item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
#     logger.info(f"收集到的测试用例:{items}")


@pytest.fixture(scope='session')
def drivers():
    """
    实例化webdriver驱动
    :return:
    """
    try:
        desired_capabilities = DesiredCapabilities.CHROME
        # 等待页面加载完成再输出
        desired_capabilities["pageLoadStrategy"] = "eager"
        driver = webdriver.Chrome(desired_capabilities=desired_capabilities)
        driver.maximize_window()
        time.sleep(2)
        logger.info(f"实例化驱动成功！")
        yield driver
        logger.info(f"关闭浏览器，测试结束！")
        driver.quit()
    except:
        logger.error("实例化驱动错误，请检查驱动与浏览器版本是否一致！")


@pytest.fixture(scope='session')
def hand_driver(drivers):
    from src.pages.WithdrawPage import WithdrawPageOperation
    from src.pages.LoginPage import LoginPageOperation
    hand_driver = drivers
    withdraw = WithdrawPageOperation(hand_driver)
    login = LoginPageOperation(hand_driver)
    with allure.step(f"手动验证登录开始！"):
        withdraw.open_url(r'https://www.coupert.com/user/login')
        login.input_email(Email)
        login.input_password(PassWord)
        login.visible_account_email()
        time.sleep(5)
    yield hand_driver


