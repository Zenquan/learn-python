fo = open('./1.txt', 'r+', -1, 'utf8', None, None)
print(fo.name, fo.buffer, fo.encoding)

line = fo.readline(100)
print('%s' % line)

fo.close()