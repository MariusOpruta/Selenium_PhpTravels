from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class HOTELTRAVEL:
    SELECT_HOTEL_SEARCH = (By.ID,"select2-hotels_city-container")
    SEARCH_HOTEL = (By.CLASS_NAME,"select2-search__field")
    SELECT_CHECK_IN = (By.ID,"checkin")
    DATES_IN = (By.CSS_SELECTOR,"#checkin")
    DATES_OUT = (By.CSS_SELECTOR,"#checkout")
    SELECT_CHECK_OUT = (By.ID,"checkout")
    BUTTON_SUBMIT = (By.CSS_SELECTOR,"#submit")
    RESULT = (By.CLASS_NAME,"sec__title_list")
    URL = "https://phptravels.net"

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def select_hotel(self):
        self.browser.find_element(*self.SELECT_HOTEL_SEARCH).click()

    def type_hotel(self,hotel):
        self.browser.find_element(*self.SEARCH_HOTEL).send_keys(hotel)

    def click_select_hotel(self):
        self.browser.find_element(*self.SEARCH_HOTEL).send_keys(Keys.ENTER)

    def select_check_in(self):
        self.browser.find_element(*self.SELECT_CHECK_IN).click()

    def date_in(self,data):
        check_in = self.browser.find_element(*self.DATES_IN)

        # check_in.clear()
        check_in.send_keys(data)
        check_in.click()

    def select_check_out(self):
        self.browser.find_element(*self.SELECT_CHECK_OUT).click()

    def date_out(self,date):
        check_out = self.browser.find_element(*self.DATES_OUT)
        # check_out.clear()
        check_out.send_keys(date)
        check_out.click()

    def get_result(self):
        return self.browser.find_element(*self.RESULT).text



    def click_submit(self):
        self.browser.find_element(*self.BUTTON_SUBMIT).click()




