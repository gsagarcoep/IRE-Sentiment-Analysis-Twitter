import sys
f = open(sys.argv[1], "r")

for line in f:	
	temp = line.split()

	if temp == []:
		continue

	temp = int(temp[0])
	
	if temp == 0:
		print "Neutral sentiment" 
	elif temp== 1:
		print "Positive sentiment"
	else :
		print "Negative sentiment"
