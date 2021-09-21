from vally_qups.Locators.locators import Locators


class ProductBrands:
    def __init__(self, driver):
        self.driver = driver
        self.close_popup = Locators.popup_close
        self.speaker_brand = Locators.speaker_brand_page_xpath

    def click_speaker(self):
        self.driver.find_element_by_xpath(self.speaker_brand).click()

    def close_popup_button(self):
        self.driver.find_element_by_xpath(self.close_popup).click()
