# 身份运算符is is not
a = '123'
b = '123'
print(a is b)  # True,因为他们的id是一致的 is 比较的是id

print(id(a))
print(id(b))

print(a is not b)  # False
print("======================")

# 成员运算符in not in,用来判断一个值是否在每个集合中
arr1 = [1,2,3]
arr2 = [3,4,5]
for x in arr2:
    if x not in arr1:
        print("%d is not in arr1"%x)
    else:
        print("%d is in arr1"%x)
