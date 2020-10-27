from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')


class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.ID, 'add_to_basket_form')
    PRODUCT_PRICE = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/article/table/tbody/tr[4]/td')
    PRODUCT_NAME = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/h1')
    PRODUCT_ADD_BASKET_FORM = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    SUM_BASKET_FORM = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
