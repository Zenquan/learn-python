import re

str = '123acd, add, afd, agd_&\n\t\r '
print(re.findall('a[cdf]d', str))
print(re.findall('a[c-f]d', str))
print('^' , re.findall('a[^c-f]d', str))
print(re.findall('\d', str))
print(re.findall('\D', str))
print(re.findall('\W', str))
print(re.findall('\w', str))
print(re.findall('\s', str))
print(re.findall('\S', str))