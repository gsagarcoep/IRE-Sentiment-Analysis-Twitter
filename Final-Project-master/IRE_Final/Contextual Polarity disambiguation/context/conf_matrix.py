test = open("label_test.txt",'r');
out = open("output",'r');

#test -> postive out -> postive TP[1]++
#test -> negative out -> negative TP[2]++
#test -> neutral out -> neutral TP[3]++

#test -> Negative out -> neutral FN[2]++
#test -> negative out -> postive FN[2]++
total = 0
test_arr = []
out_arr = []
#for line in test:
#	line.strip("\n")
#	test_arr.append(line)
for line in test:
     test_arr.extend([int(number) for number in line.split()])
for line in out:
     out_arr.extend([int(number) for number in line.split()])
Matrix = [[0 for x in xrange(3)] for x in xrange(3)] 

for i in range(len(test_arr)):
	Matrix[test_arr[i]+1][out_arr[i]+1] = Matrix[test_arr[i]+1][out_arr[i]+1] +1
	total = total + 1
def confusion_table(matrix, given_class):
	"""Returns a confusion table in the following format:
	   [[true positives, false negatives],
	   [false positives, true negatives]]
	  for the given given_class index in the confusion matrix.
			  """
	predicted = matrix[given_class]
	actual    = [matrix[i][given_class] for i in range(len(matrix))]
	true_pos  = predicted[given_class]
	false_pos = sum(actual) - true_pos
	false_neg = sum(predicted) - true_pos
	total     = sum([sum(i) for i in matrix])
	true_neg  = total - true_pos - false_pos - false_neg
        return [[true_pos, false_neg],
	    [false_pos, true_neg]]
#print test_arr
#print out_arr
#print Matrix
# This prints the Matrix for Negative Class"
Neg_M = confusion_table(Matrix, 0)
# This prints the Matrix for Neutral Class"
Neu_M = confusion_table(Matrix, 1)
# This prints the Matrix for Postive Class"
Pos_M = confusion_table(Matrix, 2)

#print Neg_M, Neu_M, Pos_M
def recall_function(matrix):
	return 1.0*matrix[0][0]/(matrix[0][0] + matrix[0][1])
def precision_function(matrix):
	return 1.0*matrix[0][0]/(matrix[0][0] + matrix[1][0])
def fcall(recall,precision):
	return 2*recall*precision/(recall+precision) 

print "----Recall----"
# Recall for Negative Class
negr = recall_function(Neg_M)
# Recall for Neutral Class
neur = recall_function(Neu_M)
# Recall for Positive Class
posr = recall_function(Pos_M)
print (negr + neur + posr)/3
print "----Precision----"

# Precision for Negative Class
negp = precision_function(Neg_M)
# Precision for Neutral Class
neup = precision_function(Neu_M)
# Precision for Positive Class
posp = precision_function(Pos_M)
print (negp + neup + posp)/3

print "----F-Call----"

# F-Call for Negative Class
#print fcall(negr, negp)
# F-Call for Neutral Class
#print fcall(neur, neup)
# F-Call for Positive Class
#print fcall(posr, posp)
print (fcall(negr, negp) + fcall(neur, neup )+ fcall(posr, posp))/3

 
acc = 0
for i in range(3):
	acc = acc + Matrix[i][i]

print "----Accuracy----"
print 1.0*acc/total
