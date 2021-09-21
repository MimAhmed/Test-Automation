from vally_qups.Locators.locators import Locators


class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.close_popup = Locators.popup_close
        self.click_login_icon = Locators.login_icon_xpath
        self.username_textbox_phone = Locators.username_textbox_xpath
        self.password_textbox_pass = Locators.password_textbox_xpath
        self.login_button = Locators.login_button_xpath

    def login_icon_click(self):
        self.driver.find_element_by_xpath(self.click_login_icon).click()

    def enter_username(self, username):
        self.driver.find_element_by_name(self.username_textbox_phone).clear()
        self.driver.find_element_by_name(self.username_textbox_phone).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_pass).clear()
        self.driver.find_element_by_name(self.password_textbox_pass).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button).click()

    def close_popup_button(self):
        self.driver.find_element_by_xpath(self.close_popup).click()
