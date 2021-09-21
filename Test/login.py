from selenium import webdriver
import time
import unittest
from vally_qups.Pages.login_page import LoginPage
from vally_qups.Locators import locators
import HtmlTestRunner


class LoginTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/driver/chromedriver_win32_93/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_user_login(self):
        driver = self.driver
        driver.get(locators.BASE_URl)
        login = LoginPage(driver)
        login.close_popup_button()
        login.login_icon_click()
        login.enter_username("01963068116")
        login.enter_password("EaNt6HzQEnQgWHE1*")
        login.click_login()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Joy/PycharmProjects/simplePOM/simplepomprojects/Reports'))

