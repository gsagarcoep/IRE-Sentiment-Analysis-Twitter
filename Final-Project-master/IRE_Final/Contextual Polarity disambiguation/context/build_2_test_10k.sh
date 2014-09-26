a=10000
b=`wc -l < final_mi_tokens.txt`
let c=$b-$a

#Running individual features for both the marked instance and context

head -$a final_context_tokens.txt > train_context_tokens.txt
head -$a final_context_tags.txt > train_context_tags.txt

python count_emoticon.py train_context_tokens.txt

#	So count_emoticon_class.txt is created.

python convert_lower_and_count.py train_context_tokens.txt > lower_context_tok.txt

#	The marked instance is converted to lower case.

#  Running the previous script file - count_capital.txt is created.

#4. This is for counting pos tags for the tweet tags:

python get_pos_count.py train_context_tags.txt > fv_pos_count.txt  

#5. for punctuation and elongation:

python new_punctuation_and_elog.py lower_context_tok.txt > fv_punct_and_elog.txt

## we are not doing cluster in this part


#6. Now doing the score part:

python ~/Dropbox/dictionaries/get_sent_score_unigram.py lower_context_tok.txt $HOME > fv_score_unigram.txt

 python ~/Dropbox/dictionaries/get_sent_score_bigram.py lower_context_tok.txt $HOME > fv_score_bigram.txt

#7. building the unigram model,

#python make_ngram_model.py lower_context_tok.txt 1 > unigram_model.txt
#python make_ngram_model.py lower_context_tok.txt 2 > bigram_model.txt


#8. constructing unigram:
c=`wc -l < ../mi/unigram_model.txt`
d=`wc -l < ../mi/bigram_model.txt`
e=`head -1 fv_345678.txt | wc -w`
let o=$c+$d+$e

python construct_unigram.py lower_context_tok.txt $o > fv_svm_1_unigram.txt
	
a=`wc -l < unigram_model.txt`
let p=$a+$o

python construct_bigram.py lower_context_tok.txt $p > fv_svm_2_bigram.txt

paste count_capital.txt count_emoticon_class.txt fv_pos_count.txt fv_punct_and_elog.txt fv_score_unigram.txt fv_score_bigram.txt -d " " > fv_345678.txt

b=`wc -l < bigram_model.txt`
let c=$p+$b

python merge_3to9.py  fv_345678.txt $c  > fv_svm_3to8.txt


