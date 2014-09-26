import sys

f = open('unigram_model.txt', "r")

model = []
for line in f:
	li = line[:-1]
	model.append(li)

f.close()


f = open(sys.argv[1], "r")


for line in f:
	tem = line[:-1]
	tem = tem.split()
	l = len(tem)
	
	indexlist = []
	for i in range(l):
		if tem[i] in model:
			indexlist.append(model.index(tem[i]) + 1)

	il = sorted(list(set(indexlist)))

	for i in il:
		print str(i) + ":1",
	print 

f.close()

	
