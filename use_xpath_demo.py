from lxml import html

def parse():
    '''将html中的内容使用xpath进行提取'''
    #读取文件中内容
    f = open('./static/index.html','r',encoding='utf-8')
    s =f.read()

    selector = html.fromstring(s)

    #解析H3标题
    h3 =selector.xpath('/html/body/h3/text()')
    print(h3[0])

    # 解析ul
    # ul = selector.xpath('/html/body/ul/li')
    ul = selector.xpath('//ul/li')
    print(len(ul))
    for li in  ul:
        print(li.xpath('text()')[0])

    # 解析ul下指定的元素
    ul2 = selector.xpath('/html/body/ul/li[@class="important"]/text()')[0]
    print(ul2)

    #a
    a =selector.xpath('//div[@id="container"]/a/text()')[0]
    alink =selector.xpath('//div[@id="container"]/a/@href')[0]
    print(a)
    print(alink)
    f.close()

if __name__ =='__main__':
    parse()