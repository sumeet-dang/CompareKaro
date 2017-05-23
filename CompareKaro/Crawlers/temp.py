import urllib.request
from bs4 import BeautifulSoup

link ="http://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=sita+amish"

def amazon_crawl(link):
    with urllib.request.urlopen(link) as url:
        s = url.read()

    soup = BeautifulSoup(s)

    fo = open("foo.txt", "w+")
    fo.write(soup.prettify())
    fo.close()

amazon_crawl(link)
