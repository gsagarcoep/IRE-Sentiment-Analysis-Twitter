import sys

g = open("neg_words_potts.txt", "r")

#loading the model
negw = []
for line in g:
	tem = line[:-1]
	negw.append(tem)

g.close()

punct = [".", ":", ";", "!", "?"]

f = open(sys.argv[1], "r")

otherlist = ["\\", "^", "/", "@", "~", "!", "$", "%", "&", "*", "(", ")", "+", "-", "_", "[" , "]", "{", "}" , "|", ","]

#now going tweet by tweet.
for line in f:
	temp = line[:-1]
	tweet = temp.split()
	
	flag = 0 #for multiple cases

	newt = []
	for i in tweet:
		if i in negw and flag == 0:
			flag = 1 #negation started
			newt.append(i)

		elif i in negw and flag == 1:
			newt.append(i)	
		
		elif flag == 1 and i in punct:
			flag = 0
			newt.append(i)

		elif flag == 1:
			if i in otherlist:
				newt.append(i)
				continue
			newt.append(i+"_NEG")
			
		elif flag == 0:
			newt.append(i)
		
	print " ".join(newt)		

f.close()
