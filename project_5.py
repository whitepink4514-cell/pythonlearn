#函数进阶
#变量的作用域指的是变量的作用范围（标识这个变量在哪里可以使用，在哪儿不可以使用）
#全局变量：在函数之外定义的变量，称之为全局变量，在整个文件中（包括函数内）都可以使用（通常定义在文件的顶部）
#局部变量：在函数内部定义的变量，称之为局部变量，只能在函数内部使用，外部无法访问（函数执行完毕后，会自动销毁其内部局部变量）
"""
#num全局变量
num = 100

def circle_area(r):
    pi = 3.14
    area = pi * r * r

    num = 10000
    print("num = ", num)  #10000

    return area

c_area = circle_area(10)
print(c_area)

print("num = " , num)   #100
"""

#global 关键字用于明确告诉python解释器，在函数中要使用全局变量，使得可以在函数内部修改全局变量的值
#在基于global声明全局变量时，要先声明，再使用
"""
num = 1 #全局变量
def fun1():
    global num

    num = 100
    print(num)  #100

fun1()  #这就是在“调用”这个函数
print(num)  #100
""" 

#尽量避免在函数中使用全局变量，因为会使得代码难以维护和调试
#考虑使用函数参数和返回值来传递数据，而不是依赖全局变量
#global主要用在程序的状态、配置和计数器等场景中

#调试开关
"""
debug_mode = False

def enable_debug_mode():
    global debug_mode
    debug_mode = True
    print("调试模式已开启")

def disable_debug_mode():
    global debug_mode
    debug_mode = False
    print("调试模式已关闭")
"""

#函数参数详解：传参方式 、 默认参数 、 不定长参数

#1、位置参数：调用函数时，根据函数定义时的位置来传递参数。调用函数时参数顺序和定义函数时参数顺序完全一致
"""
#定义函数
def reg_stu(name, age, gender, city):
    print(f"注册成功,姓名:{name}, 年龄:{age}, 性别:{gender}, 城市:{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}


# 调用函数
stu = reg_stu("张三", 18, "男", "北京")
print(stu)

"""

"""
#2、关键字参数：调用函数时，以函数定义时形参名称作为关键字，以"键 = 值" 的形式传递参数（不要求顺序）
# 定义函数
def reg_stu(name, age, gender, city):
    print(f"注册成功,姓名:{name}, 年龄:{age}, 性别:{gender}, 城市:{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

# 调用函数
stu = reg_stu(name="张三", age=18, gender="男", city="北京")
print(stu)

stu2 = reg_stu(gender="男", name="王武", city="上海", age=22)
print(stu2)

stu2 = reg_stu("赵四", 28, gender="男", city="上海")        #两种传参方式混用
print(stu2)
"""
#如果位置参数与关键字参数混用，关键字参数必须在位置参数之后（关键字参数之间，没有顺序要求）

#位置参数：简洁；但是可读性差，易出错，维护难（适合参数少，不超过三个）
#关键字参数：代码繁琐，但是可读性强，易维护和扩展（参数较多或易混淆的场景）

#默认参数
#也称为缺省参数，用于在定义函数时，为参数提供默认值，调用函数时，可以不传递有默认值的参数
#注意：默认参数必须放在没有默认值的参数列表的后面，一个函数在定义时是可以设置多个默认参数的
#注意：函数调用时，如果为默认参数传递了值，则会修改默认的参数值；如果没有传递该参数，则直接使用默认值
"""
def reg_stu(name, age, gender='男', city='北京'):
    print(f"注册成功,姓名:{name}, 年龄:{age}, 性别:{gender}, 城市:{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

# 调用函数
stu = reg_stu(name="张三", age=18)
print(stu)

stu = reg_stu("张三", 18)
print(stu)
"""

#需求：定义函数，根据传入的数据，计算这批数据中的最大值，最小值以及平均值
#不定长参数 ， 也叫可变参数

#位置传递（*args）
#注意：传递的所有匹配的位置参数都会被args变量收集，这些参数会合并封装为一个组，args是元组类型（并不会封装关键字参数）
#args只是约定俗成的变量名，并不是关键字，这里可以使用任何合法的变量名（如*data）
"""
def calc_data(*args):
    max_data = max(args)
    min_data = min(args)
    avg_data = sum(args) / len(args)

    return max_data , min_data , avg_data

max_data , min_data , avg_data  = calc_data(10 , 20 , 30 , 40 , 50 , 60 , 70 , 80)
print(f"最大值为：{max_data} , 最小值为：{min_data} , 平均值为：{avg_data}")

max_data , min_data , avg_data  = calc_data(100 , 200 , 300 , 400)
print(f"最大值为：{max_data} , 最小值为：{min_data} , 平均值为：{avg_data}")
"""


#关键字参数（**args），封装到字典中

