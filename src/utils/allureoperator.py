import time
import builtins
import allure
import pytest
from src.utils.logoperator import LogOperator


logger = LogOperator(__name__)


def compose(**kwargs):
    """
    将头部ALlure装饰器进行封装
    可以采用：
        feature='模块名称'
        story='用户故事'
        title='用例标题'
        testcase='测试用例链接地址'
        severity='用例等级(blocker、critical、normal、minor、trivial)'
        link='链接'
        testcase=("url", "xx测试用例")
        issue=('bug地址', 'bug名称')
    的方式入参数
    :param kwargs:
    :return:
    """

    def deco(f):
        builtins.__dict__.update({'allure': allure})
        # 失败重跑
        if kwargs.get("reruns"):
            f = pytest.mark.flaky(
                reruns=kwargs.get("reruns", 2),  # 默认共执行2次
                reruns_delay=kwargs.get("reruns_delay", 5)  # 默认等待5秒
            )(f)
            kwargs.pop("reruns")
            if kwargs.get("reruns_delay"):
                kwargs.pop("reruns_delay")
        _kwargs = [('allure.' + key, value) for key, value in kwargs.items()]
        for allurefunc, param in reversed(_kwargs):
            if param:
                if isinstance(param, tuple):
                    f = eval(allurefunc)(*param)(f)
                else:
                    f = eval(allurefunc)(param)(f)
            else:
                f = eval(allurefunc)(f)
        return f
    return deco


def attach_png(pic_path, name, ele=None):
    """
    将png图片存放到allure报告上
    :param pic_path: 图片位置
    :param name: 展示的名称
    :param ele: ElementOperator对象
    :return:
    """
    try:
        if ele:
            ele.screenshot_pic(pic_path)
        allure.attach.file(source=pic_path, name=name, attachment_type=allure.attachment_type.PNG)
        logger.info(f'截图 {name}，存放到 {pic_path} 成功！')
    except Exception as e:
        logger.error(f'存放图片{name}失败:{e}')


def attach_text(body, name):
    """
    将text放在allure报告上
    :param body: 内容
    :param name: 标题
    :return:
    """
    try:
        allure.attach(body=str(body), name=str(name), attachment_type=allure.attachment_type.TEXT)
        logger.info(f'存放文字 {name}:{body} 成功！')
    except Exception as e:
        logger.error(f'存放文字失败 {name}:{body}！:{e}')
