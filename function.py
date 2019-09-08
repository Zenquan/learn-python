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