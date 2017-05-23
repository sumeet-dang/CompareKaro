from django.shortcuts import render
from Crawlers.Helpers.amazon_crawler import amazon_crawl
from django import template
from Crawlers.Helpers.snapdeal_crawler import snapdeal_crawl
from Crawlers.Helpers.ebay_crawler import ebay_crawl



# Create your views here.
def load_sources(request):
    if(request.method == "POST"):
        item = request.POST.get("item_name")
        amazon_link = "http://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=" + item.replace(" ","+")
        snapdeal_link = "https://www.snapdeal.com/search?keyword=" + item.replace(" ","%20") + "&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy"
        ebay_link = "http://www.ebay.in/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=" + item.replace(" ","+") + "&_sacat=0"
        context_dict = {}
        minimum_list = []
        amazon_list = amazon_crawl(amazon_link)
        snapdeal_list = snapdeal_crawl(snapdeal_link)
        ebay_list = ebay_crawl(ebay_link)        

        seq = min(amazon_list, key=lambda x:x['Price'])
        amazon_minimum = seq
        amazon_minimum['Source'] = 'Amazon'
        seq = min(snapdeal_list, key=lambda x:x['Price'])
        snapdeal_minimum = seq
        snapdeal_minimum['Source'] = 'Snapdeal'
        seq = min(ebay_list, key=lambda x:x['Price'])
        ebay_minimum = seq
        ebay_minimum['Source'] = 'Ebay'

        minimum_list.append(amazon_minimum)
        minimum_list.append(snapdeal_minimum)
        minimum_list.append(ebay_minimum)

        context_dict['amazon_list'] = amazon_list
        context_dict['snapdeal_list'] = snapdeal_list
        context_dict['ebay_list'] = ebay_list
        context_dict['minimum_list'] = minimum_list
        return render(request, "Crawlers/search_results.html", context_dict)
    else:
        return render(request,"Crawlers/search.html")
