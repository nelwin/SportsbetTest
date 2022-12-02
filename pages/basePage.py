from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def wait_for_element_to_be_visible(self, locator):
        try:
            WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_element_located(locator))
        except Exception as ex:
            print(ex)
