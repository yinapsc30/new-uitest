from src.utils.constant import BASE_PATH
from src.utils.logoperator import LogOperator
import logging
import os
import time
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver import ActionChains as AC
from src.utils.timeoperator import TimeOperator

"""
    此类封装所有操作，所有页面继承该类
"""


class BasePage(object):

    def __init__(self, driver):
        self.logger = LogOperator(__name__)
        self.driver = driver

    def implicitly_wait_second(self, sec):
        self.driver.implicitly_wait(sec)

    # 等待元素可见
    def wait_eleVisible(self, loc, model=None, timeout=30, poll_frequency=0.5):
        """
        :param loc:元素定位表达;元组类型,表达方式(元素定位类型,元素定位方法)
        :param timeout:等待的上限
        :param poll_frequency:轮询频率
        :param model:等待失败时,截图操作,图片文件中需要表达的功能标注
        :return:None
        """
        self.logger.info(f'等待"{model}"元素,定位方式:{loc}')
        try:
            start = datetime.now()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(loc))
            end = datetime.now()
            self.logger.info(f'等待"{model}"时长:{end - start}')
            return True
        except TimeoutException:
            self.logger.exception(f'等待"{model}"元素失败,定位方式:{loc}')
            # 截图
            self.save_webImgs(f"等待元素[{model}]出现异常")
            raise

    # 判断元素可点击
    def ele_is_enabled(self, loc, timeout=30, poll_frequency=0.5, model=None):
        """
        :param loc:元素定位表达;元组类型,表达方式(元素定位类型,元素定位方法)
        :param timeout:等待的上限
        :param poll_frequency:轮询频率
        :param model:等待失败时,截图操作,图片文件中需要表达的功能标注
        :return:None
        """
        self.logger.info(f'判断"{model}"元素可点击,定位方式:{loc}')
        try:
            start = datetime.now()
            WebDriverWait(self.driver, timeout, poll_frequency).until(loc.is_enabled())
            end = datetime.now()
            self.logger.info(f'等待"{model}"时长:{end - start}')
            return True
        except TimeoutException:
            self.logger.exception(f'判断"{model}"元素失败,定位方式:{loc}')
            # 截图
            self.save_webImgs(f"判断元素[{model}]出现异常")
            raise

    # 等待元素不可见
    def wait_eleNoVisible(self, loc, timeout=30, poll_frequency=0.5, model=None):
        """
        :param loc:元素定位表达;元组类型,表达方式(元素定位类型,元素定位方法)
        :param timeout:等待的上限
        :param poll_frequency:轮询频率
        :param model:等待失败时,截图操作,图片文件中需要表达的功能标注
        :return:None
        """
        logging.info(f'等待"{model}"消失,元素定位:{loc}')
        try:
            start = datetime.now()
            WebDriverWait(self.driver, timeout, poll_frequency).until_not(EC.visibility_of_element_located(loc))
            end = datetime.now()
            self.logger.info(f'等待"{model}"时长:{end - start}')
            return True
        except TimeoutException:
            self.logger.exception(f'等待"{model}"元素失败,定位方式:{loc}')
            # 截图
            self.save_webImgs(f"等待元素[{model}]消失异常")
            raise

    # 查找一个元素element
    def find_element(self, loc, model=None):
        self.logger.info(f'查找"{model}"元素，元素定位:{loc}')
        try:
            ele = self._get_element(loc, model)
            return ele
        except NoSuchElementException:
            self.logger.exception(f'查找"{model}"元素失败,定位方式:{loc}')
            # 截图
            self.save_webImgs(f"查找元素[{model}]异常")
            raise

    # 查找元素elements
    def find_elements(self, loc, model=None):
        self.logger.info(f'查找"{model}"元素集，元素定位:{loc}')
        try:
            return self.driver.find_elements(*loc)
        except NoSuchElementException:
            self.logger.exception(f'查找"{model}"元素集失败,定位方式:{loc}')
            # 截图
            self.save_webImgs(f"查找元素集[{model}]异常")
            raise

    # 查看元素是否存在
    def elements_is_exists(self, loc, model=None, timeout=3, poll_frequency=0.5):
        start_time = time.time()
        self.logger.info(f'查找"{model}"元素，元素定位:{loc}')
        while True:
            try:
                WebDriverWait(self.driver, timeout, poll_frequency).until(
                    EC.visibility_of_element_located(loc)
                )
                return True
            except:
                if time.time() - start_time >= timeout:
                    self.logger.info(f'未找到"{model}"元素')
                    return False
                else:
                    time.sleep(0.2)

    # 输入操作
    def input_text(self, loc, text, model=None):
        # 查找元素
        ele = self.find_element(loc, model)
        # 输入操作
        self.logger.info(f'在"{model}"输入"{text}",元素定位:{loc}')
        try:
            ele.send_keys(text)
        except:
            self.logger.exception(f'"{model}"输入操作失败!')
            # 截图
            self.save_webImgs(f"[{model}]输入异常")
            raise

    # 上传操作
    def upload_file(self, loc, path, model=None):
        # 查找元素
        ele = self.find_element(loc, model)
        # 输入操作
        self.logger.info(f'在"{model}"上传文件："{path}",元素定位:{loc}')
        try:
            ele.send_keys(path)
        except:
            self.logger.exception(f'"{model}上传操作失败!')
            # 截图
            self.save_webImgs(f"[{model}]操作异常")
            raise

    # 清除操作
    def clean_input_text(self, loc, model=None):
        ele = self.find_element(loc, model)
        # 清除操作
        self.logger.info(f'清除"{model}",元素定位:{loc}')
        try:
            ele.clear()
        except:
            self.logger.exception(f'"{model}"清除操作失败')
            # 截图
            self.save_webImgs(f"[{model}]清除异常")
            raise

    # 点击操作
    def click_element(self, loc, model=None):
        # 先查找元素在点击
        ele = self.find_element(loc, model)
        # 点击操作
        self.logger.info(f'点击"{model}",元素定位:{loc}')
        try:
            ele.click()
        except:
            self.logger.exception(f'"{model}"点击失败')
            # 截图
            self.save_webImgs(f"[{model}]点击异常")
            raise

    # js点击操作
    def click_by_js(self, loc, timeout=8, frequency=0.5, model=None):
        time.sleep(0.5)
        self.wait_eleVisible(loc, model, timeout, frequency)
        ele = self.find_element(*loc)
        try:
            self.driver.execute_script("(arguments[0]).click()", ele)
        except:
            self.logger.exception(f"向{loc}元素点击失败")
            self.save_webImgs(model)
            raise
        else:
            self.logger.info(f"向{loc}元素点击成功")

    # 获取文本内容
    def get_text(self, loc, model=None):
        # 先查找元素在获取文本内容
        ele = self.find_element(loc, model)
        # 获取文本
        self.logger.info(f'获取"{model}"元素文本内容，元素定位:{loc}')
        try:
            text = ele.text
            self.logger.info(f'获取"{model}"元素文本内容为"{text}",元素定位:{loc}')
            return text
        except:
            self.logger.exception(f'获取"{model}"元素文本内容失败,元素定位:{loc}')
            # 截图
            self.save_webImgs(f"获取[{model}]文本内容异常")
            raise

    # 获取属性值
    def get_element_attribute(self, loc, name, model=None):
        # 先查找元素在去获取属性值
        ele = self.find_element(loc, model)
        # 获取元素属性值
        self.logger.info(f'获取"{model}"元素属性，元素定位:{loc}')
        try:
            ele_attribute = ele.get_attribute(name)
            self.logger.info(f'获取"{model}"元素"{name}"属性集为"{ele_attribute}"，元素定位:{loc}')
            return ele_attribute
        except:
            self.logger.exception(f'获取"{model}"元素"{name}"属性失败,元素定位:{loc}')
            # 截图
            self.save_webImgs(f"获取[{model}]属性异常")
            raise

    # iframe 切换
    def switch_iframe(self, frame_refer, timeout=30, poll_frequency=0.5, model=None):
        # 等待 iframe 存在
        self.logger.info('iframe 切换操作:')
        try:
            # 切换 == index\name\id\WebElement
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.frame_to_be_available_and_switch_to_it(frame_refer))
            sleep(0.5)
            self.logger.info('切换成功')
        except:
            self.logger.exception('iframe 切换失败!!!')
            # 截图
            self.save_webImgs(f"iframe切换异常")
            raise

    # 窗口切换 = 如果是切换到新窗口,new. 如果是回到默认的窗口,default
    def switch_window(self, name, cur_handles=None, timeout=20, poll_frequency=0.5, model=None):
        """
        调用之前要获取window_handles
        :param name: new 代表最新打开的一个窗口. default 代表第一个窗口. 其他的值表示为窗口的 handles
        :param cur_handles:
        :param timeout:等待的上限
        :param poll_frequency:轮询频率
        :param model:等待失败时,截图操作,图片文件中需要表达的功能标注
        :return:
        """
        try:
            if name == 'new':
                if cur_handles is not None:
                    self.logger.info("切换到最新打开的窗口")
                    WebDriverWait(self.driver, timeout, poll_frequency).until(EC.new_window_is_opened(cur_handles))
                    window_handles = self.driver.window_handles
                    self.driver.switch_to.window(window_handles[-1])
                else:
                    self.logger.exception("切换失败,没有要切换窗口的信息!!!")
                    self.save_webImgs("切换失败_没有要切换窗口的信息")
                    raise
            else:
                self.logger.info("切换到为 handles 的窗口")
                self.driver.swich_to.window(name)
        except:
            self.logger.exception("切换窗口失败!!!")
            # 截图
            self.save_webImgs("切换失败_没有要切换窗口的信息")
            raise

    def close_other_window(self, current_handle):
        """关闭除当前窗口外的所有窗口"""
        try:
            window_handles = self.driver.window_handles
            self.logger.exception("关闭除当前窗口外的所有窗口")
            for handle in window_handles:
                if handle == current_handle:
                    pass
                else:
                    try:
                        self.driver.switch_to.window(handle)
                        self.logger.exception(f"关闭窗口：{handle}")
                        self.driver.close()
                    except Exception as e:
                        self.logger.exception(f"关闭失败，失败窗口：{handle}，异常信息：{e}")
            self.driver.switch_to.window(current_handle)
        except Exception as e:
            self.logger.exception(f"关闭窗口失败，异常信息：{e}")

    def get_current_handle(self):
        """获取当前页面的handle"""
        try:
            current_handle = self.driver.current_window
            self.logger.info(f"获取当前页面handle:{current_handle}")
            return current_handle
        except Exception as e:
            self.logger.info(f"获取当前页面handle失败，异常信息:{e}")

    def get_current_link(self):
        """获取当前页面的link"""
        try:
            current_link = self.driver.current_url
            self.logger.info(f"获取当前页面link:{current_link}")
            return current_link
        except Exception as e:
            self.logger.info(f"获取当前页面link失败，异常信息:{e}")

    # 截图
    def save_webImgs(self, model=None):
        # filepath = 指图片保存目录/model(页面功能名称)_当前时间到秒.png
        # 截图保存目录
        # 拼接日志文件夹，如果不存在则自动创建
        base_path = BASE_PATH
        now_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        screenshot_path = os.path.join(base_path, f'/data/screenshot/{now_date}')
        if not os.path.exists(screenshot_path):
            os.mkdir(screenshot_path)
        # 当前时间
        dateNow = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
        # 路径
        filePath = '{}\\{}_{}.png'.format(screenshot_path, model, dateNow)
        try:
            self.driver.save_screenshot(filePath)
            self.logger.info(f"截屏成功,图片路径为{filePath}")
        except:
            self.logger.exception('截屏失败!')

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)
        self.logger.info("刷新页面...")

    def get_url(self, url):
        """打开网址并验证"""
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            self.logger.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    def back_to(self):
        """返回前一页"""
        try:
            self.driver.back()
            self.driver.implicitly_wait(10)
            self.logger.info("执行返回操作，返回上一页")
        except Exception as e:
            self.logger.info(f"返回操作失败，异常信息:{e}")

    def close_page(self):
        """返回前一页"""
        try:
            self.driver.close()
            self.driver.implicitly_wait(10)
            self.logger.info("关闭当前页面")
        except Exception as e:
            self.logger.info(f"关闭当前页面，异常信息:{e}")

    def get_cookies(self):
        """获取当前页面所有的cookie"""
        all_cookie = self.driver.get_cookies()
        self.logger.info(f"获取所有cookie{all_cookie}")
        return all_cookie

    def put_cookie(self, cookie):
        """注入cookie"""
        try:
            for i in cookie:
                self.driver.add_cookie(i)
            self.logger.info(f"注入cookie完成")
        except Exception as e:
            self.logger.info(f"添加cookie失败，异常信息：{e}")

    def move_to_click(self, loc, model=None):
        # 先查找元素
        ele = self.find_element(loc, model)
        try:
            self.logger.info(f'移动鼠标到"{model}"元素,元素定位:{loc}')
            AC(self.driver).move_to_element(ele).click().perform()
        except:
            self.logger.exception(f'移动鼠标到"{model}"元素失败,元素定位:{loc}')
            # 截图
            self.save_webImgs(f'移动鼠标到"{model}"元素异常')
            raise

    def _get_element(self, loc, model=None, time_out=10):
        start_time = time.time()
        while True:
            try:
                self.driver.implicitly_wait(30)
                web_element = self.driver.find_element(*loc)
                try:
                    self.height_light(web_element)
                except Exception:
                    pass
                return web_element
            except NoSuchElementException as n:
                time.sleep(0.5)
                if time.time() - start_time >= time_out:
                    raise NoSuchElementException(f"{time_out}秒后仍没有找到元素「{model}」:{n}")
            except WebDriverException as w:
                time.sleep(0.5)
                if time.time() - start_time >= time_out:
                    raise WebDriverException(f"{time_out}秒后浏览器仍异常「{model}」:{w}")
            except Exception as e:
                raise Exception(f"查找元素异常：{e}")

    def height_light(self, element):
        """
        元素高亮
        :param element:
        :return:
        """
        self.driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
                                   element, "border:2px solid red;")

    def scroll_page_to_element_visible(self, loc, model=None):
        """
        滚动页面至元素可见
        :return:
        """
        # 先查找元素
        ele = self.find_element(loc, model)
        try:
            self.logger.info(f'滑动屏幕到"{model}"元素可见，元素定位:{loc}')
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        except:
            self.logger.exception(f'滑动屏幕到"{model}"元素可见，元素定位:{loc}')
            # 截图
            self.save_webImgs(f'滑动屏幕到"{model}"元素异常')
            raise
