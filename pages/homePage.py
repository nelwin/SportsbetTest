from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class homePage(BasePage):
    # Locators


    FIRST_CARD_NTJ = (By.XPATH,'//div[@data-automation-id="group-1-carousel-1-body-container"]//div')
    MARKET_FIRST_NTJ = (By.XPATH,'//div[@data-automation-id="racecard-body"]//following-sibling::div[1]//following-sibling::div[1]/div[1]')
    MARKET_SECOND_NTJ = (By.XPATH,'//div[@data-automation-id="racecard-body"]//following-sibling::div[2]//following-sibling::div[1]/div[1]')


    def __init__(self, driver):
        super().__init__(driver)


    def click_first_card_NTJ(self):
        super().wait_for_element_to_be_visible(homePage.FIRST_CARD_NTJ)

        element = self.find_element(*homePage.FIRST_CARD_NTJ)
        element.click()


    def click_first_market_NTJ(self):
        super().wait_for_element_to_be_visible(homePage.MARKET_FIRST_NTJ)

        element = self.find_element(*homePage.MARKET_FIRST_NTJ)
        element.click()


    def click_second_market_NTJ(self):
        super().wait_for_element_to_be_visible(homePage.MARKET_SECOND_NTJ)

        element = self.find_element(*homePage.MARKET_SECOND_NTJ)
        element.click()
