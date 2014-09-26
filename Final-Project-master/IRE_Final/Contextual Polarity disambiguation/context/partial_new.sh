

#Running individual features for both the marked instance and context

#8. constructing unigram:
o=114113

python construct_unigram.py lower_context_tok.txt $o > fv_svm_1_unigram.txt
	
a=`wc -l < unigram_model.txt`
let p=$a+$o

python construct_bigram.py lower_context_tok.txt $p > fv_svm_2_bigram.txt

paste count_capital.txt count_emoticon_class.txt fv_pos_count.txt fv_punct_and_elog.txt fv_score_unigram.txt fv_score_bigram.txt -d " " > fv_345678.txt

b=`wc -l < bigram_model.txt`
let c=$p+$b

python merge_3to9.py  fv_345678.txt $c  > fv_svm_3to8.txt


