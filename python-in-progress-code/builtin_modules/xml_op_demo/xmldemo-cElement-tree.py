import xml.etree.cElementTree as et


"""
Python 有三种方法解析 XML，SAX，DOM，以及 ElementTree:

1.SAX (simple API for XML )
Python 标准库包含 SAX 解析器，SAX 用事件驱动模型，通过在解析XML的过程中触发一个个的事件并调用用户定义的回调函数来处理XML文件。

2.DOM(Document Object Model)
将 XML 数据在内存中解析成一个树，通过对树的操作来操作XML。

3.ElementTree(元素树)
ElementTree就像一个轻量级的DOM，具有方便友好的API。代码可用性好，速度快，消耗内存少。
cElementTree效率更高，推荐使用cElementTree
注：因DOM需要将XML数据映射到内存中的树，一是比较慢，二是比较耗内存，而SAX流式读取XML文件，比较快，占用内存少，但需要用户实现回调函数（handler）。
"""


def xml_find_node_demo():
    # 打开文件, 读出xml文件对象
    tree = et.parse('db.xml')
    print(tree)  # 是一个对象 <xml.etree.ElementTree.ElementTree object at 0x00000182E1813B38>
    # 获取跟节点
    root = tree.getroot()  # 获取根节点
    print(root)  # 是一个对象  <Element 'data' at 0x000001D4ED0C47C8>
    # 查找三种方式
    # 1. 全文搜索: root.iter('year'),会查找所有符合条件的节点
    # years = root.iter('year')
    # for y in years:
    #     print(y.tag)  # 获取year节点对象的标签名
    #     print(y.attrib)  # 获取year节点对象的属性. 以key:value对的形式输出. key代指属性名, value代指属性值
    #     print(y.text)  # 获取year节点对象中的文本内容.

    # 2.1 在root的子节点找，只找一个就返回: root.find('country')
    country = root.find('country')
    # print(country.tag)
    # print(country.attrib)
    # print(country.text)
    # for child in country:  # 可以输出该节点下面的所有自节点
    #     print(child.tag)
    #     print(child.attrib)
    #     print(child.text)
    # 2.2 # 链式查找country下的year. 并获取其标签名, 属性, 文本内容，同于接着上面的继续,  country.find('year')
    # year = root.find('country').find('year')
    # print(year.tag)
    # print(year.attrib)
    # print(year.text)

    #  3. 在root的子节点找所有: root.findall("country")
    countries = root.findall('country')
    # chs = []
    for c in countries:
        for ch in c:
            # chs.append(ch)
            print(ch.tag, end=',')
            print(ch.attrib, end=',')
            print(ch.text, end=',')
        print()
    # print(chs)


def xml_change_value_and_write():  # 修改节点属性
    tree = et.parse('db.xml')
    root = tree.getroot()
    years = root.iter('year')
    for y in years:
        y.text = str(int(y.text) + 10)  # 将所有year节点的只增加5年
    tree.write('db2.xml')


def xml_add_value_and_write():  # 增加节点
    tree = et.parse('db.xml')
    root = tree.getroot()
    # 为country节点添加president属性
    countries = root.iter('country')  # 返回的是一个迭代器对象
    clist = list(countries)  # 把迭代器转换为列表
    # print(clist)
    p = et.Element('president')
    p.attrib = {'favorite_food': 'chicken'}
    p.text = 'NewTon lee'
    clist[0].append(p)
    p1 = et.Element('president')
    p1.attrib = {'favorite_food': 'roasted beef'}
    p1.text = 'Michael wong'
    clist[1].append(p1)
    p2 = et.Element('president')
    p2.attrib = {'favorite_food': 'lamb chop'}
    p2.text = 'Jessica Jade'
    clist[2].append(p2)
    tree.write('db3.xml')


def xml_delete_elem():
    tree = et.parse('db3.xml')
    root = tree.getroot()
    cs = root.iter('country')
    for c in cs:
        p = c.find("president")
        # print(p)
        if p is not None:
            c.remove(p)
    tree.write('db3.xml')


# 创建一个新xml文档
def create_new_xml():
    root = et.Element('students')
    stu = et.SubElement(root, 'student', attrib={'id': 'stu1'})
    name = et.SubElement(stu, 'name')
    name.text = "Steven lee"
    age = et.SubElement(stu, 'age')
    age.text = '18'
    gender = et.SubElement(stu, 'gender')
    gender.text = 'male'
    stu2 = et.SubElement(root, 'student', attrib={'id': 'stu2'})
    name = et.SubElement(stu2, 'name')
    name.text = "LiLi wong"
    age = et.SubElement(stu2, 'age')
    age.text = '23'
    gender = et.SubElement(stu2, 'gender')
    gender.text = 'female'
    etree = et.ElementTree(root)  # 生成元素数
    etree.write('Students.xml', encoding='utf-8', xml_declaration=True)  # 调用元素树的write方法保存文档


def create_new_xml2():  # 方式2，只有属性的节点
    root = et.Element('students')
    # 注意：需要一次添加所有属性，否则后面的属性会覆盖前面的属性
    stu = et.SubElement(root, 'student', attrib={'id': 'stu1', 'name': 'Ben lee', 'age': '30', 'gender': 'male'})
    stu.attrib['address'] = '3 pawsey road kgn5'  # 可以使用这种方式多次添加新属性
    stu2 = et.SubElement(root, 'student', attrib={'id': 'stu2', 'name': 'stacy lau', 'age': '28', 'gender': 'female'})

    etree = et.ElementTree(root)  # 生成元素树
    etree.write('Students2.xml', encoding='utf-8', xml_declaration=True,short_empty_elements=False)  # 调用元素树的write方法保存文档


if __name__ == '__main__':
    # xml_find_node_demo()
    # xml_change_value_and_write()
    # xml_add_value_and_write()
    # xml_delete_elem()
    # create_new_xml()
    create_new_xml2()
