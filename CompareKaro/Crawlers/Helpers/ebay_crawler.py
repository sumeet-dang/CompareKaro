import urllib.request
from bs4 import BeautifulSoup

# link = "http://www.ebay.in/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=sita+amish&_sacat=0"

def ebay_crawl(link):
    with urllib.request.urlopen(link) as url:
        s = url.read()

    soup = BeautifulSoup(s)

    # fo = open('Crawlers/extracts/ebay.txt','r')
    # soup = BeautifulSoup(fo.read())
    # fo.close()

    master_list = []

    list_image = soup.find_all("a",class_="img imgWr2")
    list_url = soup.find_all("a",class_="img imgWr2")
    list_name = soup.find_all("a",class_="img imgWr2")
    list_price = soup.find_all("li", class_="lvprice prc")

    for name, image, price, url in zip(list_name, list_image, list_price, list_url):
        info = {}
        info['Name'] = str.strip(name.img['alt'])
        info['Image'] = str.strip(image.img['src'])
        info['Price'] = str.strip(price.span.text.replace("Rs.",""))
        info['Url'] = str.strip(url['href'])
        master_list.append(info)

    return master_list

    # for content in master_list:
    #     print("1.Name : ", content['Name'])
    #     print("2.Image Url : ", content['Image'])
    #     print("3.Price : ", content['Price'])
    #     print("4.Url : ", content['Url'])
