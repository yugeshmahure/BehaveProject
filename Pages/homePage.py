from Pages.BasePage import BasePage


class homePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def open(self, url):
        self.driver.get(url)

    def click_hotel_tab(self):
        self.click("hotel_tab_class")

    def enter_search_text(self, city_name):
        self.type("city_field_ID", city_name)