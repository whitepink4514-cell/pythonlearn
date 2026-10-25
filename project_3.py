#数据存储容器
#一种可以容纳多份数据的数据类型（容器），容纳的每一份数据成为一个元素，每一个元素都可以是任何类型的数据，比如：字符串，数字，布尔等
#五种数据容器：列表，字符串，元组，集合，字典

#列表（list)
#列表名称 = [元素1 ， 元素2 ， 元素3 ……]
#可以存储不同类型的元素
#元素有序 ，可以重复，元素可以修改
#列表的索引/下标是从0开始，例如 s[0]就是获取第一个元素，向右递加
#也可以是反向索引，例如s[-1]就是列表最后一个元素，向左递减

"""
#定义列表
s = [56 , 90 , 88 , 65 ,"A" , "Hello" , True]
print(type(s))

#访问列表元素
#获取
print(s[0])  #正向索引
print(s[-7])  #反向索引

#修改
s[4] = "ABC"
print(s)

#删除
del s[5]
print(s)

#遍历
for item in s:
    print(item)
"""

#列表的切片
#切片是指对操作的数据截取其中一部分的操作。列表，字符串，元组都支持切片操作
#序列数据[开始索引：结束索引：步长] 
#不包含结束索引位置对应的元素，开始索引未指定默认为0；结束索引未指定默认为列表长度；步长未指定默认为1
#正向索引和反向索引都是可以的
"""
s = [56 , 90 , 88 , 65 ,"A" , "Hello" , True]

print(s[1:5:2])
print(s[:-2:])
"""

#列表的常用方法就是指列表这种数据类型内置的常见功能（添加元素，删除元素等）
# append() 在列表的尾部添加元素 s.append(10086)
# insert() 在指定索引之前，插入该元素 s.insert(0,92)
# remove 移除列表中第一个匹配到的元素 s.remove(75)
# pop() 删除列表中指定索引位置的元素（如果未指定索引，默认删除最后一个） s.pop(2)/s.pop()
# sort() 对列表进行排序（列表元素的数据类型一致，才可以进行排序） s.sort()
# reverse() 反转列表元素  s.reverse()

"""
s = [56 , 90 , 88 , 65 , 90 , 100 , 209 , 72 , 145]
print(s)

s.append(188)
print(s)

s.insert(2 , 80)
print(s)

s.remove(90)
print(s)

s.pop(1)
print(s)

s.pop()
print(s)

#pop()删除列表中指定索引位置的元素并返回
e = s.pop()
print(e)

s.sort()  #升序排序，从小到大
print(s)

s.reverse()
print(s)

"""

#将用户输入的十个数字，存储到一个列表里，并将列表中的数字进行排序，输出其中的最小值，最大值以及平均值

"""
#1、定义列表
num_list = []
#2、将用户输入的数字存入列表中
for i in range(10):
    num = int(input("请输入一个数字"))
    num_list.append(num)

print("数字列表：",num_list)
      
#3、排序
num_list.sort()
print("排序后的数字列表：" , num_list)

#4、输出
print("最小值：" , num_list[0])
print("最大值：" , num_list[-1])
#sum()求和，len()获取元素的个数
print("平均值：" , sum(num_list)/len(num_list))
"""

