import time

# ticks = time.time()

# print(ticks)

# localtime = time.asctime(time.localtime(ticks))

# print(localtime)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

print(time.strftime('%a %b %d %H:%M:%S %Y', time.localtime()))

a = 'Tue Sep 10 18:25:05 2019'
print (time.strptime(a,"%a %b %d %H:%M:%S %Y"))