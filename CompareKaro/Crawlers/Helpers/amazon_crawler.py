import urllib.request
from bs4 import BeautifulSoup

# link ="http://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=sita+amish"

def amazon_crawl(link):
    print(link)
    with urllib.request.urlopen(link) as url:
        s = url.read()

    # fo = open('Crawlers/extracts/foo.txt','r')
    # soup = BeautifulSoup(fo.read())
    # fo.close()

    soup = BeautifulSoup(s)

    master_list = []

    list_name = soup.find(id="s-results-list-atf").find_all(class_="a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal")
    list_image = soup.find(id="s-results-list-atf").find_all(class_="s-access-image cfMarker")
    list_price = soup.find(id="s-results-list-atf").find_all(class_="a-size-base a-color-price s-price a-text-bold")
    list_url = soup.find(id="s-results-list-atf").find_all(class_="a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal")

    for name, image, price, url in zip(list_name, list_image, list_price, list_url):
        info = {}
        info['Name'] = str.strip(name.h2['data-attribute'])
        info['Image'] = str.strip(image['src'])
        info['Price'] = str.strip(price.text)
        info['Url'] = str.strip(url['href'])
        master_list.append(info)

    return master_list
    # for content in master_list:
    #     print("1.Name : ", content['Name'])
    #     print("2.Image Url : ", content['Image'])
    #     print("3.Price : ", content['Price'])
    #     print("4.Url : ", content['Url'])
