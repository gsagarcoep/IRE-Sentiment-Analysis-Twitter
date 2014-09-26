import sys

#global score dictionaries
nrcht ={}
sa140 = {}
ol = {}
eln = {}


## f1 is for nrcht and sa140 and ,
## 	1. total score of tokens for which score(token) > 0
##	2. total score of all tokens
##	3. max score
##	4. score of last token
##	5. score of first token  (newly added)
##
## So these 5 features will be for both the nrcht and sa140 lexicons - totalling to 10 features

def f1_lookup_and_compute(seg, dit):
	temp = seg.split()
	score_gt1 = 0.0
	score_total2 = 0.0
	score_max3 = -100000.0
	score_lt4 = 0.0
	score_ft5 = 0.0

	#for last token
	if temp[-1] in dit:
		score_lt4 = dit[temp[-1]]

	#for first token
	if temp[0] in dit:
		score_ft5 = dit[temp[0]]

	for i in temp:
		if i in dit:
			if dit[i] > 0:
				score_gt1 += dit[i]

			if dit[i] > score_max3:
				score_max3 = dit[i]

			score_total2 += dit[i]

	if score_max3 == -100000.0:
		score_max3 = 0.0  #if there is no word in the dictionary then.
	return [score_gt1, score_total2, score_max3, score_lt4, score_ft5]


def make_featurelist(data):
	global nrcht, sa140, ol, eln
        a = f1_lookup_and_compute(data, nrcht)
        a += f1_lookup_and_compute(data, sa140)
        a += f1_lookup_and_compute(data, ol)
        a += f1_lookup_and_compute(data, eln)

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
		dname[temp[0]] = float(temp[1])
	f.close()
	
def fill_dict_space(dname, fname):
	f = open(fname, "r")
	for line in f:
		temp = line[:-1]
		temp = temp.split(' ')
		dname[temp[0]] = float(temp[1])
	f.close()
	
def main():
	global nrcht, sa140, ol, eln
	fn1 = sys.argv[1]  # the file containing the tweet tokens

	fn2 = './NRC_hashtag/unigrams-pmilexicon.txt'
	fn3 = './sentiment140_lexicon/unigrams-pmilexicon.txt'
	fn4 = './opinion_lexicon/complete_dict.txt'
	fn5 = './NRC_emotion_unigram.txt'

	fill_dict(nrcht, fn2)
	fill_dict(sa140, fn3)
	fill_dict_space(ol, fn4)
	fill_dict_space(eln, fn5)

	scores = run_tweets(fn1)
#	print scores

if __name__ == "__main__":
	main()


