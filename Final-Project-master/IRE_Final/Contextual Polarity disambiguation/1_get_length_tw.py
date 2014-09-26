import sys

f = open(sys.argv[1], "r")

for line in f:
	temp = line[:-1]
	if temp == '':

		print 0
		continue
	
	temp = temp.split('\t')
	tw = temp[0]

	spt = tw.split()
	print len(spt)

f.close()
