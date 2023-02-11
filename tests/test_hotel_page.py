from time import sleep

from pages.hotel_page import  HOTELTRAVEL

def test_hotel(browser):
    testdate = HOTELTRAVEL(browser)
    testdate.load_page()
    sleep(4)
    testdate.select_hotel()
    testdate.type_hotel("Cluj")
    sleep(30)
    testdate.click_select_hotel()
    testdate.select_check_in()
    testdate.get_date_in("11")
    testdate.get_date_out(12)
    testdate.click_submit()
    sleep(4)

