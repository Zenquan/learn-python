import json

data = {
  'no': 1,
  'name': 'Runoob',
  'url': 'https://www.runnoob.com'
}

json_str = json.dumps(data)
print(repr(data))
print(json_str['name'])

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])