#合并两个列表中的元素，并将合并的结果进行去重复处理
#如何判断一个元素是否在列表中：
#可以使用in运算符，语法为：元素 in 列表
#返回结果为布尔值，True代表存在，False代表不存在
"""
num_list1 = [19 ,23 ,54 ,64 ,875 , 20 , 109 , 232 , 123 , 54]
num_list2 = [55 , 80 , 72 , 35 , 60 , 123 , 54 , 29 , 91]

#合并列表
for num in num_list2:
    num_list1.append(num)

print(num_list1)

#去除重复元素
new_list = []  #去除重复后的列表

for num in num_list1:
    #判断new_list中是否存在num元素
    if num not in new_list:
        new_list.append(num)

print(new_list)


#合并两个列表中的元素，并将合并的结果进行去重复处理  (简化)
num_list1 = [19 ,23 ,54 ,64 ,875 , 20 , 109 , 232 , 123 , 54]
num_list2 = [55 , 80 , 72 , 35 , 60 , 123 , 54 , 29 , 91]

#合并列表
#解包：将列表这一容器解开成一个一个独立的元素
#组包：将多个值合并到一个容器中
num_list = [*num_list1 , *num_list2]

print(num_list)
#去除重复元素
new_list = []  #去除重复后的列表

for num in num_list:
    #判断new_list中是否存在num元素
    if num not in new_list:
        new_list.append(num)

print(new_list)

#合并两个列表中的元素，并将合并的结果进行去重复处理  （方法三）
num_list1 = [19 ,23 ,54 ,64 ,875 , 20 , 109 , 232 , 123 , 54]
num_list2 = [55 , 80 , 72 , 35 , 60 , 123 , 54 , 29 , 91]

#合并列表
num_list = num_list1 + num_list2

print(num_list)

#去除重复元素
new_list = []  #去除重复后的列表

for num in num_list:
    #判断new_list中是否存在num元素
    if num not in new_list:
        new_list.append(num)

print(new_list)
"""

#生成一个1-20的平方列表
#从如下数字列表中提取所有偶数，并计算其平方，组成一个新的列表
"""
#方法1：
sq_list = []

for num in range(1,21):
    sq_list.append(num**2)


print("1-20的平方列表为：" , sq_list)

new_list = []
for num1 in sq_list:
    if num1 % 2 == 0:
        new_list.append(num1 ** 2)

print("从数字列表中提取的偶数平方组成的列表为：" , new_list)

"""
"""
#方法2：列表推导式-->就是按照一定的规则快速生成一个列表的方法-->语法格式：
#[要插入的值 for i in 列表/序列 if 条件]

num_list = [num**2 for num in range(1,21)]
print(num_list)

new_list = [num ** 2 for num in num_list if num % 2 == 0]
print(new_list)
"""


#字符串

#字符串的基本操作
"""
s = "Hello-python"

print(s[4]) #正向索引
print(s[-8])

#字符串是不可变的，无法修改

for i in s:
    print(i ,end="\t")

print()

#切片
print(s[:5:])
print(s[6::])
print(s[-1:-7:-1])  #python反转了nohtyp
print(s[::-1])  #nohtyp-olleH
"""

#字符串常用方法
# s.find("python")  在字符串中查找子串，返回第一次出现的索引位置，找不到返回-1
# s.count("H")  统计字串在字符串中出现的次数
# s.upper()  将字符串中所有字母转换为大写，返回大写的结果，但是不改变字符串本身
# s.lower()  将字符串中所有字母转换为小写，返回小写的结果，但是不改变字符串本身
# s.split(' ')  将字符串按照指定分隔符分割为列表
# s.strip()/s.strip("*") 去除字符串两端的空白字符或者指定字符
# s.replace("H","C")将字符串中的指定子串替换为新的子串
# s.startwith("P")检查字符串是否以指定子串开头，返回布尔值
"""
s = "Hello-pyhton-Hello-world"

index = s.find("-") #返回第一次出现的索引位置
print(index)

c = s.count("o")
print(c)

su = s.upper()
print(su)

sl = s.lower()
print(sl)

slist = s.split("-")
print(slist)

ss = s.strip()  #去除字符串两端的空格
print(ss)

sr = s.replace("-" , "_")
print(sr)

print(s.startswith("Hello"))
print(s.endswith("Python"))
#但是原始字符串是不变的
"""

#案例
#邮箱格式验证：用户输入一个邮箱，验证邮箱格式是否正确（包含一个@和至少一个.），如果输入正确，输出“邮箱格式正确”
#否则输出“邮箱格式错误”
"""
mail = input("请输入您的邮箱：")

if mail.count("@") == 1 and mail.count(".") > 0:
    print("邮箱格式正确")
else:
    print("邮箱格式错误")
"""

