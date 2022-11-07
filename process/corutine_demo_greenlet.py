from greenlet import greenlet  # 这是一个第三方库，需要安装


def test1():
    print(12)
    gr2.switch()
    print(34)


def test2():
    print(56)
    gr1.switch()  # 类似以yield的效果
    print(78)
    gr1.switch()


if __name__ == '__main__':
    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    gr2.switch()
