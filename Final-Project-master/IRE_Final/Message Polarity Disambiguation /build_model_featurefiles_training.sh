
### FV Files already obtained:
### 	1. count_capital.txt  (feature for ALL CAPS - 1 feature)
###	2. count_emoticon_class.txt (feature for emoticon class counts - 7 features)

python get_pos_count.py tags_of_tweet.txt  > fv_pos_count.txt  #for 25 POS tags

python new_punctuation_and_elog.py final_lnnt.txt > fv_punct_and_elong.txt #for 4 features (for 4 different counts)


python cluster_fv.py final_lnnt.txt > fv_of_cluster_tw.txt  #for 1000 cluster fv

###now worrying about sentiment scores
# the python scripts and the datasets are in ~/Dropbox/dictionaries/ folder
python ~/Dropbox/dictionaries/get_sent_score_unigram.py final_lnnt.txt $HOME > fv_score_unigram.txt # 20 features - from 4 dicts
python ~/Dropbox/dictionaries/get_sent_score_bigram.py final_lnnt.txt $HOME > fv_score_bigram.txt # 10 features - from 2 dicts
python ~/Dropbox/dictionaries/get_sent_score_noncont.py final_lnnt.txt $HOME > fv_score_noncont.txt # we have 2 dicts, total 18 features (9 features from each 1)

## now making use of word n-grams.
python make_ngram_with_thresh.py final_lnnt.txt 1 0  > unigram_model.txt

python make_ngram_with_thresh.py final_lnnt.txt 2 1 > bigram_model.txt

#python make_ngram_model.py final_lnnt.txt 3 > trigram_model.txt

#now we need to build the features correspoding to unigram and bigram models

python construct_unigram.py final_lnnt.txt > features/fv_svm_1_unigram.txt

a=`wc -l < unigram_model.txt`

python construct_bigram.py final_lnnt.txt $a > features/fv_svm_2_bigram.txt

b=`wc -l < bigram_model.txt`

let c=$a+$b

#python construct_trigram.py final_lnnt.txt $c > features/fv_svm_3_trigram.txt


paste count_capital.txt count_emoticon_class.txt fv_pos_count.txt fv_punct_and_elong.txt fv_score_unigram.txt fv_score_bigram.txt fv_score_noncont.txt -d " " > fv_3456789.txt

x=`wc -l < trigram_model.txt`

#let d=$c+$x  ##use this when trigram is used as feature
let d=$c ##this is used when trigram is not being used.

python merge_3to9.py fv_3456789.txt $d > features/fv_svm_3to9.txt

m=`head -1 fv_3456789.txt | wc -w `
let e=$d+$m  #change is 85 if more features are added later.

python add_index_to_cluster.py fv_of_cluster_tw.txt $e > features/fv_svm_10.txt





