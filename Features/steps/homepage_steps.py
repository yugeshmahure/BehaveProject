import time

from behave import *

from Pages.homePage import homePage
from utils import configReader


@given(u'the user is navigates to makemytrip')
def navigate_to_homepage(context):
    context.homepage = homePage(context.driver)
    context.homepage.open(configReader.readConfig("basic info", "testsiteurl"))


@when(u'the user enters search text for hotel search')
def navigate_to_homepage(context):
    context.homepage.enter_search_text("Maldives")


@when(u'the user selects destination city')
def navigate_to_homepage(context):
    pass


@when(u'the user clicks on hotel tab')
def step_impl(context):
    context.homepage.click_hotel_tab()

