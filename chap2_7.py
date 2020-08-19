# food = input("请问您想吃什么?请输入：")
# def cook(x):
#     str = '您好，欢迎来到KFC餐厅，您的点餐为' + x
#     return str
# res = cook(food)
# print(res)


# def menu(hamburger, drink, snacks='蛋挞'):  #默认参数 snacks
#     print('汉堡选择：' + hamburger)
#     print('饮料选择：' + drink)
#     print('小食选择：' + snacks + '\n')
#
# menu('香辣鸡腿堡','可乐')
# menu('老北京鸡肉卷','雪碧')
# menu('培根烤鸡腿堡','橙汁')
# menu('培根烤鸡腿堡','橙汁','薯条')

# def menu(*food):
#     for i in food:
#         print('点餐内容：' + i)
#
#
# menu('香辣鸡腿堡', '可乐')
# menu('卤肉饭', '老北京鸡肉卷', '雪碧', '可乐')
# menu('烤串', '火锅', '培根烤鸡腿堡', '橙汁', '薯条', '甜筒')


# trump = '所有餐厅都要卖【兰州拉面】'
#
#
# def kfc():
#     global harland
#     harland = '所有KFC餐厅卖烤串'
#     print('KFC餐厅：%s' % trump)
#     print('KFC餐厅：%s' % harland)
#
#
# def mcdonald():
#     print('麦当劳餐厅：%s' % trump)
#     print('麦当劳餐厅：%s' % harland)
#
#
# kfc()
# mcdonald()

# def fun(x, y=2, z=9):
#     print(x, y, z)
#
# fun(2, z=4)

# def fun(x, y):
#     z = x * x * y
#     return x, y, z
#
#
# print(fun(2, 5))
# x, d, zs = fun(2, 6)
#
# print(x, d, zs)

a = 100


def func1():
    global a
    print("a= {}".format(a))
    a = 200
    print("a= {}".format(a))


def func2():
    print("a= {}".format(a))


func1()
func2()
