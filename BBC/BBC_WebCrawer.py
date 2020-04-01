# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:33:49 2020

@author: 呂兆凱
"""

def CoronavirusTopic():
    """ 程式碼開始 """
    '''
    爬蟲
    '''
    import urllib.request as req
        
    url="https://www.bbc.com/zhongwen/trad/51222586"
    request=req.Request(url, headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    '''
    解析爬下來的文字
    '''
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
        
    titles=root.find_all("span", class_="title-link__title-text") 
    links=root.find_all("a", class_="title-link")
    images=root.find_all("div", class_="js-delayed-image-load")

    '''
    讀取data.json
    若無此檔案，則建立空的dict
    '''
    import pathlib, os, json
    curPath=str(pathlib.Path(__file__).parent.absolute())
    dict={}
    if os.path.exists(curPath + "/src/data.json"):
        with open(curPath + '/src/data.json', 'r') as f:
            dict = json.load(f)

    '''
    把不重複的資訊放進dict內
    dict = {標題: [圖片位置，新聞網址，對應的圖片連結]}
    (忽略重複的標題)
    '''
    i=len(dict)
    for j, title in enumerate(titles):
        titles[j] = title.string
        if dict.get(titles[j], 0) == 0: #title內容為空才放網址
            dict[titles[j]]=[curPath + '/picture/' + str(i) + '.png', "https://www.bbc.com"+links[i]['href'], images[j]['data-src']]
            i=i+1

    '''
    下載還未載過的圖片
    '''
    import requests
    count = 1
    for i in range(len(titles)):
        save_path = dict[titles[i]][0]
        if not os.path.exists(save_path): #已存過圖片不再存 & 圖片總數=titles數
            url=dict[titles[i]][2]
            request=requests.get(url)
            file_name = save_path
            f=open(file_name,'wb')
            f.write(request.content)
            f.close()
            print("Picture ", count, "downloaded !")
            count += 1

    '''
    把已經不存在的title從dict和檔案中刪除
    '''
    # dict["example"] = [curPath + '/picture/' + "example.txt"] # for test, 在picture資料夾內新增一個example.txt
    titles = set(titles) # 去除重複的titles
    to_delete_title = titles ^ dict.keys() # return set(不存在的titles)
    print(to_delete_title)
    for tmp in to_delete_title:
        os.remove(dict[tmp][0])
        del dict[tmp]
        print("delete Title = ", tmp)

    '''
    把dict存成data.json
    '''
    with open(curPath + '/src/data.json', 'w') as outfile:
        json.dump(dict, outfile)
    
if __name__ == "__main__":
    import json
    CoronavirusTopic()
    

    
