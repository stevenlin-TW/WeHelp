import urllib.request as req
import bs4
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def getTitles(url, spoil):
    request = req.Request(url, headers={
        "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    html_text = bs4.BeautifulSoup(data, "html.parser")
    #print(html_text)
    titles = html_text.find_all("div", class_= "title")
    with open('movie.txt', 'a', newline='', encoding='utf-8') as file:
        for title in titles:
            if title.a != None and title.a.string[1:3] == spoil:
                file.write(title.a.string + '\n')
    
    next_page = html_text.find("a", string="‹ 上頁")
    return next_page.get("href")

spoils = ["好雷", "普雷", "負雷"]
for spoil in spoils:
    url = "https://www.ptt.cc/bbs/movie/index.html"
    for i in range(10):
        url = "https://www.ptt.cc" + getTitles(url, spoil)