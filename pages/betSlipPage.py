from selenium.webdriver.common.by import By

from pages import race_marketPage
from pages.basePage import BasePage


class betSlipPage(BasePage):
    # Locators

    # BETSLIP_BTN = (By.XPATH,'//*[@id="base"]/div/div[2]/div/div[1]/div/header/button[2]') --old
    BETSLIP_BTN = (By.XPATH, '//span[@data-automation-id="header-bet-count"]')
    BETSLIP_BETPLACED_RACE_TEXT = (By.XPATH,'//*[@id="base"]/div//span[@data-automation-id="betslip-bet-title"]')
    BETSLIP_HIDE = (By.XPATH,'//i[@data-automation-id="betslip-header-hide"]')

    race_list=[]

    def __init__(self, driver):
        super().__init__(driver)



    def confirm_betslip(self):
        super().wait_for_element_to_be_visible(betSlipPage.BETSLIP_BTN)
        element_text = self.find_elements(*betSlipPage.BETSLIP_BETPLACED_RACE_TEXT)
        for e in element_text:
            betSlipPage.race_list.append(e.text)
        print(betSlipPage.race_list)
        for e1 in betSlipPage.race_list:
            for e2 in race_marketPage.race_marketPage.race_market_names:
              if e2 in e1:
                assert True
                break
            else:
              assert False
    def hide_betslip(self):
        super().wait_for_element_to_be_visible(betSlipPage.BETSLIP_HIDE)
        self.find_element(*betSlipPage.BETSLIP_HIDE).click()

    def click_betslip_btn(self):
        super().wait_for_element_to_be_visible(betSlipPage.BETSLIP_BTN)
        self.find_element(*betSlipPage.BETSLIP_BTN).click()