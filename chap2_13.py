# 文件的读写

# print('开课吧'.encode('gbk'))
# print('开课吧'.encode('utf-8'))
# print(b'\xbf\xaa\xbf\xce\xb0\xc9'.decode('gbk'))
# print(b'\xe5\xbc\x80\xe8\xaf\xbe\xe5\x90\xa7'.decode('utf-8'))
# print(type('开课吧'))
# print(type(b'\xbf\xaa\xbf\xce\xb0\xc9'))
# print(type(b'\xe5\xbc\x80\xe8\xaf\xbe\xe5\x90\xa7'))

# with open(r'test.txt','a') as myfile:  # 建议使用with语句
#     myfile.write('你好')

# from kkb_tools import open_file
# myfile = open(r'test2.txt','a')
# myfile.write('从你的全世界路过')
# myfile.close()
# open_file('test2.txt')

myfile = open(r"C:\Users\Administrator\Desktop\python.txt", "r")
content = myfile.read(3)
conetnt1 = myfile.read()

myfile.close()
print(content)
print(conetnt1)
