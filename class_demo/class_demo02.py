from class_demo01 import Animal

class Dog(Animal):
  def __init__(self):
    print('子类的构造方法')

  def childrenMethod(self):
    print('子类的方法')