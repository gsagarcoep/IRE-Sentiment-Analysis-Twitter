import sys

#global score dictionaries
nrcht ={}
sa140 = {}

# for non contigous pairs we do not use score of last token and score of first token
## f1 is for nrcht and sa140 and ,
## 	1. total score of tokens for which score(token) > 0
##	2. total score of all tokens
##	3. max score
##
## So these 5 features will be for both the nrcht and sa140 lexicons - totalling to 10 features

def f1_lookup_and_compute(seg, dit):
	temp = seg.split()
	score_gt1 = 0.0
	score_total2 = 0.0
	score_max3 = -100000.0
	
	lg = len(temp)
	
	#for unigram - unigram pair
	for k in range(0, lg-2):
		i = temp[k] + " " + temp[k+2]

		if i in dit:
			if dit[i] > 0:
				score_gt1 += dit[i]

			if dit[i] > score_max3:
				score_max3 = dit[i]

			score_total2 += dit[i]

	if score_max3 == -100000.0:
		score_max3 = 0.0  #if there is no word in the dictionary then.

	a = [score_gt1, score_total2, score_max3]

	#Now, for unigram-bigram pair and bigram-unigram pair
	score_gt1 = 0.0
	score_total2 = 0.0
	score_max3 = -100000.0

	for k in range(0, lg-3):
		i = temp[k] + " " + temp[k+1] + " " + temp[k+3]

		if i in dit:
			if dit[i] > 0:
				score_gt1 += dit[i]
			
			if dit[i] > score_max3:
				score_max3 = dit[i]

			score_total2 += dit[i]


		j = temp[k] + " " + temp[k+2] + " " + temp[k+3]
		if j in dit:
			if dit[j] > 0:
				score_gt1 += dit[j]
			if dit[j] > score_max3:
				score_max3 = dit[j]

			score_total2 += dit[j]
	if score_max3 == -100000.0:
		score_max3 = 0.0  #if there is no word in the dictionary then.
	
	a += [score_gt1, score_total2, score_max3]

	#now for bigram-bigram pair
	score_gt1 = 0.0
	score_total2 = 0.0
	score_max3 = -100000.0

	for k in range(0, lg-4):
		i = temp[k] + " " + temp[k+1] + " "  + temp[k+3] + " " + temp[k+4]

		if i in dit:
			if dit[i] > 0:
				score_gt1 += dit[i]

			if dit[i] > score_max3:
				score_max3 = dit[i]

			score_total2 += dit[i]

	if score_max3 == -100000.0:
		score_max3 = 0.0  #if there is no word in the dictionary then.

	a += [score_gt1, score_total2, score_max3]

	return a

def make_featurelist(data):
	global nrcht, sa140
        a = f1_lookup_and_compute(data, nrcht)
        a += f1_lookup_and_compute(data, sa140)

	for i in a:
		print i,
	print
        return ''

def run_tweets(fname):
	f = open(fname, "r")
	ffl = [] #final feature list - contains the feature list of scores for each of the tweet.
	for line in f:
		temp = line[:-1]
		temp = temp.split('\t')
		ans = make_featurelist(temp[0])
		ffl.append(ans)
	return ffl


def fill_dict(dname, fname):
	f = open(fname, "r")
	for line in f:
		temp = line[:-1]
		temp = temp.split('\t')

		kl = temp[0].split('---')
		kl = " ".join(kl)
		dname[kl] = float(temp[1])
	f.close()
	
	
def main():
	global nrcht, sa140
	fn1 = sys.argv[1]  # the file containing the tweet tokens

	fn2 = './NRC_hashtag/pairs-pmilexicon.txt'
	fn3 = './sentiment140_lexicon/pairs-pmilexicon.txt'

	fill_dict(nrcht, fn2)
	fill_dict(sa140, fn3)

	scores = run_tweets(fn1)
#	print scores

if __name__ == "__main__":
	main()


