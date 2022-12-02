
from behave import *

from pages.homePage import homePage
from pages.race_marketPage import race_marketPage
from pages.betSlipPage import betSlipPage

@given("user launches the web application")
def step_impl(context):
    print("---------Launch Browser-----------")
    url = context.url_web
    context.driver.get(url)
    context.driver.set_page_load_timeout(5)


@then('I click on first card under "Next to Jump" carousel')
def step_impl(context):
    print("----------Click on first card under next to jump carousel-------")
    context.fp = homePage(context.driver)
    context.fp.click_first_card_NTJ()
    # context.fp.click_first_market_NTJ()
    # context.fp.click_second_market_NTJ()


@step("I add 2 different bets into the Bet Slip by clicking on market button for a particular horse")
def step_impl(context):
    print("----------Select 2 different bets for a fixed market-------")
    context.rp = race_marketPage(context.driver)
    context.rp.click_first_market_NTJ()
    context.rp.click_second_market_NTJ()


@step("I check betslip to confirm the 2 bets placed")
def step_impl(context):
    print("----------Select 2 different bets for a fixed market-------")
    context.bs = betSlipPage(context.driver)
    context.bs.confirm_betslip()