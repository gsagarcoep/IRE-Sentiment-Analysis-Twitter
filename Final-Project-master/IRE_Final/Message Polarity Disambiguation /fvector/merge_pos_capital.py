import sys

f1 = "count_capital.txt" 
f2 = "fv_pos_count.txt"

n = 96277 + 20341

l1 = []

f = open(f1, "r")
for line in f:
	l1.append(line[:-1])
f.close()

l2 = []
f = open(f2, "r")
for line in f:
	l2.append(line[:-1].split())
f.close()

for i in range(len(l1)):
	l2[i].append(l1[i])
	


for i in range(len(l1)):
	for j in range(26):
		print str(n+j+1) +":" +  l2[i][j],
	print
