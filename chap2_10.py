# 类和对象
# class Musician:
#     loveMusic = True
#
#     def sing(self):
#         print('我在唱歌')
#
#
# laoFan = Musician()
# print("音乐人老樊")
# print(laoFan.loveMusic)
# laoFan.sing()


# class Musician:
#     name = '羽泉'
#
#     def sing(self):
#         print(self.name + '是音乐人')  #的用法
#
#
# singer = Musician()
# print(singer.name)
# singer.sing()


# class Musician:
#     def __init__(self):
#         print('你好,这里是初始化方法init')
#
#     name = '羽泉'
#
#     def hello(self):
#         print('hello,大家好')
#
#     def sing(self):
#         self.hello()
#         print(self.name + '是音乐人')
#
#
# singer = Musician()
# singer.sing()


# class Musician:
#     def __init__(self,name,anotherName,music):
#         self.name = name
#         self.anotherName = anotherName
#         self.music = music
#     def intr(self):
#         print('各位歌迷好,我是%s' %self.name)
#         print('熟悉我的朋友都叫我%s' %self.anotherName)
#     def sing(self):
#         print('我为大家唱一首%s' %self.music)
# jam = Musician('萧敬腾','雨神','王妃')
# jam.intr()
# jam.sing()

import math


class Program:
    def __init__(self):
        self.key = 1

    # 工时计算
    def BOSS_input(self):
        # 设置默认参数
        self.types = int(input('请选择需要计算的工作：1-配送次数计算，2-快递员数计算，请选择'))
        self.sizes = float(input('请输入项目大小：1代表标准，还可以输入其他倍数或小数'))
        if self.types == 1:
            self.others = int(input('请输入投入的快递员数，请输入整数'))
        else:
            self.others = int(input('请输入快递次数，请输入整数'))

    # 计算工作量
    def calculate_job(self):
        print('计算结果如下')
        if self.types == 1:
            # 工时计算过程
            self.num = math.ceil(round((self.sizes * 100 / 20 / self.others), 2))
            print('%.1f个标准集装箱大的快递项目，使用%d位快递员配送，则需要配送次数%d次' % (self.sizes, self.others, self.num))
        elif self.types == 2:
            # 人力计算过程
            self.person = math.ceil(round((self.sizes * 100 / 20 / self.others), 2))
            print('%.1f个标准集装箱大的快递项目，%d次配送完毕，则需要快递员数：%d位' % (self.sizes, self.others, self.person))

    def again(self):
        num = input('是否继续计算？继续请输入y，输入其他键将结束程序。')
        if num != 'y':
            # 如果用户不输入'y'，则把key赋值为0
            self.key = 0

    def res(self):
        print('欢迎BOSS使用配送计算小程序')
        while self.key == 1:
            self.BOSS_input()
            self.calculate_job()
            self.again()
        print('工作辛苦。')


pro = Program()
pro.res()
