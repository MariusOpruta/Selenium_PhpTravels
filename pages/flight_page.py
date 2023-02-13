from selenium.webdriver.common.by import By

class flight:
    TAB_FLIGHT = (By.CSS_SELECTOR,"#flights-tab")
    FROM_AIRPORT = (By.CSS_SELECTOR,"#autocomplete")
    DESTINATION = (By.CSS_SELECTOR,"#autocomplete2")
    DATE = (By.CSS_SELECTOR,"#departure")
    SEARCH = (By.ID,"flights-search")

    def __init__(self, browser):
        self.browser = browser

    def click_tab_flight(self):
        self.browser.find_element(*self.TAB_FLIGHT).click()

    def from_airport(self,text):
        self.browser.find_element(*self.FROM_AIRPORT).send_keys(text)

    def destination(self,text):
        self.browser.find_element(*self.DESTINATION).send_keys(text)

    def date(self,date):
        self.browser.find_element(*self.DATE).send_keys(date)

    def click_search(self):
        self.browser.find_element(*self.SEARCH).click()

