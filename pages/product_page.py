from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'Add to basket not found in page'

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_add_basket_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADD_BASKET_MESSAGE), 'Success add basket message ' \
                                                                                         'not found '

    def should_not_be_basket_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADD_BASKET_MESSAGE), 'Success basket message ' \
                                                                                             'is present, but should ' \
                                                                                             'not be '

    def should_not_be_basket_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADD_BASKET_MESSAGE), 'Success basket message ' \
                                                                                             'is present and not ' \
                                                                                     'disappeared '

    def should_be_price_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_BASKET_MESSAGE), 'Price basket message not found'

    def is_success_add_basket_message_valid(self):
        name_product_in_mess = self.browser.find_element(*ProductPageLocators.SUCCESS_ADD_BASKET_MESSAGE_PRODUCT_NAME)
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert name_product.text == name_product_in_mess.text, 'Name product in basket message invalid'

    def is_price_basket_message_valid(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_product_in_mess = self.browser.find_element(*ProductPageLocators.PRICE_BASKET_MESSAGE_PRICE_VALUE)
        assert price_product.text == price_product_in_mess.text, 'Price product in basket message invalid'
