import re

# str = '123acd, add, afd, agd_&\n\t\r '
# print(re.findall('a[cdf]d', str))
# print(re.findall('a[c-f]d', str))
# print('^' , re.findall('a[^c-f]d', str))
# print(re.findall('\d', str))
# print(re.findall('\D', str))
# print(re.findall('\W', str))
# print(re.findall('\w', str))
# print(re.findall('\s', str))
# print(re.findall('\S', str))

# str2 = 'python 1111java678php'
# r = re.findall('[a-z]{3, 6}', str2)
# print(r)
# a = 'pytho0python1python2'
# r1 = re.findall('python*', a)
# r2 = re.findall('python?', a)
# r3 = re.findall('python+', a)
# r4 = re.findall('python{1, 2}', a)
# print(r1, r2, r3, r4)

qq = '10001'
r= re.findall('^\d{4, 8}', qq)
print(r)