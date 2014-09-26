
head -10000 label.txt > label_test.txt
paste label_test.txt ../mi/fv_svm_1_unigram.txt ../mi/fv_svm_2_bigram.txt ../mi/fv_svm_3to8.txt fv_svm_1_unigram.txt fv_svm_2_bigram.txt fv_svm_3to8.txt -d " "> final_train.txt


svm-predict final_train.txt final.txt.model output

