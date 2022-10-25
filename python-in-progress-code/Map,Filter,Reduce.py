import math

# map的用法
def mapProc(items, outputs):
    outputs.append(list(map(lambda x: x ** 2, items)))
    return outputs


def sqrt(num):
    return math.sqrt(num)


def power(n):
    return n ** 2


def double_up(n):
    return n * 2


funcs = [double_up, power, sqrt]

if __name__ == '__main__':
    # items = [1, 2, 3, 4, 5]
    # outputs = []
    # print(mapProc(items, outputs))

    nums =[1,2,3,4,5]
    for n in nums:
        value = map(lambda x:x(n),funcs)
        print(list(value))

