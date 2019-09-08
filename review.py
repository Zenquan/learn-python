list1 = [1, 2, 3, 4, 5, 2,2 ]

print(list1[0], list1[1], list1[3])
print(1 in list1, len(list1))

# list1.clear()
# print('list1.clear', list1)

list2 = list1.copy()
print('list.copy', list2)

print('list.count', list1.count(2))

print('list1.index', list1.index(2, 3))

list1.insert(3, 66)

print('list1.insert',list1)

list1.pop()
print('list1.pop', list1)

list3 = [222]

list1.extend(list3)
print(list1)

list1.reverse()
list1.remove(5)

print(list1)

# list1.append(9)
list1.sort()
print('list.sort',list1)
print('list1 + list2', list1 + list2)
# for i in list1:
  # print(i)
  # print(list1[i])

tup = (1, 2,3)
# tup[0] = 2
print(tup[0])

for t in tup:
  print(t)
print(1 in tup, len(tup))
sets = {1, 2,3}
# print(sets[1])
# sets.add(4)
# for s in sets:
#   print(s)
sets2={2,3,4}
print('sets|set2', sets | sets2)
print('sets-set2', sets - sets2)
print('sets&set2', sets & sets2)