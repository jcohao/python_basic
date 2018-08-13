#/usr/bin/env python3
'''
	告诉shell使用Python3解释器来解释代码，如果有这行代码并且给脚本通过
	chmod a+x xx.py增加执行权限，则可直接使用./xx.py来执行py文件
	否则只能使用python3 xx.py
'''

'''
	strip()默认情况下会删除字符串首尾的空格及换行符
	当使用参数时会删除字符串中的对应的首位字符
'''
str = "hello world"
# str.strip('hl')返回"ello world"，原字符串不变

'''
	split()默认情况下会把空白符当成分隔符，把原字符串进行切分，返回一个列表
	传入参数的时候会用传入的参数对字符串进行切分
'''

'''
	当出现了异常应该用try, except, finally来处理，可以把可能出现异常的代码放在try里
	然后在except中添加处理异常的方法，finally是用来进行清理工作的，无论程序正不正常
	里面的代码都会执行
'''

filename = '/etc/protocols'
f = open(filename)
try:
	f.write('shiyanlou')
except:
	print("File write error")
finally:
	f.close()
	
# 这里尝试写入一个以只读方式打开的文件，所以抛出异常

# 在程序执行过程中可以用raise来抛出异常

raise ValueError()

'''
	对于文件夹，Python中可以识别成一个包，前提是这个文件夹中有一个__init__.py文件
	该文件可以为空
	例如我们创建一个目录 shiyanlou，在这个目录下有 __init__.py 
	和 louplus.py 两个代码文件，我们想要引入 louplus.py 文件就
	可以用 import shiyanlou.louplus 这种代码来引入，
	前提是 shiyanlou 目录已经放到了 Python 模块搜索的默认路径下了
'''

'''
	命令行参数的使用方法为使用sys模块的sys.argv
	sys.argv[0]为脚本名称，sys.argv[1]为第一个参数，以此类推
'''

'''
	Python 文件都有一个 __name__ 属性，默认的属性值就是文件名（不带 .py 的字符串形式）
	例如 argtest.py 的 __name__ 属性值就是 'argtest' 
	在终端用 python 解释器执行此文件时
	($ python3 argtest.py hello shiyanlou 这样)，
	__name__ 属性的值就变成 '__main__'
'''

import sys

if __name__ == '__main__':
	for arg in sys.argv:
		print(arg)

'''
	if __name__ == '__main__': 实际的作用是让这个程序在终端像 
	$ python3 argtest.py 这样执行时可以执行到 if __name__ == '__main__': 
	这个代码块中的内容。当通过 import argtest 将该文件作为模块导入到其他代码文件时
	不会执行 if __name__ == '__main__':中的内容，因为导入后这个文件的 __name__ 属性
	值仍然是文件名 'argtest' 。
'''

'''
	在字符串中，使用r可以让反斜杠不起作用，如r'This is a line with\n' 则\n会显示，
	而不是换行
'''

# 字符串可以用 + 号连接，可以用 * 号重复

'''
	可变数据类型就是内容改变了，但是变量的地址没有变，如list，dict
	不可变数据类型，内容改变，则开辟新的内存空间来存储新变量，变量的地址改变
	如number，string，tuple，sets
	字符串元素不能改变，str = 'hao' str[0] = 'r'是不允许的  
'''

'''
	2 / 4 除法运算，得到的是一个浮点数 0.5
	2 // 4 整除运算，得到的是一个截去小数部分的整数 0
'''

'''
	循环语句可以有else块，在穷尽列表（for循环）或条件变为false（while循环）导致
	循环终止时被执行，但循环被break终止时不执行
'''

'''
	type()函数不会认为子类是父类的一种类型
	而isinstance()函数则会
'''

# print()函数的字符串格式化，print('my name is %s' % 'jcohao')