#输入一个字符串，判断该字符串是否是回文（两边对称）
"""
# 黄山落叶松叶落山黄  上海自来水来自海上
msg1 = "黄山落叶松叶落山黄"
msg2 = "上海自来水来自海上"

if msg1[::-1] == msg1:
    print(f"{msg1}是回文")
else:
    print(f"{msg1}不是回文")

if msg2[::-1] == msg2:
    print(f"{msg2}是回文")
else:
    print(f"{msg2}不是回文")
"""

#将用户输入的十个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来
"""
# 创建空列表
new_list = []

# 输入10个字符串
for i in range(10):
    word = input(f"请输入第{i+1}个字符串：")

    # 反转字符串
    word = word[::-1]

    # 转换为大写
    word = word.upper()

    # 添加到列表
    new_list.append(word)

# 遍历输出列表
for word in new_list:
    print(word)
"""

#元组
#元组一旦被定义，就不能修改
#元组是不可变的序列，可以存储不同类型的元素，溯源可以重复，有序，不支持修改（支持索引访问，切片）
#定义元组
#t1 = (5,7,9,,1,2,3,10,6,4,8,12,7,5)
#t2 = ()
#t3 = tuple()
#方法：count():统计某元素在元组中出现的次数  index():查找某个元素在元组中的索引位置（第一次出现的位置）
#[]是索引

"""
t1 = (80 , 95 , 78 , 50 , 76 , 80 , 85 , 20)

print(t1)
print(type(t1))

#索引访问
print(t1[0])
print(t1[-1])

#切片
print(t1[:3:])

#count()统计元素的个数
print(t1.count(80))

#index()获取元素的索引（第一个元素的位置）
print(t1.index(80))

#如果定义单元素的元组，单个元素之后需要加上逗号，比如（100，）
t2 = (100,)
print(type(t2))
"""

#元组的组包和解包
#组包：将多个值合并到一个容器（元组，列表）中
#解包：将容器（元组，列表）解开成独立的元素，分别赋值给多个变量

"""
t1 = (5 , 7 , 9 , 1)
t2 = 5 , 7 ,9 , 7

#基础解包
a , b , c , d = t1  #左边接收数据，右边提供数据

#(*)扩展包
x , *y , z = t2  #x为5 ， y为[7 , 9] , z为1
s , *o = t2  # s为5 ， o为[7 ， 9 ， 1]
*o ,s = t1  # o为[5 , 7 , 9] s为1
#在元组解包时，*表示收集剩余的所有元素，允许我们处理不确定数量的元素（生成列表，以便于可以进行进一步的处理）


"""

#完成以下案例：
#1、现有两个变量，分别为a = 10 , b = 20，现需要将这两个变量值交换，然后输出到控制台
#2、现有三个变量，分别为a = 100 , b = 200 , c = 300，现需要将这三个变量值进行交换，将a , b , c的值分别赋值给c , a , b，并将其输出到控制台

"""
#现有两个变量，分别为a = 10 , b = 20，现需要将这两个变量值交换，然后输出到控制台
a = 10
b = 20

a , b = b , a     # b , a 其实就是组包
print(a)
print(b)

a = 100
b = 200
c = 300

c , b , a = a , b ,c
print(a , b , c)
"""

#案例：根据提供的学生成绩单，完成如下需求：
# 1、计算每个学生的总分、单科平均分、然后一并输出
# 2、统计各科成绩的最低分，最高分，平均分，并输出
# 3、查找成绩优秀（平均分大于90）的学生，并输出

