from selenium import webdriver
import time
import unittest
from vally_qups.Pages.career_page import CareerPage
from vally_qups.Locators import locators
import HtmlTestRunner


class BrandPageTest(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/driver/chromedriver_win32_93/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_career_page(self):
        driver = self.driver
        driver.get(locators.Career_URL)
        career = CareerPage(driver)
        career.close_popup_button()
        time.sleep(2)
        career.click_tab()
        career.check_email()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Joy/PycharmProjects/evally/vally_qups/Reports'))
