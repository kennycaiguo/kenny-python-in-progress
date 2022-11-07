from threading import Timer


def test():
    print("testing....end")


if __name__ == '__main__':
    t = Timer(2, test)  # 2秒后执行test
    t.start()
