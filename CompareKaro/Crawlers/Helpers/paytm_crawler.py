import urllib.request
from bs4 import BeautifulSoup

# link = "https://paytm.com/shop/search?q=sita%20amish&from=organic&child_site_id=1&site_id=1"

def ebay_crawl(link):
    with urllib.request.urlopen(link) as url:
        s = url.read()

    soup = BeautifulSoup(s)

    # fo = open('../extracts/paytm.txt','r')
    # soup = BeautifulSoup(fo.read())
    # fo.close()

    master_list = []

    list_image = soup.find_all("div",class_="_3nWP")
    # list_url = soup.find_all("a",class_="img imgWr2")
    # list_name = soup.find_all("a",class_="img imgWr2")
    # list_price = soup.find_all("li", class_="lvprice prc")

    for child in list_image:
        print(child)

    # for name, image, price, url in zip(list_name, list_image, list_price, list_url):
    #     info = {}
    #     info['Name'] = str.strip(name.img['alt'])
    #     info['Image'] = str.strip(image.img['src'])
    #     info['Price'] = str.strip(price.span.text.replace("Rs.",""))
    #     info['Url'] = str.strip(url['href'])
    #     master_list.append(info)

    # for content in master_list:
    #     print("1.Name : ", content['Name'])
    #     print("2.Image Url : ", content['Image'])
    #     print("3.Price : ", content['Price'])
    #     print("4.Url : ", content['Url'])

    return master_list
ebay_crawl(link)
