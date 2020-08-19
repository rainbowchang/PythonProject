import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
res_movies = requests.get('https://movie.douban.com/chart',headers=headers)
# 获取数据
bs_movies = BeautifulSoup(res_movies.text,'html.parser')
# 解析数据
list_movies= bs_movies.find_all('div',class_='pl2')
# 查找最小父级标签

list_all = []
# 创建一个空列表，用于存储信息

for movie in list_movies:
    tag_a = movie.find('a')
# 提取第1个父级标签中的<a>标签
    name = tag_a.text.replace(' ', '').replace('\n', '')
# 电影名，使用replace方法去掉多余的空格及换行符
    url = tag_a['href']
# 电影详情页的链接
    tag_p = movie.find('p', class_='pl')
# 提取第1个父级标签中的<p>标签
    information = tag_p.text.replace(' ', '').replace('\n', '')
# 电影基本信息，使用replace方法去掉多余的空格及换行符
    tag_div = movie.find('div', class_='star clearfix')
# 提取第1个父级标签中的<div>标签
    rating = tag_div.text.replace(' ', '').replace('\n', '')
# 电影评分信息，使用replace方法去掉多余的空格及换行符
    list_all.append([name,url,information,rating])
# 将电影名、URL、电影基本信息和电影评分信息，封装为列表，用append方法添加进list_all

print(list_all)
# 打印