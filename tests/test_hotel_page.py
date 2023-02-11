from datetime import datetime, timedelta
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
    # start_date = "12-02-2023"
    # date_1 = datetime.strptime(start_date, '%m-%d-%Y')
    # date_2 = date_1+timedelta(days=20)
    # end_date = datetime.strptime(date_2,'%d-%m-%Y')
    testdate.get_select_check_in("12-02-2023")
    testdate.date_check_out("20-02-2023")
    sleep(4)
    testdate.click_submit()
    sleep(30)

