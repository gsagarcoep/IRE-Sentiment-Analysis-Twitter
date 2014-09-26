import sys

f = open(sys.argv[1], "r")

N = int(sys.argv[2])

for line in f:
	temp = line.split()
	l = len(temp)

	for i in temp:
		print str(N+1+int(i))+ ":1",
	print

f.close()

