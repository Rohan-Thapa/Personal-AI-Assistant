from bs4 import BeautifulSoup
from urllib.request import urlopen

news_url = "https://news.google.com/news/rss"
Client = urlopen(news_url)
xml_page = Client.read()
Client.close()

soup_page = BeautifulSoup(xml_page, "xml")
news_list = soup_page.findAll("item")
print("Here are top 5 news")

for news in news_list[:5]:
    print("> "+news.title.text)
