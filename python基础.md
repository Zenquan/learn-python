# python学习

![](https://ws1.sinaimg.cn/large/005Pf0eLgy1g6u7cn7lqwj30ss0nwwip.jpg)

## 标准数据类型

### 数字

进制转化

```py
bin()转化成二进制
int()转化成十进制
hex()转化成十六进制
oct()转化成八进制
```



### 序列

1. 有索引，可用于取值，不过最好的取值方式是**解包**
2. 切片`[start: end:step]`: start开始，end结束，step步长（默认为1）
3. in、not in 、len()

##### list、tuple

```py
list1=[1,2,3,4]
vs
tuple1=(1,2,3,4)
```

区别：list可变、tuple不可变

```py
list1[0] = 2
tuple1[0] = 2 x 报错

list1.append(5)
list1.pop(5)
tuple1.append(5) x 报错
tuple1.pop(5) x 报错
```

### 集合

set(可变)

1. 无序无索引
2. 不重复
3. len、in、 not in
4. | ：并集 、 &：交集 、- ：差集

```py
set1 = {1, 2, 3,4}
set1[0] x 报错
```



```py
set2 = {5, 1, 3, 4}
set1 | set2 // {1,2,3,4,5}
set1 & set2 // {1, 3, 4}
set1 - set2 // {2}
```

### 值类型和引用类型

值类型：Number、String、Tuple

引用类型： list、set、dict

```py
n1 = 3
n2 = n1
n1 = 4
n2 // 3
```



```py
l1 = [1,2,3]
l2 = l1
l1[0] = 4
l2[0] // 4
```



![](https://ws1.sinaimg.cn/large/005Pf0eLgy1g6u8vrlsauj30ig0j8mxa.jpg)

## 条件控制和循环语句

```py
if xx:

	pass

else:

	pass

if xx:

	pass

elif:

	pass
```



```py
for...in...
while xx:
	pass
```

## 枚举

```py
from enum import Enum

Colors = Enum('Colors',('red', 'yellow'))

for name, member in Colors.__members__.items():
    print(name, '=>', member, ',', member.value)
```



## 函数

1. 形参、实参
2. 默认参数
3. 可变参数（*xx）组装成tuple
4. 关键参数（**kw）or （xx=xx）组装成dict

```py
name = 'zenquan'

def praise (name):
  if name == 'zenquan':
    print('You are so great!')

praise('zenquan')

def noop():
  pass

noop()

# def my_abs(num):
#   if not isinstance(num, (int, float)):
#     raise TypeError('bad operand type')

#   if num >= 0:
#     return num
#   else:
#     return -num

# my_abs('12')

def pover(x, n=2):
  s = 1
  while n>0:
    n = n-1
    s = s * x

  return s

print(pover(4,3))

def cal(*numbers):
  sum = 0
  for number in numbers:
    sum = sum + number ** 2
  print(numbers)
  return sum

# print(cal([1,2,3]))
# print(cal((1,2,3)))
print(cal(1,2,3))
cal()

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Bob', 35, city='Beijing')
```



## 类

类与对象

类：用于描述真实事物的抽象映射，拥有方法和属性

对象：类经过实例化之后得到的实例

```py
#!/usr/bin/python
#-*-coding: UTF-8-*-

# 类：对现实事物的描述映射， 拥有着属性和方法
# 实例化之后得到的实例拥有着实例变量和方法
class Animal(): 
  # .__doc__
  '所有动物的基类'
  # 数据成员 = 类变量 + 实例变量
  # .__dict基类的类属性
  sum = 0 # 类变量， 动物的种类总数

  # 实例变量
  def __init__(self, name, age, price):
    self.name = name
    self.age = age
    self.price = price

  # 实例有获取名字的方法
  def get_name(self):
    return self.name

  # 实例有获取年龄的方法
  def get_age(self):
    return self.age

  # 实例有奔跑的方法
  def run(self):
    print('%s can run' % self.name)

  def __del__(self):
    class_name = self.__class__.__name__
    print(class_name, '销毁')

dog = Animal('Jo', 3, 300)
print(dog.name, dog.age, dog.price)
print(dog.get_name(), dog.get_age(), dog.run())
# print(dog.__dict__, Animal.__dict__)
print(Animal.__name__)
print(Animal.__doc__)
print(Animal.__module__)
print(Animal.__bases__)

dog2 = dog
dog3 = dog
print(id(dog), id(dog2), id(dog3))

del dog
del dog2
del dog3


继承

from class_demo01 import Animal

class Dog(Animal):
  def __init__(self):
    print('子类的构造方法')

  def childrenMethod(self):
    print('子类的方法')
```

## 连接mysql

```py
# -*-coding: utf-8-*-
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='test_mysql'
)
mycursor = mydb.cursor()

mycursor.execute('CREATE DATABASE test_mysql')
mycursor.execute('SHOW DATABASES')

for x in mycursor:
    print(x)

mycursor.execute('CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))')

mycursor.execute('SHOW TABLES')

for x in mycursor:
    print(x)

mycursor.execute('DROP DATABASE test')

mycursor.execute(
    'CREATE TABLE IF NOT EXISTS `runoob_tbl`('
    '`runoob_id` INT UNSIGNED AUTO_INCREMENT,'
    ' `runoob_title` VARCHAR(100) NOT NULL,'
    '`runoob_author` VARCHAR(40) NOT NULL,'
    '`submission_date` DATE,'
    'PRIMARY KEY ( `runoob_id` )'
    ')ENGINE=InnoDB DEFAULT CHARSET=utf8;'
)

mycursor.execute(''
    'ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY'
)

sql = 'INSERT INTO sites (name, url) VALUES  (%s, %s)'
val = ('Runoob', 'http://www.baidu.com')
mycursor.execute(sql, val)
mydb.commit()
print('插入成功')

sql = 'INSERT INTO sites (name, url) VALUES (%s, %s) '
val = [
    ('taobao', 'https://www.taobao.com'),
    ('jd', 'https://www.jd.com'),
    ('souhu', 'https://www.souhu.com'),
    ('didi', 'https://www.didi.com'),
    ('tencent', 'https://www.qq.com')
]

mycursor.executemany(sql, val)
mydb.commit()
print('批量插入成功')

sql = 'SELECT name, url from sites ORDER BY name DESC LIMIT 3 OFFSET 1'
sql = 'DELETE FROM sites WHERE name="taobao"'
mycursor.execute(sql)
# myresult = mycursor.fetchall()
mydb.commit()

# for x in myresult:
#     print(x)

sql = 'UPDATE sites SET url="https://www.zenquan.cn", name="sohu" where url=%s'
url = ('https://www.souhu.com',)
mycursor.execute(sql, url)
mydb.commit()

sql = 'DROP TABLE IF EXISTS runoob_tbl'
mycursor.execute(sql)

sql1 = '''
    SELECT name, SUM(singin) as singin_count from employee_tbl GROUP BY name
'''
sql2 = '''
    SELECT name, COUNT(*) from employee_tbl GROUP BY name
'''
mycursor.execute(sql1)


myresult = mycursor.fetchall()

print(myresult)

```



