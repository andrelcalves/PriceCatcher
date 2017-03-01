from lxml import html
import requests

# will be replaced for a function that will stored the data into mongodb database
def list_item(products, prices):
    item = 0
    for product in products:
        print product, 'R$ ', prices[item]
        item = item+1

baseurl = 'http://www.deliveryextra.com.br/secoes/C312/alimentos'
page = requests.get(baseurl)
tree = html.fromstring(page.content)

#This will create a list of products
products = tree.xpath('//div[@class="showcase-item__info"]/h3/a/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="value"]/text()')

list_item(products,prices)

#navagete into the catalog
nextpage = tree.xpath('//li[@class="pageSelect nextPage item inline--middle"]/a/@href')
lastpage = tree.xpath('//li[@class="pageSelect lastpage item inline--middle"]/a/@href')

nexturl = baseurl + nextpage[0]
print 'lastpage ', lastpage
print 'nexturl', nexturl

pagecount = lastpage[0][4:6]

i=1
while (i<=pagecount):
    nexturl = baseurl + nextpage[0]
    page = requests.get(nexturl)
    tree = html.fromstring(page.content)

    #This will create a list of products
    products = tree.xpath('//div[@class="showcase-item__info"]/h3/a/text()')

    #This will create a list of prices
    prices = tree.xpath('//span[@class="value"]/text()')

    #Getting next page
    nextpage = tree.xpath('//li[@class="pageSelect nextPage item inline--middle"]/a/@href')
    print 'nexturl', nexturl
    
    list_item(products,prices)
    i=i+1
