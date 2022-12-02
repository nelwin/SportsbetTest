from selenium.webdriver.common.by import By

from pages.basePage import BasePage


class race_marketPage(BasePage):
    # Locators


    MARKET_FIRST_NTJ = (By.XPATH,'//*[@id="base"]//div[@data-automation-id="racecard-body"]/div[2]//div[@data-automation-id="racecard-outcome-0-L-price"]')
    MARKET_SECOND_NTJ = (By.XPATH,'//*[@id="base"]//div[@data-automation-id="racecard-body"]/div[3]//div[@data-automation-id="racecard-outcome-0-L-price"]')
    MARKET_FIRST_NTJ_TEXT = (By.XPATH,'//*[@id="base"]//div[@data-automation-id="racecard-body"]/div[2]//div[@data-automation-id="racecard-outcome-name"]/span')
    MARKET_SECOND_NTJ_TEXT = (By.XPATH,'//*[@id="base"]//div[@data-automation-id="racecard-body"]/div[3]//div[@data-automation-id="racecard-outcome-name"]/span')
    race_market_names=[]

    def __init__(self, driver):
        super().__init__(driver)



    def click_first_market_NTJ(self):
        super().wait_for_element_to_be_visible(race_marketPage.MARKET_FIRST_NTJ)

        element = self.find_element(*race_marketPage.MARKET_FIRST_NTJ)
        element.click()
        text= self.find_element(*race_marketPage.MARKET_FIRST_NTJ_TEXT).text
        print(text)
        race_marketPage.race_market_names.append(text)
        print("First bet for fixed market selected")

    def click_second_market_NTJ(self):
        super().wait_for_element_to_be_visible(race_marketPage.MARKET_SECOND_NTJ)

        element = self.find_element(*race_marketPage.MARKET_SECOND_NTJ)
        element.click()
        text = self.find_element(*race_marketPage.MARKET_SECOND_NTJ_TEXT).text
        print(text)
        race_marketPage.race_market_names.append(text)
        print("Second bet for fixed market selected")
        print(race_marketPage.race_market_names)

