class Duck(object):
    def swim(self):
        print("duck swim...")

    def walk(self):
        print("duck walk...")

    def sound(self):
        print("ka ka ka ...")


class Goose(object):
    def swim(self):
        print("goose swim...")

    def walk(self):
        print("goose walk...")

    def sound(self):
        print("go go go  ...")


class Dog(object):
    def swim(self):
        print("gdog swim...")

    def walk(self):
        print("dog walk...")

    def sound(self):
        print("wang wang wang   ...")


def test_animal(animals):  # 鸭子模型的应用，这几个类并没有继承关系，但是他们的方法完全一样，可以传递给同一个函数
    for a in animals:
        a.swim()
        a.walk()
        a.sound()
        print("===================================")


if __name__ == '__main__':
    test_animal([Duck(), Goose(), Dog()])
