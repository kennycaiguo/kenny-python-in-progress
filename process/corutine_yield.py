def A():
    a_list = ['1', '2', '3']
    for to_b in a_list:
        from_b = yield to_b  # yield关键字会返回一个生成器，即使没有return语句
        print('receive %s from B' % (from_b,))
        print('do some complex process for A during 200ms ')


def B(a):
    from_a = a.send(None)
    print('response %s from A ' % (from_a,))
    print('B is analysising data from A')
    b_list = ['x', 'y', 'z']
    try:
        for to_a in b_list:
            from_a = a.send(to_a)
            print('response %s from A ' % (from_a,))
            print('B is analysising data from A')
    except StopIteration:
        print('---from a done---')
    finally:
        a.close()


if __name__ == "__main__":
    a = A()
    print(type(a))  # <class 'generator'>
    B(a)
