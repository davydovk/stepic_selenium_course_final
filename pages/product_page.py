from Stepic.stepic_selenium_course_final.pages.base_page import BasePage
from Stepic.stepic_selenium_course_final.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_login_url(self):
        assert '?promo=newYear' in self.browser.current_url, f"Url does not have '?promo=newYear', waiting url >>> " \
                                                             f"http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear, " \
                                                             f"current url >>> {self.browser.current_url}"

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_add_to_basket(self):
        self.should_be_message()
        self.should_be_right_price()

    def should_be_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MESSAGE).text
        print(product_name, message)
        assert product_name == message, f'{product_name} is not {message}'

    def should_be_right_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        print(product_price, basket_price)
        assert product_price == basket_price, f"{product_price} not equal {basket_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), \
            "Success message is presented, but should not be"
