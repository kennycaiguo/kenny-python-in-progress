import xml.dom.minidom  # 如果不导入，无法使用

"""
dom解析比sax解析要慢，但是可以重复解析
"""


def dom_create_demo1():  # dom可以创建xml，方式一
    doc = xml.dom.minidom.Document()
    root = doc.createElement('Person')
    doc.appendChild(root)
    # 文本数据：
    data = [{'name': "刘德华", 'age': '60', 'gender': 'male'}, {'name': "韩梅梅", 'age': '30', 'gender': 'female'}]
    for i in data:
        node = doc.createElement('person')
        node.setAttribute('name', i['name'])
        node.setAttribute('age', i['age'])
        node.setAttribute('gender', i['gender'])

        root.appendChild(node)

    print(root)
    # 写xml
    with open('persons2.xml', 'w', encoding='utf-8') as f:
        doc.writexml(f, indent='\n', addindent='\t', encoding='utf-8')


def dom_create_demo2():  # dom可以创建xml,方式二
    doc = xml.dom.minidom.Document()
    root = doc.createElement('People')
    doc.appendChild(root)

    # 文本数据：
    data = [{'name': "刘德华", 'age': '60', 'gender': 'male'}, {'name': "韩梅梅", 'age': '30', 'gender': 'female'}]
    for i in data:
        person = doc.createElement('person')
        # 创建person的子节点
        name = doc.createElement('name')
        age = doc.createElement('age')
        gender = doc.createElement('gender')
        # 创建文本节点
        t_name = doc.createTextNode(i["name"])
        t_age = doc.createTextNode(i['age'])
        t_gender = doc.createTextNode(i['gender'])
        # 将文本节点添加到对应的节点中
        name.appendChild(t_name)
        person.appendChild(name)

        age.appendChild(t_age)
        person.appendChild(age)

        gender.appendChild(t_gender)
        person.appendChild(gender)
        root.appendChild(person)

    print(root)
    # 写xml
    with open('person3.xml', 'w', encoding='utf-8') as f:
        doc.writexml(f, indent='\n', addindent='\t', encoding='utf-8')


def dom_parse_demo():
    # 1.解析文档获取文档树
    dom_tree = xml.dom.minidom.parse('movie_data.xml')
    # print(dom_tree)
    root = dom_tree.documentElement
    # print(root)
    movie_list = root.getElementsByTagName('movie')
    for m in movie_list:
        movie_title = m.getElementsByTagName('title')[0]
        # 获取文本节点
        # print(movie_title.childNodes[0].nodeValue)  # 获取节点文本方法1
        print("title:", movie_title.childNodes[0].data)  # 获取节点文本方法2
        # 获取属性getAttribute()方法
        print("director:", movie_title.getAttribute("director"))
        # 获取演员列表，注意默认是会把缩进也当作一个文本节点，我们需要过滤没有用的节点
        actors_list = m.getElementsByTagName('actors')
        for actors in actors_list:
            # 只处理元素节点
            for ch in actors.childNodes:
                if isinstance(ch, xml.dom.minidom.Element):
                    print("actor:", ch.childNodes[0].data)
            print("====================================")

        desc = m.getElementsByTagName('desc')
        # 注意如果某一个属性不是每一个节点都有，需要先判断一下，否则报索引越界错误
        if desc:
            print(desc[0].childNodes[0].data.strip())


if __name__ == '__main__':
    # dom_create_demo1()
    # dom_create_demo2()
    dom_parse_demo()
