
import os
import pydash
import yaml
from assertpy import assert_that

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.utils import ChromeType


def before_all(context):
    print("\n################### BEFORE ALL ##################")
    yaml.warnings({'YAMLLoadWarning': False})
    env = os.getenv('ENV', 'dev')
    env = env.lower() if len(env) > 0 else 'dev'

    print(f"USING ENVIROMENT:{env}")
    with open(os.path.join(os.path.dirname(__file__), "../config/config.yaml")) as f:
        environs = yaml.safe_load(f.read())
        print(f"\n Environments YAML: {environs}")

    assert_that(pydash.has(environs, env), f'No ENV found in YAML for {env}').is_true()

    context.envname = env
    context.env = environs[env]

    # set all root objects in environment.py to context

    for root_obj in environs:
        setattr(context, root_obj, environs[root_obj])

    context.url_web = context.env.get('url_web')
    context.browser = context.env.get('browser')

    print(f"url_web => {context.url_web}")


def before_scenario(context, driver):
    print("---------Before Scenario------")
    browser = pydash.get(context.env, 'browser')
    if browser.lower() == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=420*1080")
        options.add_argument("--disable-pop-blocking")
        options.add_argument("--enable-javascript")
        options.add_argument("--disable-extentions")


        context.driver = webdriver.Chrome(executable_path=ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install(),
                                          options=options)

    elif browser.lower() == "Firefox":
        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    context.driver.implicitly_wait(2)
    # context.driver.maximize_window()



def after_scenario(context, driver):
    print("------After Scenario-----")
    context.driver.close()
    context.driver.quit()



