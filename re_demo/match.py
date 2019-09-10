import re

# print(re.match('www', 'www.baidu.com, www.sohu.com'))
# print(re.match('www', 'http://www.baidu.com, www.sohu.com'))
# print(re.search('www', 'http://www.baidu.com, www.sohu.com').span())

phone = '2004-959-559 # 这是一个国外电话号码'
num = re.sub(r'#.*$', '', phone)
print("phone", num)