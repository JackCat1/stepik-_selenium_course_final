from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_not_be_basket_item(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket item is present on page, but not "\
                                                                             "be "

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Message about empty basket should be on page"
