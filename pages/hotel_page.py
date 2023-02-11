from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class HOTELTRAVEL:
    SELECT_HOTEL_SEARCH = (By.ID,"select2-hotels_city-container")
    SEARCH_HOTEL = (By.CLASS_NAME,"select2-search__field")
    SELECT_CHECK_IN = (By.ID,"checkin")

    DATES_IN = (By.XPATH, "//div[@id='checkin']//tbody//td[@class='day  active']")
    # DATES_IN = (By.CSS_SELECTOR,"#fadein > div:nth-child(30) > div.datepicker-days > table > tbody > tr:nth-child(3) > td.day.active")
    DATES_OUT = (By.XPATH, "//div[@id='checkout']//tbody//td[@class!='day disabled old']")
    SELECT_CHECK_OUT = (By.ID, "checkout")
    BUTTON_SUBMIT = (By.CSS_SELECTOR,"#submit")
    URL = "https://phptravels.net/"

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

    def get_date_in(self,element):
        all_dates = self.browser.find_elements(*self.DATES_IN)
        all_dates.send_keys(element)
        # for date in all_dates:
        #     if date.text == element:
        #         date.click()
        #         break

    def get_date_out(self,elemment):
        all_dates_out = self.browser.find_elements(*self.DATES_OUT)
        for element in all_dates_out:
            if element.get_atribute('day ') == elemment+20:
                print(all_dates_out.text)
                element.submit()
                break


    def click_submit(self):
        self.browser.find_element(*self.BUTTON_SUBMIT).click()



