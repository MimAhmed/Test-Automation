from vally_qups.Locators.locators import Locators


class CareerPage:
    def __init__(self, driver):
        self.driver = driver
        self.close_popup = Locators.popup_close
        self.speaker_brand = Locators.speaker_brand_page_xpath
        self.career_tab = Locators.career_tab_xpath

    def close_popup_button(self):
        self.driver.find_element_by_xpath(self.close_popup).click()

    def click_tab(self):
        self.driver.find_element_by_xpath(self.career_tab).click()

    def check_email(self):
        email = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[1]/div[2]/p/a")
        email_id = email.get_attribute('href')
        print(email_id)
        domain_check = "@evaly.com.bd" in email_id
        print(domain_check)
