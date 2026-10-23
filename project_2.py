#数据的逻辑处理
#if 条件判断
 #完成B站登录功能的实现，正确账号和密码为18888888888/666888
"""
account = input("请输入您的账号：")
passport = input("请输入密码")
relaccount = '18888888888'
relpassort = '666888'
if account == relaccount and passport == relpassort:
    print("欢迎登录")
else:
    print("您的账号或密码错误")
"""

#判断平年还是闰年
#非整百年份，且能被4整除的年份是闰年
#整百年份，必须能被400整除才是闰年
"""
year = int(input("请输入年份："))

if year % 100 != 0:
    if year % 4 == 0:
        print("该年是闰年")
    else:
        print("该年是平年")
else:
    if year % 400 == 0:
        print("该年是闰年")
    else:
        pring("该年是平年")
"""

#判断数字是整数，负数还是零
#如果 数字>0 正数；如果数字 <0，负数；负责 0
"""
num = int(input("请输入数字："))

if num > 0:
    print("该数字是正数")
elif num < 0:
    print("该数字是负数")
else:
    print("该数字是0")
"""

#根据输入用户名，密码进行登陆系统
#用户名，密码为 admin/666888 或者 root/547524 或者 zhangsan/123456
"""
account = input("请输入用户名")
passport = int(input("请输入密码"))

if account == 'admin' and passport == 666888:
    print("欢迎登陆")
elif account == 'root' and passport == 547524:
    print("欢迎登陆")
elif account == 'zhangsan' and passport == 123456:
    print("欢迎登陆")
else:
    print("您的账号或密码错误")
"""

#请根据输入的考试成绩，判断成绩等级
"""
grade = int(input("请输入学生的考试成绩："))

if grade >= 85:
    print("该同学成绩为优秀")
elif grade >= 60 and grade < 85:
    print("该同学成绩为及格")
else:
    print("不及格")
"""


#购物折扣
"""
amount = int(input("请输入本次购物总金额"))

if amount >= 500:
    print(f"请支付{amount * 0.8}元")
elif amount >= 300 and amount <= 500:
    print(f"请支付{amount * 0.9}元")
elif amount <= 300 and amount >= 100:
    print(f"请支付{amount * 0.95}元")
else:
    print(f"请支付{amount}元")
"""

#判断三角形类型
"""
len1 = int(input("三角形第一条边长："))
len2 = int(input("三角形第二条边长："))
len3 = int(input("三角形第三条边长："))

if (len1 + len2 > len3) and (len1 + len3 > len2) and (len2 +len3 > len1):
    if len1 ==len2 and len2 == len3:
        print("等边三角形")
    elif (len1 == len2) or (len2 == len3 ) or (len1 == len3 ):
        print("等腰三角形")
    #如果是三边相等的话，直接第一条就确认了，就不会向下执行了
    else:
        print("普通三角形")
else:
    print("不能构成三角形")
"""

#match模式匹配
#结构模式匹配就是用一个清晰的 模板 去精确的匹配数据的结构和内容， 匹配成功则执行相应的操作
# | 是或的意思
# _表示匹配其他所有情况
"""
day = input("请输入星期几（1-7）")
match day:
    case "1":
        print("周一：工作会议日")
    case "2":
        print("周二：学习培训日") 
    case "3":
        print("周三：项目开发日")
    case "4":
        print("周四：代码审查日")
    case "5":
        print("周五：总结规划日")
    case "6" | "7":
        print("周末：休息放松日")  
    case _:
        print("输入错误")

"""

#实现一个计算器，可以实现 + - * /，用户输入需要运算的两个数以及运算符之后，就可以进行运算
# /号除数不能为0
"""
num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))

syn = input("请输入需要的运算符（+ - * /） ：")
match syn:
    case "+":
        print(f"{num1} + {num2} 的值为：{num1 + num2} ")
    case "-":
        print(f"{num1} - {num2} 的值为：{num1 - num2} ")
    case "*":
        print(f"{num1} * {num2} 的值为：{num1 * num2} ")
    case "/" if num2 !=0:  #if条件成立，才能匹配这个case
        print(f"{num1} / {num2} 的值为：{num1 / num2} ")
    case _:
        print("输入错误")
"""

