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
# print(dog.name, dog.age, dog.price)
# print(dog.get_name(), dog.get_age(), dog.run())
# # print(dog.__dict__, Animal.__dict__)
# print(Animal.__name__)
# print(Animal.__doc__)
# print(Animal.__module__)
# print(Animal.__bases__)

# dog2 = dog
# dog3 = dog
# print(id(dog), id(dog2), id(dog3))

# del dog
# del dog2
# del dog3