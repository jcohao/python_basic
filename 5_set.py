'''
    集合是一个无序不重复元素的数据集，无序则不可以使用索引来进行顺序访问
    不重复则可用于去重和测试是否存在
    创建集合可以使用{}和set函数，但创建空集合只能用set()函数，因为{}创建的为空字典
'''

courses = {'Linux', 'Java', 'Linux'}
courses = set(['Linux', 'Java', 'Linux'])
# 使用set函数所传递的参数可以为列表，也可以为元组

nameset = set('shiyanlou.com')
# 直接由字符串和set函数创建集合，会将字符串拆散为不同的字符，并去除重复的字符

# 进行测试判断是否存在
('Linux' in courses) == 1
('C++' not in courses) == 1

courses.add('Python')
# 往集合中添加元素
# 方法update()也可以添加元素，且参数可以为列表、元组、字典等
courses.update(['C++', 'C#'])

courses.remove('Linux')
# 删除指定的元素，元素不存在则抛出异常
# 使用方法discard()也可以删除指定元素，且元素不存在不会发生错误
courses.discard('math')

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1 | set2
set1.union(set2)
# 求两个集合的并集

set1 & set2
# 求交集

set1 - set2
# 求两个集合的差

set1 ^ set2
# 求交集的补集




