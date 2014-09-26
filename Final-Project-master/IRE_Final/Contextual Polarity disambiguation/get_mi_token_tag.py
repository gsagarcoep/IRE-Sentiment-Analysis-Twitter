import sys

f = open('indices_tw.txt', "r")

indlist = []
for line in f:
	temp = line[:-1]
	temp = [int(x) for x in temp.split() ]
	indlist.append(temp)

f.close()

f = open(sys.argv[1], "r")

flag = int(sys.argv[2]) # for value = 1, we will get marked instance
			# for value = 0, we will get context

entiretw = []
for line in f:
	tem = line.split()
	entiretw.append(tem)

f.close()

for i in range(len(entiretw)):
	if entiretw[i] == '':
		continue
	start = indlist[i][0]
	end = indlist[i][1]


	if flag == 0 : #context

		a = entiretw[i][:start]
		b = a + entiretw[i][end:]

		print " ".join(b)
	elif flag == 1:
		print " ".join(entiretw[i][start:end])
		

	
