import xml.sax
from xml import sax

"""
利用sax解析xml需要定义一个类继承sax.handler.ContentHandler
sax解析效率比较高但是不能重复解析
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Person:(name:{s.name},age:{s.age})".format(s=self)


class SaxHandler(xml.sax.handler.ContentHandler):  # pycharm 重写方法的快捷方式：alt+insert

    def __init__(self):
        self.name = ''
        self.age = 0
        self.current_tag = ''

    def startElement(self, tag_name, attrs):
        if 'name' == tag_name:
            self.current_tag = tag_name

        if 'age' == tag_name:
            self.current_tag = tag_name

    # 获取文本内容
    def characters(self, content):
        if 'name' == self.current_tag:
            # print(content)
            self.name = content
        if 'age' == self.current_tag:
            # print(content)
            self.age = content

    def endElement(self, tag_name):
        if 'name' == tag_name:
            print(tag_name + ":" + self.name)

        if 'age' == tag_name:
            print(tag_name + ":" + self.age)


class SaxHandler2(xml.sax.handler.ContentHandler):  # pycharm 重写方法的快捷方式：alt+insert

    def __init__(self):
         self.persons=[]

    def startElement(self, tag_name, attrs):
        if 'person' == tag_name:
            # print(attrs['name'], attrs['age'])
            self.persons.append(Person(attrs['name'],attrs['age']))


def sax_demo1():  # 方式一
    # 1.实例化sax解析
    parser = sax.make_parser();
    # 2.封闭命名空间
    parser.setFeature(sax.handler.feature_namespaces, 0)  # 关闭命名空间
    # 3.1.实例化内容处理对象
    sax_handler = SaxHandler()
    # 3.2将处理对象设置到sax解析器
    parser.setContentHandler(sax_handler)
    # 4.解析文档
    parser.parse('people.xml')


def sax_demo2():  # 方式2
    # 1.实例化sax解析
    parser = sax.make_parser();
    # 2.封闭命名空间
    parser.setFeature(sax.handler.feature_namespaces, 0)  # 关闭命名空间
    # 3.1.实例化内容处理对象
    sax_handler = SaxHandler2()
    # 3.2将处理对象设置到sax解析器
    parser.setContentHandler(sax_handler)
    # 4.解析文档
    parser.parse('people2.xml')

    for p in sax_handler.persons:
        print(p)

if __name__ == '__main__':
    # sax_demo1()
    sax_demo2()
