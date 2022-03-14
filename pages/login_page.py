from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'In url not found "login" path'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.AUTH_FORM), 'Login form not found'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), 'Registration form not found'

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FIELD)
        password_field.send_keys(password)

        repeat_password_field = self.browser.find_element(*LoginPageLocators.REG_REPEAT_PASSWORD_FIELD)
        repeat_password_field.send_keys(password)

        submit_button = self.browser.find_element(*LoginPageLocators.REG_SUBMIT_BUTTON)
        submit_button.click()
