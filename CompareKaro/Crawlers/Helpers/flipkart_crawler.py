import urllib.request
from bs4 import BeautifulSoup


link ="https://www.flipkart.com/search?q=iphone%206s&otracker=start&as-show=on&as=off"

def flipkart_crawl(link):
    with urllib.request.urlopen(link) as url:
        s = url.read()

    soup = BeautifulSoup(s)
    # master_list = []

    fo = open('flipkart.txt','w+')
    fo.write(soup.prettify())
    fo.close()

    # list_name = soup.find(class_="_2SxMvQ")
    # print(list_name)
    # list_image = soup.find(id="s-results-list-atf").find_all(class_="s-access-image cfMarker")
    # list_price = soup.find(id="s-results-list-atf").find_all(class_="a-size-base a-color-price s-price a-text-bold")
    # list_url = soup.find(id="s-results-list-atf").find_all(class_="a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal")

    # for name in list_name:
    #     print(name)


flipkart_crawl(link)
