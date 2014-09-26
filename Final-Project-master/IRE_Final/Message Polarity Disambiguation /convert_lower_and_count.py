import sys

f = open(sys.argv[1], "r")

clist = []
for line in f:
	tem = line[:-1]
	tem = tem.split()
	count = 0
	tw = []
	for i in tem:
		if i.isupper():
			count+=1
		tw.append(i.lower())
	clist.append(count)
	print " ".join(tw)
	
f.close()

f = open("count_capital.txt", "w")

for i in clist:
	f.write(str(i) + "\n")

f.close()
