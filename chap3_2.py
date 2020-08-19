# import requests
# from bs4 import BeautifulSoup
# #引入BS库
# res = requests.get('https://xiaoke.kaikeba.com/example/canteen/index.html')
# html = res.text
# soup = BeautifulSoup(html,'html.parser') #把网页解析为BeautifulSoup对象
# print(soup)




# import requests
# from bs4 import BeautifulSoup
#
# res = requests.get('https://xiaoke.kaikeba.com/example/canteen/index.html')
# html = res.text
# soup = BeautifulSoup(html,'html.parser')
# items = soup.find_all(class_='show-list-item') # 通过匹配标签和属性提取我们想要的数据
# print('*' * 30)
# print(items) # 打印items
# print(type(items)) #打印items的数据类型

# import requests
# from bs4 import BeautifulSoup
# res = requests.get('https://xiaoke.kaikeba.com/example/canteen/index.html')
# html = res.text
# soup = BeautifulSoup(html,'html.parser')
# items = soup.find_all(class_='show-list-item')
# print("想找的菜的信息都在这里了：")
# for item in items:
#     print(item) # 打印item
#     print('%' * 30)



import requests
from bs4 import BeautifulSoup
res = requests.get('https://xiaoke.kaikeba.com/example/canteen/index.html')
html = res.text
soup = BeautifulSoup(html,'html.parser')
items = soup.find_all(class_='show-list-item')
for item in items:
    print('*' * 40)
    title = item.find(class_='desc-title') # 在列表中的每个元素里，匹配属性class_='title'提取出数据
    material = item.find(class_='desc-material') #在列表中的每个元素里，匹配属性class_='desc-material'提取出数据
    step = item.find(class_='desc-step') #在列表中的每个元素里，匹配属性class_='desc-step'提取出数据
    print(title.text,material.text,step.text)
