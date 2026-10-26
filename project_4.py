#函数
#函数是组织好的，可以重复使用的，用来实现特定功能的代码片段

"""
#函数基础
def 函数名（参数列表）：
    函数体
    ……
    return 返回值

#调用函数
函数名（参数）
"""

#注意：函数定义的时候的参数列表与返回值语句是可有可无的（由需求决定）
#函数必须先定义后调用执行（函数定义时，内部代码并未执行，在调用时才会执行）

# def out_line():
#     print('__________')

# out_line()        #通过函数名就可以调用函数了

# out_line()

# out_line()


#函数的参数以及返回值
#这就是 return 最重要的作用：把函数计算出的结果交给外部代码，让外部代码继续使用

"""
#定义圆的面积
def circle_area(r):     #r为形参
    area = 3.14 * r * r
    return area

c_area = circle_area(10)        #10为实参
print(f"半径为10的圆的面积为:{c_area}")

#计算长方形的面积
def rectangle_area(len , wid):
    area = len * wid
    return area

c_area = rectangle_area(10 , 5)
print(f"长方形的面积为:{c_area}")
"""

#如果不写return , 就直接print(rectangle_area(10 , 5)),return就是把值返回给 rectangle_area(10 , 5)

#函数3：计算圆的面积和周长 ---> 如果返回值有多个，多个返回值之间逗号分隔 ---> 多个返回值封装到元组中
"""
def circle_area_len(r):
    return 3.14 * r * r , round(2 * 3.14 * r , 1)       #round(数字（四舍五入）  ， 保留小数位)

circle_area_len(10)
al = circle_area_len(10)
print(al)

print(type(al))

area , len = circle_area_len(10)  #解包操作
print(area)
print(len)
"""

#函数的说明文档   parameter参数 perimeter周长

# def circle_area_len(r):
#     """
#     :parameter r : 圆的半径
#     :return : 圆的面积，圆的周长
#     """
#     return 3.14 * r * r , round(2 * 3.14 * r , 1)       #round(数字（四舍五入）  ， 保留小数位)

# circle_area_len(10)
# al = circle_area_len(10)
# print(al)
# help(circle_area_len)

#嵌套调用指的是在一个函数中，又调用另外一个函数
#函数调用遵循栈结构，最后被调用的函数最先返回LIFO（Last in first out , 后进先出）
"""
def function_a():
    print("a ... before")
    function_b()
    print("a ... after")


def function_b():
    print("b ... before")
    function_c()
    print("b ... after")


def function_c():
    print("c ...")


function_a()

# function_a()开始
#     打印"a ... before"
#     调用function_b()
#         打印"b ... before"
#         调用function_c()
#             打印"c ..."
#         打印"b ... before"
#         function_b()返回
#     打印"a ... after"
#     function_a() 返回
"""

#完成如下需求：
# 1、定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底 * 高/2）
# 2、定义一个函数：计算传入的字符串中元音字母的个数（元音字母位 aeiouAEIOU）
# 3、定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分，最低分，平均分（保留1位小数）并返回

"""
#定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底 * 高/2）
def triangle_area(base , height):
    area = base * height / 2 
    return area

print("底长为30，高为20的三角形面积为：" , triangle_area(30 , 20))

#计算传入的字符串中元音字母的个数（元音字母位 aeiouAEIOU）
def count_aeiou(s):
    num = 0
    for w in s :
        if w in "aeiouAEIOU":
            num += 1

    return num
#法一：
count = count_aeiou("Hello Python Hello world")

print(count)
#法二：
print(count_aeiou("Hello Python Hello world"))

#计算传入的班级学员高考成绩列表中成绩的最高分，最低分，平均分（保留1位小数）并返回
def calculate_score(score_list):
    
    # 计算传入的班级学员高考成绩列表中成绩的最高分，最低分，平均分
    # : parameter score_list:分数列表
    # : return :最高分，最低分，平均分
    
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list) / len(score_list) , 1)

    return max_s , min_s , avg_s

s_list = [589 , 566 , 570 , 455 , 480 , 479 , 720 , 766]
max_s , min_s , avg_s = calculate_score(s_list)
print(f"班级成员高考成绩的最高分为：{max_s} , 最低分为{min_s} , 平均分为{avg_s}")

"""

#练习
"""
# 定义一个函数，根据传入的分数，计算对应分数的等级
# 分数 >= 90 : A  分数 >= 75 :B  分数 >= 60 :C  分数< 60:D
def grade_score(score):
    if score < 0 or score > 100:
        return "分数无效"
    elif score >= 90:
         return  "A"
    elif score >= 75:
         return  "B"
    elif score >= 60:
         return  "C"
    else:
         return  "D"

#用户输入分数
score = float(input("请输入您的分数："))
grade = grade_score(score)
print(f"{score}分对应的成绩等级为：{grade}")

"""

#定义一个函数，用于判断一个字符串是否为回文串，返回bool值。
"""
def jud_str(msg):
    if msg[::-1] == msg:
        return True
    else:
        return False

msg = input("请输入需要判断的字符串：")
result = jud_str(msg)
print(f"{msg}是否为回文串：{result}")

#法二：
def jud_str(msg):
    return msg[::-1] == msg

msg = input("请输入需要判断的字符串：")
result = jud_str(msg)
print(f"{msg}是否为回文串：{result}")
"""

"""
#定义一个函数：完成时间转换功能，将传入的秒转换为小时，分钟，秒
def switch_time(time):
    hour = time // 3600
    minute = time % 3600 // 60
    second = time % 60
    return hour , minute , second

time = int(input("时间转换器，请输入秒数："))
hour , minute , second = switch_time(time)
print(f"{time}秒是：{hour}小时{minute}分钟{second}秒")
"""


#定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边，等腰，普通，或者不能构成三角形）
def type_triangle(len1 , len2 , len3):
    if (len1 + len2 <= len3) or (len1 + len3 <= len2) or (len3 + len2 <= len1):
        return "不能构成三角形"
    elif len1 == len2 and len2 == len3 :
        return "等边三角形"
    elif len1 == len2 or len2 == len3 or len1 == len3:
        return "等腰三角形"
    else:
        return "普通三角形"

len1 = int(input("请输入三角形第一条边："))
len2 = int(input("请输入三角形第二条边："))
len3 = int(input("请输入三角形第三条边："))

result = type_triangle(len1, len2, len3)

print(f"三角形的类型为：{result}")

