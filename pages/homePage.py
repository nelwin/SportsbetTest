from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class homePage(BasePage):
    # Locators

    FIRST_CARD_NTJ = (By.XPATH,'//div[@data-automation-id="home-tabs-container"]//following-sibling::div[1]/div[2]/div[2]/div/div/following-sibling::div[1]')
    MARKET_FIRST_NTJ = (By.XPATH,'//*[@id="base"]//div[@data-automation-id="racecard-body"]/div[2]//div[@data-automation-id="racecard-outcome-0-L-price"]')
    MARKET_SECOND_NTJ = (By.XPATH,'//*[@id="base"]//div[@data-automation-id="racecard-body"]/div[3]//div[@data-automation-id="racecard-outcome-0-L-price"]')


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
