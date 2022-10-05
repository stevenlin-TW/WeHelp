import urllib.request as req
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with req.urlopen(url) as response:
    data = json.load(response)
#print(sites['result']['results'][0]['address'][5:8])

sites = data['result']['results']
#print(type(sites[2]['file']))

district = ('中正區','萬華區','中山區','大同區','大安區','松山區','信義區','士林區','文山區','北投區','內湖區','南港區')
# 景點名稱、區域、經度、緯度、第一張圖檔網址
# key_list = ['stitle','address','longitude','latitude','file']

with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    for site in sites:
        year = int(site['xpostDate'][0:4])
        dis = site['address'][5:8]
        if year>=2015 and dis in district:
            first_pic = []
            x = 0
            while True:
                if site['file'][x:x+2] == 'gh' or site['file'][x:x+2] == 'Gh':
                    first_pic.append(site['file'][x])
                    break
                else:
                    first_pic.append(site['file'][x])
                    x += 1
            file.write(site['stitle'] + ',' + dis + ',' + site['longitude'] + ',' + site['latitude'] + ',' + ''.join(first_pic) + '\n')
