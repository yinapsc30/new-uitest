import os
from typing import Union


def get_env(name, base: Union[str, int] = ''):
    """
    从环境变量中获取指的信息
    @param name: 环境变量信息
    @param base: 默认信息
    @return:
    """
    return os.getenv(name) and os.getenv(name).strip() or base


BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_PATH, 'data')
SRC_PATH = os.path.join(BASE_PATH, 'src')
TOOL_PATH = os.path.join(SRC_PATH, 'tools')
# ALLURE_TOOL_PATH = os.path.join(TOOL_PATH, 'allure-2.14.0/bin')
# debug暂时写死，后续做成动态获取
ALLURE_TOOL_PATH = '/Users/soar/Downloads/allure-2.19.0/bin'

LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
TEST_PIC = os.path.join(REPORT_PATH, 'test_pic')
IMG_PATH = os.path.join(DATA_PATH, 'img')

for i in [LOG_PATH, REPORT_PATH, TEST_PIC]:
    if not os.path.exists(i):
        os.mkdir(i)

if __name__ == '__main__':
    print("BASE_PATH:", BASE_PATH)
    print("SRC_PATH:", SRC_PATH)
    print("TOOL_PATH:", TOOL_PATH)
    print("DATA_PATH:", DATA_PATH)
    print("IMG_PATH:", IMG_PATH)
