import requests
from  lxml import html


def spider(sn):
    url = 'http://search.dangdang.com/?key={sn}&act=input'.format(sn=sn)
    #获取文本内容
    html_data= requests.get(url).text

    selector =html.fromstring(html_data)

    ul_list =selector.xpath('//div[@id="search_nature_rg"]/ul/li')
    print(len(ul_list))
    for li in ul_list:
        title = li.xpath('a/@title')[0]
        print(title)
        link = li.xpath('a/@href')[0]
        print(link)
        print('---------------------')
        price =li.xpath('p[@class="price"]/span[@class="search_now_price"]/text()')
        print(price[0].replace('¥',''))
        print('---------------------')

        # 商家
        store = li.xpath('p[@class="search_shangjia"]/a/text()')
        store = '当当自营' if len(store) == 0 else store[0]
        print(store)
        print('-----------------------')

if __name__ =='__main__':
    sn='9787115428028'
    spider(sn)