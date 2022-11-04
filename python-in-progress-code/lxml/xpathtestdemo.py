import lxml.etree as et

"""
爬虫基础xpath
"""

def parse_demo():
    content = ''
    with open('mp4br.txt','r',encoding='utf-8') as f:
        content = f.read()
    # print(content)
    tree = et.HTML(content)
    # result = tree.xpath('/html/body/section/div[1]/div/article[*]')  #获取article 元素
    # result = tree.xpath('/html/body/section/div[1]/div/article[*]/a/@href')
    result = tree.xpath('/html/body/section/div[1]/div/article[*]//h2/a')

    # print(result)
    for r in result:
        # print(r.text)  # 获取a标签的文本
        txt = r.xpath('./text()') # 获取a标签文本方式2，'.'表示当前节点
        print(txt[0])
        print(r.get('href'))  # 获取a标签的连接
    # _times = tree.xpath('//div/time')
    # print(_times)
    # for t in _times:
    #     print(t.text)
    imgs = tree.xpath('/html/body/section/div[1]/div/article[*]/a/img')
    # print(imgs)
    for img in imgs:
        print(img.get('data-src'))

if __name__ == '__main__':
    parse_demo()
