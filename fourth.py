# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 14:02:04 2020

@author: 魏湧致 / 世界和台灣確診與死亡人數
"""

def Web_Crawler():
    Total_case = open('Coronavirus_Cases.txt', 'wt', encoding="utf-8")
    Countries_two = open('Countries.txt', 'wt', encoding="utf-8")
    TotalCases = open('TotalCases.txt', 'wt', encoding="utf-8")
    NewCases = open('NewCases.txt', 'wt', encoding="utf-8")
    TotalDeaths = open('TotalDeaths.txt', 'wt', encoding="utf-8")
    NewDeaths = open('NewDeaths.txt', 'wt', encoding="utf-8")
    TotalRecovered = open('TotalRecovered.txt', 'wt', encoding="utf-8")
    ActiveCases = open('ActiveCases.txt', 'wt', encoding="utf-8")
    SeriousCritical = open('SeriousCritical.txt', 'wt', encoding="utf-8")
    TotCases1M = open('TotCases1M.txt', 'wt', encoding="utf-8")
    TotDeaths1M = open('TotDeaths1M.txt', 'wt', encoding="utf-8")
    
    import urllib.request as req
    url = "https://www.worldometers.info/coronavirus/#countries"
    request = req.Request(url, headers={
            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    
    Coronavirus_Cases = root.find_all("div", class_="maincounter-number")
    for maincounter_number in Coronavirus_Cases:
        Total_case.write(str(maincounter_number.span.string))
        Total_case.write("\n")
        
    Countries = root.find_all("td", style="font-weight: bold; font-size:15px; text-align:left;")
    Main = root.find_all("td")
    
    china=[]
    for i in range(9):
        china.append(str(Main[(int)(len(Main)/2)-19+i].string) )
    china_num = china[0].split(',')
    
    Count = [0,1,2,3,4,5,6,7,8,9,10]
    check_re=0
    for Country in Countries:
        if Country.string == "China":
            break
        check=0
        country_num = str(Main[ Count[1] ].string).split(',')
        if check_re == 1:
            check=0
        elif len(china_num) > len(country_num):
            check=1
            check_re=1
        elif len(china_num) == len(country_num):
            for i in range(len(china_num)):
                check=0
                if int(china_num[i]) > int(country_num[i]):
                    check=1
                    check_re=1
                    break
                elif int(china_num[i]) < int(country_num[i]):
                    break
        if check == 1:
            Countries_two.write("China"+"\n")
            TotalCases.write(china[0]+"\n")
            NewCases.write(china[1]+"\n")
            TotalDeaths.write(china[2]+"\n")
            NewDeaths.write(china[3]+"\n")
            TotalRecovered.write(china[4]+"\n")
            ActiveCases.write(china[5]+"\n")
            SeriousCritical.write(china[6]+"\n")
            TotCases1M.write(china[7]+"\n")
            TotDeaths1M.write(china[8]+"\n")
            
        Countries_two.write(str(Country.string)+"\n")
        TotalCases.write(str(Main[ Count[1] ].string)+"\n")
        NewCases.write(str(Main[ Count[2] ].string)+"\n")
        TotalDeaths.write(str(Main[ Count[3] ].string)+"\n")
        NewDeaths.write(str(Main[ Count[4] ].string)+"\n")
        TotalRecovered.write(str(Main[ Count[5] ].string)+"\n")
        ActiveCases.write(str(Main[ Count[6] ].string)+"\n")
        SeriousCritical.write(str(Main[ Count[7] ].string)+"\n")
        TotCases1M.write(str(Main[ Count[8] ].string)+"\n")
        TotDeaths1M.write(str(Main[ Count[9] ].string)+"\n")
        for i in range(10):
            Count[i] = Count[i]+10
    
    Total_case.close()
    Countries_two.close()
    TotalCases.close()
    NewCases.close()
    TotalDeaths.close()
    NewDeaths.close()
    TotalRecovered.close()
    ActiveCases.close()
    SeriousCritical.close()
    TotCases1M.close()
    TotDeaths1M.close()
#Web_Crawler()