from bs4 import BeautifulSoup
from urllib2 import urlopen
from pprint import pprint

BASE_URL = "http://www.chicagoreader.com"
section = "http://www.chicagoreader.com/chicago/best-of-chicago-2011-goods-and-services/BestOf?oid=4106022"

def get_category_links(section_url):
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, 'lxml')
    boccat = soup.find('dl', 'boccat')
    category_links = [BASE_URL + dd.a['href'] for dd in boccat.findAll('dd')]
    return category_links

def get_category_winner(category_url):
    html = urlopen(category_url).read()
    soup = BeautifulSoup(html, 'lxml')
    category = soup.find('h1', 'headline').string
    winner = [h2.string for h2 in soup.findAll('h2', 'boc1')]
    runners_up = [h2.string for h2 in soup.findAll('h2', 'boc2')]
    return {"category" : category,
            "category_url": category_url,
            "winner": winner,
            "runners_up": runners_up}
'''
Please refer to http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/
'''
if __name__ == '__main__':
    for category in get_category_links(section):
        pprint(get_category_winner(category))
        print "=============================="

