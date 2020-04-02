from __future__ import unicode_literals
import bs4
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urllib.request import urlopen


def crawler():
    tStart = time.time()
    option = webdriver.ChromeOptions()								#設定selenium browser 為chorme
    option.headless = True											#設定不顯示視窗
    browser = webdriver.Chrome(options=option)                                  
    url = "https://www.taoyuan-airport.com/main_ch/revised_flight.aspx?uid=159&pid=12"      #桃機網站url
    unloaded = True
    while unloaded:
        try:
            browser.get(url)
            WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'tt_body')))     #等待網頁加載完成
            unloaded = False
            html_source = browser.page_source						#抓取加載完的網頁原始碼
            browser.quit()											#關閉browser
        except TimeoutException:
            print("timeout! auto retry!")							#超時(3s)會再試一次
            unloaded = True
    root = bs4.BeautifulSoup(html_source, "html5lib")
    flights = root.find("tbody", class_="tt_body").findAll("tr")	#找到存有資訊的表格再find所有航班(每個tr)
    flight_info = {													#flignt_info的dict
																	#key-> ['flight0']~['flight99']
    }
    count = 0
    for flight in flights:													#對每個航班都執行
        raw_flight_table_infos = flight.findAll("td", class_="flight-table-info")
        temp = ""
        if raw_flight_table_infos:											#如果有抓到該航班資訊
            airline_logos = raw_flight_table_infos[2].findAll("img")		#找logo的標籤
            airline_names = raw_flight_table_infos[2].findAll("span")		#找航空公司名稱
            flight_numbers = raw_flight_table_infos[3].findAll("span")		#找航班編號
            temp += raw_flight_table_infos[0].get_text() + "," \                
                + raw_flight_table_infos[1].get_text() + ","
            for airline_logo in airline_logos:
                temp += "https://www.taoyuan-airport.com" + airline_logo['src'] + " "
            temp = temp.rstrip()
            temp += ","
            for airline_name in airline_names:
                temp += airline_name.get_text() + " "	#拼成字串(每個欄位用','分隔，超過一個航空公司或航班編號時以' '分隔)
            temp = temp.rstrip()
            temp += ","
            for flight_number in flight_numbers:
                temp += flight_number.get_text() + " "
            temp = temp.rstrip()
            temp += ","
            temp += raw_flight_table_infos[4].get_text() + "," \
                + raw_flight_table_infos[8].get_text()
            flight_info['flight'+str(count)] = temp		#放入dict
            count += 1
            if count == 100:                            #收集 100 筆 flight_info
                break
    flight_info_jason = json.dumps(flight_info, ensure_ascii=False, separators=(',', ': '))
    print(flight_info_jason)
    with open('fi_out.json', 'w') as file:
        file.write(flight_info_jason)                   #輸出航班資訊的json
    tEnd = time.time()
    print("It cost %.2f sec" % (tEnd - tStart))
    return flight_info_jason                            #回傳所有航班資訊的json


crawler()
