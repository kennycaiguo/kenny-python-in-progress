from collections import Iterable, Iterator, ChainMap, Counter, deque, defaultdict, namedtuple, OrderedDict

'''
 python的其他容器包括ChainMap, Counter, deque, defaultdict, namedtuple, OrderedDict等等
 其中比较重要的是Counter, deque, OrderedDict, namedtuple
'''
gen = (n for n in range(1,5))
# print(list(gen))
# for g in gen:
#     print(g, end=',')
# print()

print(isinstance(gen,Iterable))  # True
print(isinstance({},Iterable))  # True
print(isinstance('abc',Iterable))  # True
print(isinstance(100, Iterable))  # False

for i in range(1,5):
    print(next(gen), end=',')
print()

import builtins

c = ChainMap()
c1 = Counter()

d = deque('ghi')

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list())

Point = namedtuple('Point', ['x', 'y'])

dt = OrderedDict.fromkeys('abcde')