#match:基于某个变量的多个固定值进行分支判断时，可以使用match模式匹配
#if:条件判断设计复杂的逻辑判定，范围比较以及组合条件时

#请编写一个游戏角色移动控制系统，根据不同指令执行相应操作

"""
motion = input("请输入指令（上，下，左，右，跳跃，攻击，退出）：")

match motion:
    case "上" | "w" | "W":
        print("向上")
    case "下" | "s" | "S":
        print("向下")
    case "左" | "a" | "A":
        print("向左")
    case "右" | "d" | "D":
        print("向右")
    case "跳" | " ":
        print("跳跃")
    case "双击" | "j" | "J":
        print("攻击")
    case "退出" | "esc" | "ESC":
        print("退出")  
    case _:
        print("无效操作")  
"""

#循环
# while 条件表达式：
#     循环体语句1
#     循环体语句2
#     ……
#打印十遍“人生苦短，我用python”
"""
i = 0
while i < 10:
    print("人生苦短，我用python")
    i += 1
"""

#计算1-100之间所有偶数的累加之和
"""
num = 1
acc = 0

while num < 101:
    if num % 2 == 0:
        acc += num 
    num += 1

print(f"1-100之间所有偶数的累加之和为{acc}")
"""

#for循环，本质是一种轮询遍历机制，对一批内容进行逐个处理
# for 元素 in 待处理数据集：
#     循环体代码（对元素进行处理）
# else：
#     循环结束时，执行的代码

#遍历字符串“Hello-python”
"""
msg = "Hello-python"

for i in msg:
    print(i)
else:
    print("循环结束")
#其中i就是变量，里面就是遍历出来的元素
"""

#while循环：循环的次数通常是未知的，只知道循环开始/结束的条件；
#for循环：用于一个已知的数据集进行遍历或已知次数的循环

#基于for循环完成如下要求：
#计算1-100之间所有奇数之和
#range语句：根据制定规则的数字序列
#用法1：range(end) 获取一个从0开始，到end结束的数字序列（不含end)本身
#用法2：range(start , end ) 获取一个从start开始，到end结束的数字序列（不含end)本身
#用法3：range(start , end , step)获取一个从start开始，到end结束的数字序列，step步长（不含end本身）
#range(0 , 10 , 2) 获得的数据就是0.2.4.6.8

"""
smg = range(1 , 101)
total = 0 

for i in smg:
    if i % 2 != 0:
        total = total + i 

print(f"1-100之间所有奇数之和为{total}")
"""

#要计算100-500之间所有3的倍数的数字之和
"""
smg = range(100 , 501)
total = 0

for i in smg:
    if i % 3 == 0:
        total += i

print(f"1-100之间所有奇数之和为{total}")
"""

#嵌套循环
"""
for 元素 in 待处理的数据集：
    循环体的代码1
    循环体的代码2
    ……
    for 元素 in 待处理的数据集2：
        循环体的代码1
        循环体的代码2
        ……
    ……

"""

#打印一个长度为m,宽度为n的长方形，m和n为用户输入的
# ctrl + enter快速换行
#print("" end = "")表示输出结束不换行，同时" "表示输出的后面有一个空格
#print()可以表示换行
"""
#长度
m = int(input("请输入长方形的长为："))
#宽度
n = int(input("请输入长方形的宽为："))

for j in range(n):  #控制行
    for i in range(m):  #控制列
        print("*" , end=" ")
    print()
"""

#打印99乘法表
#一行行输出
#外层循环控制的是行（第二个数）
"""
for i in range(1,10):              #外层循环--控制行
    for j in range(1,i+1):         #内层循环--控制列
        print(f"{i} * {j} = {i * j}" ,end="\t")
    print()
"""

