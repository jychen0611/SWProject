# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:38:29 2020

@author: acer
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 19:47:31 2020

@author: 呂兆凱//BBC news Coronavirus新聞標題、連結、圖片
"""

def CoronavirusTopic():
    import urllib.request as req
    import json
    
    url="https://www.bbc.com/zhongwen/trad/51222586"
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    })
    
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
        
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    
    titles=root.find_all("span", class_="title-link__title-text") 
    links=root.find_all("a", class_="title-link")
    images=root.find_all("div", class_="js-delayed-image-load")

    dict={}
    i=0    
    
    for title in titles:
        dict[title.string]=[images[i]['data-src'], "https://www.bbc.com"+links[i]['href']]
        i=i+1

    # store into a file
    with open('./src/data.json', 'w') as outfile:
        json.dump(dict, outfile)

    # bbc_json=json.dumps(dict, ensure_ascii=False)
    # return(bbc_json)

if __name__ == "__main__":
    import json
    CoronavirusTopic()
