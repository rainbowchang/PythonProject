from bs4 import BeautifulSoup

bs = BeautifulSoup('<div><span>床前明月光，</span><span>疑是地上霜。</span><span>举头望明月，</span><span>低头思故乡。</span></div>','html.parser')
tag = bs.find('div')
print(tag.text)