# 字典是无序的键值对集合，元素为key:value组合，key在字典中是唯一
coursesdict = {1:'Linux', 2:'Vim'}

# 如果key不存在则访问dict[key]会抛出KeyError，可以用get()函数来获取key对应的value
# 如果key不存在则默认返回None，也可以在get()函数中给定一个默认值，若key不存在返回默认值
coursesdict.get(3, 'default')

# 可用dict()函数来创建字典，参数为包含多个二元元组的元组
# dict_form_tuple = dict(((1, 'Linux'), (2, 'Vim')))

coursesdict[3] = 'bash'
# 当key不存在时则为在字典中添加元素，若key存在则为修改原key的value

del coursesdict[1]
# 从字典中删除元素，若key不存在则抛出KeyError

# 在字典中使用方法items()来获取字典的所有元素
for key, value in coursesdict.items():
	print(key, value)

# 也可以使用keys()和values()分别只获得字典中的所有key或value的列表
coursesdict.keys()
coursesdict.values()

coursesdict.pop(3)
# 返回key对应的value，并弹出该key:value键值对





