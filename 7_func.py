'''
	变量作用域
	Python中有四种变量作用域：
		L (Local) 局部作用域
		E (Enclosing) 闭包函数外的函数中
		G (Global) 全局作用域
		B (Bulit-in) 内建作用域
	以 L -> E -> G -> B 的规则查找变量
'''

x = int(2.9) 		# 内建作用域

g_count = 0 		# 全局作用域
def outer():
	o_count = 1 	# 闭包函数外的函数中
	def inner():
		i_count = 2	# 局部作用域

'''
	Python中只有模块(module)，类(class)以及函数(def, lambda)才会引入新的作用域，
	其他的代码块(if, while, try, for)不会引入新的作用域，这些语句内定义的变量，外部也能访问
'''

'''
	当内部作用域想要修改外部作用域的变量时，需要用到global和nonlocal关键字
'''

# 修改全局变量num：
num = 1
def fun1():
	global num
	print(num)
	num = 123
	print(num)

fun1()
print(num)
# 最后输出为123

# 若想要修改闭包函数中的变量则要用nonlocal关键字：
def outer():
	num = 10
	def inner():
		nonlocal num # 这里不能声明为global，否则最后的print先找到的是nun=10 L->E->G->B
		num = 100
		print(num)
	inner()
	print(num)
outer()

# Python常用的参数有四种： 必选参数， 默认参数， 可变参数，（命名关键字参数）， 关键字参数
# 以上四种参数可以复合使用， 复合使用时各类参数的定义顺序必须同上

# 必选参数， 按照定义顺序传参
def connect(ipaddress, port):
	print("IP: ", ipaddress)
	print("Port: ", port)
	
# 设置默认参数， 当默认参数没有赋值时， 则会自动赋为默认值
# 默认参数的默认值必须为不可变的数据类型（如字符串、元组、数字、布尔值、None）
def connect(ipaddress, port=22):
	print("IP: ", ipaddress)
	print("Port: ", port)

# 若默认值为列表，调用函数后，默认值会改变
def f(a, data=[])
	data.append(a)
	print(data)
# 当函数定义时，data变量则指向了[]对象，当调用该函数，使用默认参数则改变了data的值
# 在下次调用函数时，再使用默认参数，则data的值已经改变了
	
# 要避免这个问题，可以如下设置
def f(a, data=None):
	if data == None:
		data = []
	data.append(a)
	return data
	
# 如果一个函数需要传入的参数数量不固定，则需要为函数设置可变参数
# 调用函数时，在可变参数的位置直接传入一个元组、列表或者任意数量的参数
def connect(ipaddress ,*params):
	print("IP: ", ipaddress)
	for port in ports:
		print("Ports: ", port)
		
connect('192.168.1.1', *(22, 33, 44))
# 传入元组或列表需在前面加上*，相当于传入多个参数

# 关键字参数，允许传入零个或任意多个带参数名的参数，其中参数名可自定义
# 这些关键字参数在函数内部会形成一个字典
def connect(ipaddress, *ports, **kw):
	print("IP: ", ipaddress)
	for port in ports:
		print("Port: ", port)
	for key, value in kw.items():
		print('{}: {}'.format(key, value))
		
ipaddress = '192.168.1.1'
params = (25, 26, 27)
prop = {'device': 'eth0', 'proto': 'static'}
connect(ipaddress, *params, **prop)

# 命名关键字参数，调用参数时必须写上参数名，此参数的特征时前面有一个用逗号隔开的*
# def test(m, *, a, b) 则m为必选参数，a，b为命名关键字参数
# 缺少 * 则会将a，b视为必选/位置参数
# 调用时每一个命名关键字参数都必须使用相应的参数名赋值，否则抛出TypeError

def hello(*, name):
	print("Hello", name)
	
hello('hello')
# 无法调用，应该为hello(name='hello')


# 如果函数定义中已经有了可变参数，后面跟着的命令关键字参数就不需要用 * 隔开了
# 而且调用参数的时候，可变参数要在命令关键字参数之前	
def info(name, age, *args, city, job):
	print(name, age, args, city, job)

# 使用lambda创建匿名函数
sum = lambda arg1, arg2: arg1 + arg2









