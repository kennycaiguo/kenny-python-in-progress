import pickle
import json
from pathlib import Path

"""
Python Json序列化与反序列化
　　在python中，序列化可以理解为：把python的对象编码转换为json格式的字符串，反序列化可以理解为：把json格式字符串解码为python数据对象。
  在python的标准库中，专门提供了json库与pickle库来处理这部分。
　　json的dumps方法和loads方法，可实现数据的序列化和反序列化。具体来说，dumps方法，可将json格式数据序列为Python的相关的数据类型；
    loads方法则是相反，把python数据类型转换为json相应的数据类型格式要求。在序列化时，中文汉字总是被转换为unicode码，
    在dumps函数中添加参数ensure_ascii=False即可解决。

"""


def json_serialize_demo_no_ensure():  # 未在dumps函数中添加参数ensure_ascii=False
    dict1 = {'name': 'zhangsan', 'age': 33, 'address': '红星路'}
    print('未序列化前的数据类型为:', type(dict1))
    print('为序列化前的数据：', dict1)
    # 对dict进行序列化的处理
    js_dict = json.dumps(dict1)
    print(js_dict)


def json_serialize_demo_ensure():  # 在dumps函数中添加参数ensure_ascii=False
    dict1 = {'name': 'zhangsan', 'age': 33, 'address': '红星路'}
    print('未序列化前的数据类型为:', type(dict1))
    print('为序列化前的数据：', dict1)
    # 对dict进行序列化的处理
    js_dict = json.dumps(dict1, ensure_ascii=False)
    print(js_dict)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student[name:{s.name},age:{s.age},score:{s.score}]'.format(s=self)


# json默认不能够将一个类对象序列化，如果需要序列化，必须将对象转为字典
def json_serialize_cls():
    s = Student("xiaoli", 18, 100)
    data_j = json.dumps(s, default=lambda obj: obj.__dict__)  # 这里不加default属性就会报错
    print(data_j)
    stu = json.loads(data_j)  # 反序列化后返回的是一个字典
    print(Student(**stu))  # 需要将字典转换为类对象


def json_dump_data_to_file(file):  # 很奇怪：在一个函数里面先使用json.dump(),然后再使用json.load()加载同一个文件会抛异常，分开到两个方法中操作没有问题
    data = dict(name='ken', age=33, married=True)
    f = open(file, 'w', encoding='utf-8')
    json.dump(data, f, ensure_ascii=False)


def json_load_from_file(file):
    with open(file, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        print(json_data)


def json_dump_cls_to_file(obj, fileanme):
    file = open(fileanme, 'w')
    json.dump(obj, file, default=lambda obj: obj.__dict__)  # 这里不加default属性就会报错


def json_load_cls_from_file(filename):
    path = Path(filename)
    if not path.exists():  # 判断文件是否存在，使用pathlib的Path类来构建对象，然后使用对象的exists()来判断
        print("文件不存在，请先运行 json_dump_cls_to_file(obj, fileanme)")
        return
    else:
        file = open(path, 'r')
        obj = json.load(file)
        print(Student(**obj))


if __name__ == '__main__':
    # json_serialize_demo_no_ensure()
    # json_serialize_demo_ensure()
    # json_serialize_cls()
    # json_dump_data_to_file()
    # json_load_from_file('jdata.json')
    # json_dump_data_to_file('test.json')
    # json_load_from_file('test.json')
    # s = Student("willy", 18, 100)
    # json_dump_cls_to_file(s, 'stu.json')
    json_load_cls_from_file('stu.json')
# """
# pickle操作：
# 序列化：新创建一个文件，以'wb'方式打开，然后使用pickle.dump(obj,file)
# 反序列化：1.打开需要反序列号的文件，后缀为.pickle,返回一个句柄如file
#         2.调用obj = pickle.load(file) 将文件反序列化到一个对象
# """
#
#
# def pick_serialize_test():
#     # 定义字典
#     my_dict = {"name": "ren", "age": 28}
#     # 序列号到文件
#     with open('dict_pickle.pickle', 'wb') as f:
#         pickle.dump(my_dict, f)
#     # 反序列化
#     with open('dict_pickle.pickle', 'rb') as f:
#         dict_unpickle = pickle.load(f)
#     print(dict_unpickle)  # {'name': 'ren', 'age': 28} 反序列号成功
#
#
# def pick_serialize_test2():
#     """可以同时将许多不同类型数据保存在同一份.pickle文件中, 再按照相同的顺序读出"""
#     a1 = "apple"
#     b1 = {1: 'One', 2: 'Two'}
#     c1 = ['test', 'name', 1, 2, 3]
#     f1 = open("temp.pkl", "wb")
#     # 可以保存到同一个文件中
#     pickle.dump(a1, f1)
#     pickle.dump(b1, f1)
#     pickle.dump(c1, f1)
#     f1.close()
#
#     # 再按照相同的顺序读出
#     f2 = open("temp.pkl", "rb")
#     a2 = pickle.load(f2)
#     b2 = pickle.load(f2)
#     c2 = pickle.load(f2)
#     print(a2)  # apple
#     print(b2)  # {1: 'One', 2: 'Two'}
#     print(c2)  # ['test', 'name', 1, 2, 3]
#     f2.close()
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(self.name, self.age)
#
#
# def pickle_dum_class(p):
#     with open('cls_pk.pickle', 'wb') as f:
#         pickle.dump(p, f)
#
#
# def pickle_load_cls(file):
#     with open('cls_pk.pickle', 'rb') as f:
#         p = pickle.load(f)
#         p.show()
#
#
# def test_cls_pickle():
#     p = Person("Ben", 33)
#     pickle_dum_class(p)
#     pickle_load_cls('cls_pk.pickle')
#
#
# if __name__ == '__main__':
#
#     # pick_serialize_test()
#     # pick_serialize_test2()
#     # test_cls_pickle()
