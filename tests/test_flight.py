from datetime import datetime, timedelta
from time import sleep

from pages.flight_page import flight
from pages.hotel_page import HOTELTRAVEL

def test_flight(browser):
    testflight = flight(browser)
    hotel_page = HOTELTRAVEL(browser)
    hotel_page.load_page()
    sleep(10)
    # testflight.wait_for_web()
    testflight.click_tab_flight()
    testflight.check_round_trip()
    testflight.from_airport("dubai")
    testflight.destination("colombo")
    specific_date = datetime(2023, 3, 1)
    testflight.date_departure(str(specific_date))
    testflight.date_return(str(specific_date+timedelta(20)))
    testflight.click_search()
    assert "DUBAI COLOMBO" in testflight.get_result()
    # sleep(5)