"""
students = (
    ("s001","王琳",85 , 92 ,78),
    ("s001","李牧婉",92,88,95),
    ("s003","十三",79,85,82),
    ("s004","曾牛",88,79,91)
)

# 1、计算每个学生的总分、单科平均分、然后一并输出 --->{avg:.1f}保留1位小数
print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")

#方式一：
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    print(f"{s[0]}\t {s[1]}\t {s[2]} \t{s[3]} \t{s[4]} \t{total} \t{avg:.1f}")

#方式二：
for id , name , chinese , math , english in students:  #直接把s解包了
    total = chinese + math + english
    avg = total / 3
    print(f"{id}\t {name}\t {chinese} \t{math} \t{english} \t{total} \t{avg:.1f}")


print()
# 2、统计各科成绩的最低分，最高分，平均分，并输出
#2.1 获取到各科的成绩列表
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]
#2.2 统计各科成绩的最低分，最高分以及平均分
print(f"语文最低分:{min(chinese_scores)},最高分：{max(chinese_scores)},平均分为：{sum(chinese_scores)/len(chinese_scores)}")
print(f"数学最低分:{min(math_scores)},最高分：{max(math_scores)},平均分为：{sum(math_scores)/len(math_scores)}")
print(f"英语最低分:{min(english_scores)},最高分：{max(english_scores)},平均分为：{sum(english_scores)/len(english_scores)}")

print()
#3、查找成绩优秀（平均分大于90）的学生，并输出
print("优秀学生名单如下：")
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    if avg > 90:
        print(f"学号：{s[0]} , 姓名：{s[1]} , 平均分：{avg}")
"""

#集合（set)
#列表，元组是可以存储重复元素的
#set会自动去重

#集合（set)是一种无序的，不可重复的，可修改的数据容器
#定义
# s1 = {"S","A","D","E"}
# s2 = set()

#空集合的定义不可以使用{},{}表示的是空字典；由于集合是无序的，因此是不支持下标索引访问的

# s1 = {5,3,2,0,9,12,43,64,22,5,0}

# print(s1)
# print(type(s1))

# s1.add("t")  添加元素到集合中
# s1.remove("t")  移除集合中的指定元素（指定元素不存在将报错）
# e = s1.pop()  随机删除集合中的元素并返回
# s1.clear()  清空集合
# s1.difference(s2)  求取两个集合的差集（包含在第一个集合但是不在第二个集合的元素）
# s1.union(s2)  求取两个集合的并集
# s1.intersection(s2)  求取两个集合的交集

"""
#选修足球的学生名单：
football_set = {"王林","曾牛","蓄力过","遁天","天云子","韩立","李飞宇","武丑","子陵"}
#选修篮球的学生名单：
basketball_set = {"张贴","模具人","王林","将唠叨","曾牛","王婵","韩立","天云子","丽花园","李飞宇","云路"}
#选修法语学生名单
french_set = {"序幕","王卓","十三","呼啸","将唠叨","天云子","红蝶","李飞宇","韩立","曾牛"}
#选秀艺术学生名单
art_set = {"遁天","天云子","韩立","呼啸","将唠叨","子陵"}

# 1、找出同时选修了法语和艺术的学生
#方式一：
print(french_set.intersection(art_set))

#方式二：& --> 交集
fa_set = french_set & art_set
print(f"同时选修了法语和艺术的学生：{fa_set}")


# 2、找出同时选修了所有四门课的学生
all_set = football_set & basketball_set & french_set & art_set
print(f"同时选修了四门课程的学生：{all_set}")


# 3、找出选修了足球，但是没有选修篮球的学生
#法一：
print(football_set.difference(basketball_set))

#法二：- --> 差集
fb_set = football_set - basketball_set
print(f"选修了足球，但是没有选修篮球的学生：{fb_set}")

#方式三：集合推导式 ---> 快速构建集合，语法：{要往集合中添加的数据 for s in set1 if 条件}
fb_set = {s for s in football_set if s not in basketball_set}
print(f"选修了足球，但是没有选修篮球的学生：{fb_set}")


# 4、统计每一个学生的课程数量
#获取到学生名单 -- 并集 |
all_set = football_set|basketball_set|french_set|art_set

#获取每一个学生对应选修课程数量
all_list = [*football_set , *basketball_set , *french_set , *art_set]   # *代表解包

for s in all_set:
    print(f"{s}选修了{all_list.count(s)}课程")


"""

