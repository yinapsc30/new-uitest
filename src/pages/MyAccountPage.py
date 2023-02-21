import itertools
import re
import time
from src.utils.elementoperator import BasePage
from selenium.webdriver.common.by import By
from src.page_element.MyAccountPageEle import MyAccountElement
from src.utils.sqloperator import execute_sql


class MyAccountPageOperation(BasePage):

    def open_url(self, url):
        self.get_url(url)

    def 