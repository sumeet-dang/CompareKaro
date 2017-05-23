import urllib.request
from bs4 import BeautifulSoup


link = "https://www.snapdeal.com/search?keyword=sita%20amish&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy"


def snapdeal_crawl(link):
    with urllib.request.urlopen(link) as url:
        s = url.read()

    soup = BeautifulSoup(s)

    # fo = open('Crawlers/extracts/snapdeal.txt','r')
    # soup = BeautifulSoup(fo.read())
    # fo.close()

    master_list = []

    list_image = soup.find_all("source",class_="product-image")
    list_url = soup.find_all("div",class_="product-desc-rating")
    list_name = soup.find_all("p", class_="product-title")
    list_price = soup.find_all(['p', 'span'], attrs={'class':'product-price'})

    for name, image, price, url in zip(list_name, list_image, list_price, list_url):
        info = {}
        info['Name'] = str.strip(name['title'])
        info['Image'] = str.strip(image['srcset'])
        info['Price'] = str.strip(price.text.replace("Pre Order at"," ").replace("Rs. ",""))
        info['Url'] = str.strip(url.a['href'])
        master_list.append(info)

    # for content in master_list:
    #     print("1.Name : ", content['Name'])
    #     print("2.Image Url : ", content['Image'])
    #     print("3.Price : ", content['Price'])
    #     print("4.Url : ", content['Url'])

    return master_list
