'''
    迭代器是可以记住遍历的位置的对象
    迭代器对象从集合的第一个元素开始访问，直到所有元素被访问完结束
    迭代器只能往前迭代，不能往后，当遍历结束后不会回到开头
'''


# 字符串，列表或元组对象都可以用于创建迭代器

lists = [1, 2, 3, 4]
it = iter(lists)
print(next(it))

# 第一次使用next为指向lists的第一个元素
# 迭代器也可以用于for循环中遍历

'''
    在Python中，使用了yield的函数被称为生成器，生成器是一个返回迭代器的函数
    调用生成器的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，
    返回yield的值，并在下一次执行next()时从当前位置继续执行
'''

import sys

def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return 
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)
# f是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f), end=' ')
    except StopIteration:
        sys.exit()