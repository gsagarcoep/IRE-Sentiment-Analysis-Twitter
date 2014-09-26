import sys
import os

f = open('trigram_model.txt', "r")

model = []
for line in f:
	li = line[:-1]
	model.append(li)

f.close()


f = open(sys.argv[1], "r")

N = int(sys.argv[2]) # count of number of lines in the bigram_model.txt
n = 3 # since trigram so n = 3
 
for line in f:
	tem = line[:-1]
	tem = tem.split()
	l = len(tem)
	
	indexlist = []
	for i in range(l-n+1):
		kl = " ".join(tem[i:i+n])
		if kl in model:
			indexlist.append(model.index(kl) + N + 1)

	il = sorted(list(set(indexlist)))

	for i in il:
		print str(i) + ":1",
	print 

f.close()
