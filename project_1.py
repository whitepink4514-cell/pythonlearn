#布尔类型本质也是整数类型（True--1，False--0）
# print(True + 1)

"""
#课程基础播放量为20.7万
#每月新增播放量为50万
basic_volume = 207000
increase_volume = 500000
num1 = basic_volume + increase_volume
num2 = basic_volume + increase_volume*2

print ("未来两个月第一个月的播放量为：",num1)
print ("未来两个月第二个月的播放量为：",num2)
"""


#标识符：
#为变量，函数，类等元素所起的名字
#只能数字，字母，下划线，数字不能开头
#不能使用关键字
#严格区分大小写

#变量名命名规范：英文字母全小写，见名知意，多个部分使用下划线连接
"""
a = 10
b = 20
c = a 
a = b 
b = c
print(a , b)
"""

"""
print(type(None))
print(type(True))

# isinstance()检查数据是否属于指定的类型，返回的是一个布尔值
# 具体语法为：isinstance(数据，类型)
num = 5.0
print(num)
print(isinstance(num , int))

"""


# 字符串定义方式：单引号，双引号，三引号
# s3 = """尊敬的客户：

# 您好。
# """
# print(s3)
"""
#单引号定义
s2 = 'It\'s very intersting'
s3 = 'very intersting it\'s '
s4 = "Hello 的意思是\"你好\""
"""

# \'表示单引号
# \"表示双引号
# \n表示换行
# \t 增加缩进，缩进一个制表符（tab）的大小

#字符串的拼接
#+可以用来拼接两个字符串，但是无法将非字符串和字符串进行拼接，需要转换为字符串类型
"""
slogan = "黑马程序员"+"成就IT"
print(slogan)

msg = "我的数学成绩是"
print(msg + str(9) + "分")
"""

#大家好，我叫涛哥，今年18岁，学习的专业是软件工程，爱好是Python，Java
"""
name = "涛哥"
age = 18
major = "软件工程" 
hobby = "Python、Java"
print("大家好，我叫"+name+",今年"+str(age)+"岁,学习的专业是"+major+",爱好是"+hobby)
太繁琐了
"""

#字符串的格式化
#通过 %占位符 的形式完成字符串和变量的快速拼接
#其中 % 表示我要占位，s 表示将变量转为字符串放入占位的位置
"""
s1 = "涛哥"
print("大家好，我是 %s ,欢迎大家进入python的学习" % s1)

name = "涛哥"
age = 18
major = "软件工程" 
hobby = "Python、Java"
print("大家好，我是 %s , 今年 %s 岁 , 学习的专业是 %s , 爱好是 %s" %(name , age , major , hobby) )
"""


#也可以通过f"内容{变量/表达式}"完成快速格式化
"""

name = "涛哥"
age = 18
major = "软件工程" 
hobby = "Python、Java"
print(f"大家好，我是{name},我今年{age}岁，我的专业是{major},我的爱好是{hobby}")
"""

#输入与输出
"""
name = input("请输入您的姓名：")
print(f"欢迎您，{name}")

age = input("请输入您的年龄：")
print(f"您今年{age}岁")
"""

"""
name = input("请输入您的姓名：")
age = input("请输入您的年龄：")
print(f"您的姓名为{name},您的年龄为{age}")
"""

#银行卡中有10000元，现在到ATM进行取钱操作，请根据输入的金额执行取钱操作，取钱完毕后，展示银行卡的余额
#input 接受的是字符串，不能直接计算
"""
num = 10000
print(f"您的余额为{num}元")
withdraw = int(input("请输入取款金额"))
amount = num - withdraw

print(f"请输入您的取款金额：{withdraw}")
print(f"您现在的余额为：{amount}")
#也可以最后直接num - int(withdraw)
"""

#算术运算符 //整除  %取余  **幂指数
#算术运算优先级 ** --> * / // % --> + - 
#要求输入两个数，分别计算其和和减
"""
x = input("请输入x的值：")
y = input("请输入y的值：")
print(f"x+y的值为{int(x) + int(y)} , x-y的值为{int(x) - int(y)}")
"""

#赋值运算符
#例如： = += -= *= /= %= //= **=
#有浮点数参与到，结果就是浮点数，就是那个浮点数之后都是浮点数

#比较运算符，也称为关系运算符
#会比较运算符两边的表达式，然后返回一个布尔值作为结果，True表示关系成立
#例如： == a是否等于b  ！=  a是否不等于b  > a是否大于b
# print('"100" != 100 吗 ', "100" != 100)

#逻辑运算符  and,or not(取反操作，True变成False)
#用于连接多个条件的布尔表达式，其值为真或假，并返回一个最终布尔结果的运算符

#键盘输入一个整数，判断这个数字是否在10-20之间
# num = int(input("请输入一个整数："))
# if num>10 and num<20:
#     print("这个数字在10-20之间")
# else:
#     print("这个数字不在范围内")

# num = int(input("请输入一个整数："))
# print(f"{num}不在10-20之间: " , num < 10 or num > 20)

#数据的逻辑处理
#