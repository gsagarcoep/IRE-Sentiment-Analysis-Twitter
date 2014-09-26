tail -21673 label.txt > label_training.txt

paste label_training.txt ../mi/fv_svm_1_unigram.txt ../mi/fv_svm_2_bigram.txt ../mi/fv_svm_3to8.txt fv_svm_1_unigram.txt fv_svm_2_bigram.txt fv_svm_3to8.txt -d " " > final.txt



svm-train -t 0 final.txt


