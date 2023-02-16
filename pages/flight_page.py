
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class flight:
    # PRELOADER = (By.ID,"preloader")
    TAB_FLIGHT = (By.CSS_SELECTOR,"#flights-tab")
    ROUND_TRIP = (By.CSS_SELECTOR,"#flights > form > div.row.mb-3.g-1 > div.col-md-4.flight_types > div > div:nth-child(2)")
    FROM_AIRPORT = (By.CSS_SELECTOR,"#autocomplete")
    DESTINATION = (By.CSS_SELECTOR,"#autocomplete2")
    DATE_DEPARTURE = (By.CSS_SELECTOR,"#departure")
    DATE_RETURN = (By.CSS_SELECTOR,"#return")
    SEARCH = (By.ID,"flights-search")
    RESULT = (By.CLASS_NAME,"sec__title_list")

    def __init__(self, browser):
        self.browser = browser

    # def click_preloader(self):
    #     self.browser.find_element(*self.PRELOADER).is_disabeld()

    def click_tab_flight(self):
        self.browser.find_element(*self.TAB_FLIGHT).click()

    def check_round_trip(self):
        self.browser.find_element(*self.ROUND_TRIP).click()


    def from_airport(self,text):
        self.browser.find_element(*self.FROM_AIRPORT).send_keys(text)

    def destination(self,text):
        self.browser.find_element(*self.DESTINATION).send_keys(text)

    def date_departure(self,date):
        date_departure = self.browser.find_element(*self.DATE_DEPARTURE)
        date_departure.clear()
        date_departure.send_keys(date)
        date_departure.click()

    def date_return(self,date):
        date_return = self.browser.find_element(*self.DATE_RETURN)
        date_return.clear()
        date_return.send_keys(date)
        date_return.click()
    def click_search(self):
        self.browser.find_element(*self.SEARCH).click()

    def wait_for_web(self):
       WebDriverWait(self.browser,30).until(EC.element_to_be_clickable(self.TAB_FLIGHT))
       # WebDriverWait(self.browser,10).until(EC.element_to_be_clickable(self.SEARCH))

    def get_result(self):
        return self.browser.find_element(*self.RESULT).text