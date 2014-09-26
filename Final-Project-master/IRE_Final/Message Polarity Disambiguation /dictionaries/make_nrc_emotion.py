import sys

f = open(sys.argv[1], "r")


### the scores for positive and negative ones
sp = +2
sn = -2

for line in f:
	temp  = line.split()
	if len(temp) <= 1:
		continue

	score = 0.0
	jk = float(temp[1].split(":")[1]) #positive vale ka number
	lm = float(temp[2].split(":")[1]) #negative vale ka number

	score = jk*sp + lm*sn
	print temp[0] +" " + str(score)

f.close()
