courses = ('C++', 'Python', 'PHP', 'Vim')
# 创建元组，元组为特殊的列表，元组一旦创建无法修改
# append()等方法对于元组将无法适用

new_courses = ('Linux', ['BigData1', 'BigData2'], 'Vim')
# 若元组中包含可变的数据元素，如一个列表，则该元素的内容是可以修改的

# 如果要创建只有一个元素的元组，需要在元素后面加一个逗号，否则所创建的为一个普通的变量
course = ('Linux',)
