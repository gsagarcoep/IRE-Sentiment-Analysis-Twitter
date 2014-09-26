import sys

def makemodel(fn, n, d):
	f = open(fn, "r")
	model = {}

	for line in f:
		tem = line[:-1]	
		tem = tem.split()
		l = len(tem)
		for i in range(l-n+1):
			a = tem[i:i+n]
			a = " ".join(a)
			if a not in model:
				model[a] = 1
			else:
				model[a] += 1
	

	for i in model:#looping over keys
		if model[i] > d:
			print i
	f.close()


def main():
	filen = sys.argv[1]
	n = int(sys.argv[2])
	delta = int(sys.argv[3]) # this parameter should be 0 for unigram and 1 for bigram.
	makemodel(filen, n, delta)

if __name__ == "__main__":
	main()
