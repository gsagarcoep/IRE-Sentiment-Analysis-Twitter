import sys

f = open(sys.argv[1], "r")

list1 = []
for line in f:
	temp = line[:-1]
	list1.append(int(temp))

f.close()

list2 = []

f = open(sys.argv[2], "r")
for line in f:
	temp = line[:-1]
	list2.append(int(temp))
f.close()

l = len(list1)

for i in range(l):
	print list1[i], list1[i] + list2[i]


	
