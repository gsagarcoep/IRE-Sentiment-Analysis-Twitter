import sys

f = open(sys.argv[1], "r")

N = int(sys.argv[2])

for line in f:
	temp = line.split()
	l = len(temp)

	for i in range(l):
		print str(N+1+i) + ":" + temp[i],
	print

f.close()