#需求1：根据输入的直角边的边长，打印等腰直角三角形

#外层循环控制行，内层循环控制列
"""
m = int(input("请输入等腰直角三角的腰长："))

for i in range(1,m+1):
    for j in range(1,i+1):
        print("*" , end="\t")
    print()
"""

#根据输入的数字，打印对应的数字金字塔
"""
m = int(input("请输入数字金字塔的数字："))

for i in range(1 , m+1):
    for j in range(1 , i+1):
        print(f"{j}" , end="\t")
    print()
"""
#打印国际象棋棋盘
"""
fig1 = input("请输入黑棋：")
fig2 = input("请输入白棋：")

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:                #奇偶互换
            print(f"{fig1}" , end="\t")
        else:
            print(f"{fig2}" , end="\t")
    print()
"""

"""
根据输入的用户名密码执行登录操作，具体要求如下：
1、正确的用户名和密码为：admin/666888，zhangsan/1234567,taoge/888666
2、如果登录失败，则继续输入用户名和密码登录
3、输入的用户名和密码不能为空！
4、登录成功：输出：登录成功，进入B站首页~
5、登录失败：输出：“用户名或密码错误，请重新输入！”
"""

"""
while True:
    username = input("请输入正确的用户名：")
    password = input("请输入正确的密码：")

    if username == "" or password == "":
        print("输入的用户名和密码不能为空！请重新输入")
        continue

    if username == "admin" and password == "666888" :
        print("登录成功，进入B站首页~")
        break #跳出循环
    elif username == "zhangsan" and  password == "1234567":
        print("登录成功，进入B站首页~")
        break#跳出循环
    elif username == "taoge" and  password == "888666":
        print("登录成功，进入B站首页~")
        break#跳出循环
    else:
        print("用户名或密码错误，请重新输入！")
"""

#用户名密码登录，正确的用户名和密码为admin/666888，zhangsan/1234567,taoge/888666。5次登录机会，输入错误五次，不允许再操作了

"""
for i in range(1,6):
    username = input("请输入正确的用户名：")
    password = input("请输入正确的密码：")

    if username == "" or password == "":
        print("输入的用户名和密码不能为空！请重新输入")
    
    if username == "admin" and password == "666888" :
        print("登录成功，进入B站首页~")
    elif username == "zhangsan" and  password == "1234567":
        print("登录成功，进入B站首页~")
        break#跳出循环
    elif username == "taoge" and  password == "888666":
        print("登录成功，进入B站首页~")
        break#跳出循环
    else:
        print("用户名或密码错误，请重新输入！")

else:
    print("登录失败五次，禁止继续登录")

"""

#猜数字游戏：
#系统随机生成一个随机数
# 用户根据提示猜数字，并将所猜数字输入系统
# 如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
# 如果猜对，系统自动退出，游戏结束

# import random
# random_number = random.randint(1,100)
#生成1-100之间，包含1和100的随机数
"""
import random
random_number = random.randint(1,100)

while True:

    num = int(input("请输入所猜数字："))

    if random_number < num:
        print("你猜大了")
    elif random_number > num:
        print("你猜小了")
    else:
        print("猜中了")
        break
"""

#需求1：将1-1000之间（含1000）所有的5的倍数的数字累加起来
# num = int(range(1,1001))
# total = 0

# while True:
#     if num % 5 == 0:
#         total += num

# print(f"1-1000之间所有的5的倍数之和为{total}")

#range(1, 1001) 不能直接赋值给 num 后当作整数使用
#range() 通常要配合 for 循环使用

"""
total = 0

for num in range(1,1001):
    if num % 5 == 0:
        total += num

print(f"1-1000之间所有的5的倍数之和为{total}")
"""

#统计字符串“akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd”中有多少个a和k
"""
total1 = 0
total2 = 0

smg = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"

for i in smg:
    if i == "a":
        total1 += 1
    elif i == "k":
        total2 += 1

print(f"字符串中共有{total1}个a以及{total2}个k")
"""
