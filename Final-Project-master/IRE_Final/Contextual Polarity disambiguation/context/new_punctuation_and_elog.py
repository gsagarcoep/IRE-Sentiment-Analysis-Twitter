import sys
import re

f = open(sys.argv[1], "r")

countlist = []
pattern = re.compile(r"(.)\1{1,}", re.DOTALL)

# three features - !,?, combination of !,?
# and elongation also
for line in f:
	temp = line.split()
	count1 = 0
	count2 = 0
	count3 = 0
	count4 = 0

	newtw = []
	for i in temp:
		hf = pattern.sub(r"\1\1", i)
		if hf != i:
			count4 += 1
			
		v = re.search(r'([!]+[?]+[!?]*)|([?]+[!]+[!?]*)', i)
		if v is not None:
			count3 += 1
			continue

		v = re.search(r'[!]+' , i)
		if v is not None:
			count1 += 1

		v = re.search(r'[?]+', i)
		if v is not None:
			count2 += 1

	print " ".join([str(count4) , str(count1), str(count2), str(count3)])

