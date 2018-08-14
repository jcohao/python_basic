courses = ['Linus', 'Python', 'C++', 'Vim']
# 创建列表，列表时有序的

courses.append('PHP')
# 在列表尾部添加元素

courses.insert(1, 'Java')
# 在指定位置添加元素

courses.count('Java')
# 查找对应元素出现的次数

courses.remove('C++')
# 删除指定元素，若该值多次出现，则只有第一个指定元素被删除

del courses[-1]
# 删除列表中指定位置的元素

courses.reverse()
# 将列表元素的顺序反转

new_courses = ['BigData', 'Cloud']
courses.extend(new_courses)
# 将另一列表合并到原列表的末尾位置

courses.sort()
# 对列表进行排序，前提是列表元素必须是可比较的

courses.pop()
courses.pop(1)
# 默认返回列表最后一个元素，并把它删除，加上参数i则为弹出索引为i的元素

courses * 2
# 返回一个元素重复出现的列表

courses + other_list
# 将两个列表连接成一个



# 使用列表解析求矩阵的逆矩阵
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

[[row[i] for row in matrix] for i in range(4)]
# 如果这里用括号括起则会生成生成器

# 在序列中遍历，索引位置和对应值可以使用enumerate()函数同时获得
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


# 同时遍历两个或更多的序列，可以使用zip()组合
questions = ['name', 'quest', 'favorite color'] 
answers = ['jcohao', 'tmf', 'yellow']
for q, a in zip(questions, answers):
    print('What is your {}? It is {}'.format(q, a))

  
# 列表解析也可以用双层嵌套，前者为外层循环，后者为内层循环
[m + n for m in 'ABC' for n in 'abc']