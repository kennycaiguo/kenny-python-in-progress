import pickle
import json

"""
pickle操作：
序列化：新创建一个文件，以'wb'方式打开，然后使用pickle.dump(obj,file)
反序列化：1.打开需要反序列号的文件，后缀为.pickle,返回一个句柄如file
        2.调用obj = pickle.load(file) 将文件反序列化到一个对象
"""


def pick_serialize_test():
    # 定义字典
    my_dict = {"name": "ren", "age": 28}
    # 序列号到文件
    with open('dict_pickle.pickle', 'wb') as f:
        pickle.dump(my_dict, f)
    # 反序列化
    with open('dict_pickle.pickle', 'rb') as f:
        dict_unpickle = pickle.load(f)
    print(dict_unpickle)  # {'name': 'ren', 'age': 28} 反序列号成功


def pick_serialize_test2():
    """可以同时将许多不同类型数据保存在同一份.pickle文件中, 再按照相同的顺序读出"""
    a1 = "apple"
    b1 = {1: 'One', 2: 'Two'}
    c1 = ['test', 'name', 1, 2, 3]
    f1 = open("temp.pkl", "wb")
    # 可以保存到同一个文件中
    pickle.dump(a1, f1)
    pickle.dump(b1, f1)
    pickle.dump(c1, f1)
    f1.close()

    # 再按照相同的顺序读出
    f2 = open("temp.pkl", "rb")
    a2 = pickle.load(f2)
    b2 = pickle.load(f2)
    c2 = pickle.load(f2)
    print(a2)  # apple
    print(b2)  # {1: 'One', 2: 'Two'}
    print(c2)  # ['test', 'name', 1, 2, 3]
    f2.close()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


def pickle_dum_class(p):
    with open('cls_pk.pickle', 'wb') as f:
        pickle.dump(p, f)


def pickle_load_cls(file):
    """pickle不仅可以保存python中的基本类型，也可以保存自己定义的class，但是在反序列化的时候，这个class的定义必须存在"""
    with open('cls_pk.pickle', 'rb') as f:
        p = pickle.load(f)
        p.show()


def test_cls_pickle():
    p = Person("Ben", 33)
    pickle_dum_class(p)
    pickle_load_cls('cls_pk.pickle')


if __name__ == '__main__':
    # pick_serialize_test()
    # pick_serialize_test2()
    test_cls_pickle()
