import requests

res = requests.get('https://xiaoke.kaikeba.com/example/gexu/tengwanggexu.txt')
print(type(res))
print(res.status_code)
print(res.content)
novel=res.text
print(novel)
print(res.encoding)
# print(res)
# response 四大属性  status_code content text encoding





