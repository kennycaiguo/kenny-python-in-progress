def printArgs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# python中args可以传递列表或者元组
# kwargs可以传递字典
# 如果你想在函数里同时使用所有这三种参数， 顺序是这样的：
#  some_func(fargs, *args, **kwargs)

def test_var_args(f_arg, *argv):  # python中的可变参数
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


# kwargs 允许你将不定长度的键值对, 作为参数传递给一个函数。 如果你想要在一个函数里处理带名字的参数, 你应该使用kwargs。
# 这里有个让你上手的例子:

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))


#

if __name__ == '__main__':
    # args = (3, "hello", {"name": "jack", "age": 18, "gender": "male"})
    # args = [3, "hello", {"name": "jack", "age": 18, "gender": "male"}]
    # printArgs(*args)
    #
    # kwargs = {"arg3": {"name": "May", "age": 18, "gender": "Female"}, "arg1": (100, 200, 300), "arg2": [10, 20, 30]}
    # # printArgs(**kwargs)

    # test_var_args('yasoob', 'python', 'eggs', 'test')
    jack_ = {"name": "jack","email":"Jack12345@qq.com","sujects":["chinese","english","french"]}
    greet_me(**jack_)

