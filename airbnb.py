#-*- coding: utf-8 -*-
import sys
import re
import time

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

date_list = [ ["2023-11-01", "2023-11-07"] , ["2023-11-08",  "2023-11-14"] , ["2023-11-15",  "2023-11-21"] , ["2023-11-22",  "2023-11-28"] ,
               ["2023-11-29", "2023-12-05"] , ["2023-12-06",  "2023-12-12"] , ["2023-12-13",  "2023-12-19"] , ["2023-12-20",  "2023-12-26"]  ]


# selenium 로 브라우저에 접속

options = webdriver.FirefoxOptions()
#options.headless = True
	
browser = webdriver.Firefox(options=options)

for adate, bdate in date_list :
    airbnb_page = "https://www.airbnb.co.kr/s/%EC%84%9C%EC%9A%B8-%EC%84%A0%EB%A6%89%EC%97%AD/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-11-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=6&channel=EXPLORE&date_picker_type=calendar&checkin=" + adate + "&checkout=" + bdate + "&source=structured_search_input_header&search_type=user_map_move&query=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EC%84%A0%EB%A6%89%EC%97%AD%EC%82%AC%EA%B1%B0%EB%A6%AC&place_id=ChIJFyslkQ-kfDURFbXTpsrYtFY&ne_lat=37.51476771497842&ne_lng=127.05650396860659&sw_lat=37.49729295953138&sw_lng=127.04103700396513&zoom=15.480171715329027&zoom_level=15.480171715329027&search_by_map=true"
        
    browser.get(airbnb_page)

    time.sleep(2)
        
    soup = BeautifulSoup(browser.page_source, features="html.parser")
    cols = soup.findAll( 'span' )
        
    time.sleep(2)

    for col in cols:
        if "검색 결과" in col.text and "숙소" in col.text:
            print (adate + " " + col.text)

#browser.quit()


