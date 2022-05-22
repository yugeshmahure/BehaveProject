import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils import configReader

print("value from config", configReader.readConfig("basic info","browser") == "firefox")

def before_scenario(context, driver):
    if configReader.readConfig("basic info","browser") == "chrome":
        context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    if configReader.readConfig("basic info","browser") == "firefox":
        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


# def after_scenario(context, driver):
#     time.sleep(10)
#     context.driver.quit()