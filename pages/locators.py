from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    # BASKET_LINK = (By.CSS_SELECTOR, 'a.btn.btn-default')
    BASKET_LINK = (By.CSS_SELECTOR, "span[class='btn-group'] a")


class BasketPageLocators():
    ITEMS_TO_BUY_NOW = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner')


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner > strong')
    BASKET_PRICE = (By.CSS_SELECTOR, 'div.alert div p strong')