#字典：通过【字/词】，找到该字对应的解释
#python中的字典（dict）,里面存储的是键值对 （key:value）类型的数据，可以根据键key找到对应的值value
#键值对（key:value）存储，键（key）不可以重复，可以修改
"""
#定义字典
字典名称 = {key:value , key:value , key:value……}
#定义空字典
字典名称 = {}
字典名称 = dict()

#根据key获取value
值 = 字典名称[key]
"""

#字典的基本操作
#key不能重复，如果重复了，后面的值会覆盖前面的值
#key必须是不可变类型（str , int , float , tuple）
"""
dict1 = {"王琳":670 , "李牧婉":580 , "韩立":680}

print(dict1)
print(type(dict1))

dict1["李牧婉"] = 688
print(dict1)
"""

"""
#添加
dict1['涛哥'] = 688  往指定字典中添加key-value 
#删除
score = dict1.pop("涛哥")  删除字典中指定的key，并返回该key对应的value
del dict1["涛哥"] 删除字典中指定的键值对
#修改
dict1["小智"] = 658 修改字典中指定的key对应的值
#查询
dict1["涛哥"]  根据key获取value
dict1.get("涛哥") 根据key获取value
dict1.values() 获取所有的value
dict1.items() 获取所有的key-value键值对
dict1.keys() 获取所有的key
"""
#遍历
# for k in dict1.keys():
#     print(f"{k}:{dict1[k]}")

# for item in dict1.items():
#     print(f"{item[0] : item[1]}")

# for k , v in dict1.items():
#     print(f"{k} : {v}")

#案例
# 开发一个购物管理系统，实现商品信息的添加，修改，删除，查询功能。系统使用字典结构存储商品数据
# 通过控制台菜单与用户交互。具体功能如下：
# 1、添加购物车：用户根据提示录入商品名称，以及该商品的价格，数量，保存该商品信息到购物车
# 2、修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格，数量，输入完成后修改该商品信息
# 3、删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品
# 4、查询购物车：将购物车中的商品信息展示出来，格式为：“商品名称：xxx,商品价格xxx,商品数量：xxx".
# 5、退出购物车
  #结构：shopping_cart = {"Mate80":{"price":6999 , "num":2} , "鼠标"：{}}

shopping_cart = {}

#1、制作菜单（同时按住Alt和shift，可以进行列编辑）
print("欢迎使用购物车管理系统 ~")

menu = """
######### 购物车系统 #########
#       1、添加购物车        #
#       2、修改购物车        #
#       3、删除购物车        #
#       4、查询购物车        #
#       5、退出购物车        #
##############################
"""
while True:
    print(menu)
    #2、执行的具体操作
    choice= input("请选择要执行的操作（1-5）：")

    match choice:
        case "1":  #添加购物车
            goods_name = input("请输入商品名称：")
            goods_price = float(input("请输入商品价格："))
            goods_num = int(input("请输入商品数量："))

            #如果商品存在，则不执行添加，提示信息
            if goods_name in shopping_cart:
                print("该商品已存在，请重新选择 ~")
            else:
                shopping_cart[goods_name] = {"price":goods_price , "num":goods_num}
                print("商品添加完成")

        case "2":  #修改购物车
            goods_name = input("请输入商品名称：")
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择 ~")
                continue

            goods_price = float(input("请输入商品价格："))
            goods_num = int(input("请输入商品数量："))

            #如果商品不存在，则提示错误信息，重新选择
            shopping_cart[goods_name] = {"price":goods_price , "num":goods_num}
            print("商品修改完毕")

        case "3":#删除购物车
            goods_name = input("请输入商品名称：")
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择 ~")
            else:
                del shopping_cart[goods_name]
                print("商品删除完毕")
        
        case "4":  #查询购物车
            if not shopping_cart:
                print("购物车为空，请先添加商品！")
            else:
                for goods_name in shopping_cart:
                    goods_info = shopping_cart[goods_name]
                    print(f"商品名称：{goods_name}，商品价格：{goods_info['price']}，商品数量：{goods_info['num']}")

        case "5":  #退出购物车
            print("baibai")
            break

        case _:  #匹配其他所有情况
            print("非法操作，不支持！")
