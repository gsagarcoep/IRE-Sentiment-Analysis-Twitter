import sys

def makemodel(fn, n):
	f = open(fn, "r")
	model = []

	for line in f:
		tem = line[:-1]	
		tem = tem.split()
		l = len(tem)
		for i in range(l-n+1):
			a = tem[i:i+n]
			a = " ".join(a)
			if a not in model:
				model.append(a)
	
	model = sorted(model)
	for i in model:
		print i
	f.close()


def main():
	filen = sys.argv[1]
	n = int(sys.argv[2])
	makemodel(filen, n)

if __name__ == "__main__":
	main()
