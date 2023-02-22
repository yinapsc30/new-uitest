from selenium.webdriver.common.by import By


class LoginElement:

    EMAIL = (By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div[2]/div/div[3]/div/div/div/div/input')
    PASSWORD = (By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div[2]/div/div[4]/div/div/div/div/span/input')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div[2]/div/div[7]/div/div/div/div/button')

    ACCOUNT_EMAIL = (By.XPATH, '//*[@id="__next"]/main/div/div[1]/div[1]/div[3]/span[2]')
    BALANCE_ACCOUNT = (By.XPATH, '//*[@id="__div_id_header"]/div/div[3]/div/div[2]')
