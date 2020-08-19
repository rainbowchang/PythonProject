# 类的继承  python 可以多继承

# class Musician:
#     glasses = "墨镜"
#     loveMusic = True
#
#     def sing(self):
#         print('我在唱歌')
#
#
# class Rapper(Musician):
#     pass  # pass表示'跳过'，不执行其他操作
#
#
# mcHotdog = Rapper()
# print(mcHotdog.glasses)
# mcHotdog.sing()
#
# #直接运行
# class Car:
#     wheel = 4
#     def run(self):
#         print('有%d个轮子,可以飞速的行驶'%self.wheel)
# class BMW(Car):
#     pass
#
# BENZ600 = Car()  #使用Car类创建奔驰600
# BMW320 = BMW()   #使用BMW类创建BMW320
# print("验证:子类创建的实例也属于父类")
# print(isinstance(BENZ600,Car))
# print(isinstance(BMW320,Car))
# print("验证:父类创建的实例不属于不属于不属于子类")
# print(isinstance(BENZ600,BMW))
# print("验证:所有类创建的实例都属于根类")
# print(isinstance(BENZ600,object))
# print(isinstance(BMW320,object))


# 音乐人
# class Musician(object):
#     loveMusic = True
#     def intr(self):
#         print("我喜欢音乐")
#         print("我来自音乐界")
# #演说家
# class Orator(object):
#     speak = "流利的说"
#     def intr(self):
#         print("我喜欢演说")
#         print("我来自演讲界")
# # Rapper继承了音乐人与演说家
# class Rapper(Musician,Orator):
#     pass
#
# csunYuk = Rapper()
# print(csunYuk.loveMusic)
# print(csunYuk.speak)
# csunYuk.intr()   #和音乐这个类更亲近，即相同的函数左边的构造函数左边的优先级更高
#
# class master():
#     status = "厨师"
#     def cake(self):
#         print("制作手抓饼")
#     def cook(self):
#         print("制作传统煎饼果子")
# class apprentice(master):
#     def cook(self):
#         print("制作中西方口味融合的煎饼果子")
# print("师父")
# shifu = master()
# print(shifu.status)
# shifu.cake()
# shifu.cook()
# print("徒弟")
# tudi = apprentice()
# print(tudi.status)
# tudi.cake()
# tudi.cook()


class L(object):
    def fun(self):
        print('L func')


class M(L):
    def fun(self):
        super(M, self).fun()
        print('M func')


class X:
    def fun(self):
        print('X func')


class N(M, X):
    def fun(self):
        super().fun()
        print('N func')


obj = N()
obj.fun()
