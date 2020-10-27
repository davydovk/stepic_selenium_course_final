from Stepic.stepic_selenium_course_final.pages.base_page import BasePage
from Stepic.stepic_selenium_course_final.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_login_url(self):
        assert '?promo=newYear' in self.browser.current_url, f"Url does not have '?promo=newYear', waiting url >>> " \
                                                             f"http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear, " \
                                                             f"current url >>> {self.browser.current_url}"

    def go_to_add_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        button.click()

    def should_be_basket_button_form(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON), "Button add basket is not presented"

    def should_be_product_add_basket_form(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADD_BASKET_FORM), "Product add basket form is not" \
                                                                                      " presented"

    def should_be_sum_basket_form(self):
        assert self.is_element_present(*ProductPageLocators.SUM_BASKET_FORM), "Sum basket form is not presented"

    def should_be_check_name_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME) == self.is_element_present(
            *ProductPageLocators.PRODUCT_ADD_BASKET_FORM), f"The wrong product was added to basket! correct product " \
                                                           f"{ProductPageLocators.PRODUCT_NAME}, product which was" \
                                                           f" added {ProductPageLocators.PRODUCT_ADD_BASKET_FORM}"

    def should_be_check_sum_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE) == self.is_element_present(
            *ProductPageLocators.SUM_BASKET_FORM), f"The price the basket incorrect! waiting price " \
                                                   f"{ProductPageLocators.PRODUCT_PRICE}, current price" \
                                                   f"{ProductPageLocators.SUM_BASKET_FORM}"
