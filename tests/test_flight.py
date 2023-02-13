from time import sleep

from pages.flight_page import flight
from pages.hotel_page import HOTELTRAVEL

def test_flight(browser):
    testflight = flight(browser)
    hotel_page = HOTELTRAVEL(browser)
    hotel_page.load_page()
    sleep(10)
    testflight.click_tab_flight()
    testflight.from_airport("dubai")
    testflight.destination("colombo")
    testflight.date("01-03-2023")
    sleep(4)
    testflight.click_search()
    sleep(10)