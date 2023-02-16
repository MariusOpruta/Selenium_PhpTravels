from datetime import datetime, timedelta
from time import sleep

from pages.hotel_page import  HOTELTRAVEL

def test_hotel(browser):
    testdate = HOTELTRAVEL(browser)
    testdate.load_page()
    sleep(4)
    testdate.select_hotel()
    testdate.type_hotel("Barcelona")
    sleep(15)
    testdate.click_select_hotel()
    testdate.select_check_in()
    specific_date = datetime(2023, 3, 1)
    testdate.date_in(str(specific_date))
    testdate.select_check_out()
    testdate.date_out(str(specific_date+timedelta(20)))
    sleep(4)
    testdate.click_submit()
    sleep(4)
    assert "SEARCH HOTELS IN BARCELONA" in testdate.get_result()