"""
def calc_data(*args , **kwargs):       
    # *args：把传入的位置参数（比如 2, 7, 9）打包成一个元组
    #**kwargs：把传入的关键字参数（比如 round=3, print=True）打包成一个字典（形如{"round": 3, "print": True}）

    max_data = max(args)
    min_data = min(args)
    avg_data = sum(args) / len(args)

    #处理四舍五入条件
    #kwargs.get("round")：尝试从字典里找键名为 "round" 的值。如果没有传这个参数，返回 None
    #如果传了（比如传了 round=3），就调用内置函数 round(平均数值, 保留几位小数)，并把处理后的值重新赋给 avg_data
    if kwargs.get("round") is not None:
        avg_data = round(avg_data , kwargs.get("round"))

    if kwargs.get("print"):
        print(f"计算出来的最小值：{min_data} , 最大值：{max_data} , 平均值为：{avg_data}")
    return max_data , min_data , avg_data

print(calc_data(2 , 7 , 9 , 10 , 45 , round=3 , print = True))
"""

#   *args 适用于处理数量不确定的数据
#   **kwargs适用于处理数量不确定的选项（函数的配置参数，用来定制函数的行为）

#参数类型
#普通参数：数字，布尔，字符串，列表，元组，集合，字典
#特殊参数：函数
"""
def add (x , y):
    return x + y
def substract (x , y):
    return x - y
def calc(x , y , oper):
    return oper(x , y)

result = calc(10 , 20 ,add)
print(result)
"""


#函数的参数类型
"""
#加
def add (x , y):
    return x + y

#减
def subtract (x , y):
    return x - y

#乘
def mutiply (x , y):
    return x * y

#除
def divide (x , y):
    if y == 0:
        return "错误：除数不能为0"
    return x / y

#建立字符串与函数对象的映射字典
operations = {
    "add" : add,
    "subtract" : subtract,
    "multiply" : mutiply,
    "divide" : divide

}

#计算
def calc(x , y , oper_str):
    #检查用户输入的操作是否在字典中
    if oper_str in operations:
        #根据字符串从字典中取出对应的函数对象，并调用它
        func = operations[oper_str]
        return func(x , y)
    else:
        return "错误：未知的操作符，请检查输入"


x = float(input("请输入x的值："))
y = float(input("请输入y的值："))

print("支持的操作：add , subtract , multiply , divide")
oper = input("请输入需要进行的操作:")

result = calc(x , y , oper)
print(f"计算结果：{result}")
"""

#匿名函数
#指的是没有名称的函数，需要通过lambda表达式来声明函数，可以简化简单函数的编写
# lambda 参数列表 ： 函数体

#函数逻辑比较简单（单行表达式）且只在一个地方使用时，可以考虑使用匿名函数，简化书写（通常作为高阶函数的参数使用）

"""
out_line = lambda : print("________________")

add = lambda x , y : x+y

out_line()
print(add(100 , 200))

"""

#需求：完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序：
"""
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
print(data_list)

data_list.sort(key=lambda item :len(item) , reverse=True)  #匿名函数典型应用场景
print(data_list)
"""

#命名函数与匿名函数的选择：
#匿名函数：函数逻辑简单，只在一个地方调用（常作为高阶函数的参数）
#命名函数：函数逻辑复杂，需要多步操作，需要多个地方重复使用或者需要加文档说明的场景


#案例1：定义一个函数，根据传入的数字，计算该数字阶乘的结果：（递归）
# n的阶乘公式：f(n) = n * f(n-1)
# 递归调用：指的是在函数中自己调用自己的情况 ---> 一定得有终结点,本题中终结点为1
"""
def jc(n):
    if n == 1:
        return 1
    else:
        return n * jc(n-1)

result = jc(10)
print(result)
"""

#定义一个函数，用于根据传入的一批商品信息（商品名 、 价格 、 数量）、优惠（优惠券、积分抵扣） 、 运费信息计算订单的总金额
#具体规则如下：
# 1、优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价
# 2、积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百扣除）
"""
# 计算订单总金额
def order_total(*args, coupon, score, express):
    #计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)

    #扣除优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon

    #扣减积分抵扣
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100

    #添加运费
    total_cost += express

    return total_cost

#测试
total = order_total(("鼠标",188,2),("键盘",388,1),("手机",6999,1),coupon=10,score=4000,express=9.9)
print(total)

"""

#类型注解
#类型注解是python中的一种语法特性，用于明确标识变量、函数参数和返回值的数据类型，从而使得代码更加清晰，安全，更易维护
"""
a: int = 695
score: float = 98.5
hobby: str = "Python"
flag: bool = True
pic: None = None

names: list[str | int] = ["A", "C", "E"]
phones: set[str] = {"13309091111", "15209109121"}
options: dict[str, int] = {"count": 0, "total": 0}  # key是str , vlaue是int
goods: tuple[str, int, int] = ("手机", 5999, 1)
"""
