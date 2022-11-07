import multiprocessing


def fill_dict(d, key, value):
    d[key] = value


def main1():
    mgr = multiprocessing.Manager()
    dic = mgr.dict()  # 共享资源
    procs = [multiprocessing.Process(target=fill_dict, args=(dic, i, i ** 2)) for i in range(10)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print(dic)
    for k, v in enumerate(dict(dic)):
        print("%s = %s" % (k, v))


def main2():
    mgr = multiprocessing.Manager()
    dic = mgr.dict()  # 共享资源,注意普通的字典是不能在进程间共享数据的，只有Manager创建的字典才可以在进程中共享数据
    print(type(dic))  # <class 'multiprocessing.managers.DictProxy'>
    names = ['Jack', 'Ben', 'May', 'Tommy', 'Jerry']
    score = [90, 80, 70, 50, 66]
    procs = [multiprocessing.Process(target=fill_dict, args=(dic, names[i], score[i])) for i in range(5)]
    # procs = [multiprocessing.Process(target=fill_dict, args=(dic, i, score[i])) for i in range(5)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print(dic)  # {'Jack': 90, 'Ben': 80, 'Tommy': 50, 'May': 70, 'Jerry': 66}

    # for k, v in enumerate(dict(dic)):
    #     print("%s = %s" % (k, v))

    # for k in dict(dic):  # multiprocessing.managers.DictProxy 没有实现iterkeys()
    #     print("%s = %s" % (k, dic[k]))  # ok
    # for k in dic.keys():
    #     print("%s = %s" % (k, dic[k]))  # ok

    for (k,v) in dic.items():
        print("%s = %s" % (k, v))  # 也是okey


if __name__ == '__main__':
    # main1()
    main2()
