
#paste training_labels.txt fv_svm_1_unigram.txt fv_svm_2_bigram.txt fv_svm_3_trigram.txt fv_svm_3to9.txt fv_svm_10.txt -d " " > final_fv_train.txt #for merging the features

paste training_labels.txt fv_svm_1_unigram.txt fv_svm_3to9.txt fv_svm_10.txt -d " " > final_fv_train.txt #for merging the features

svm-train -t 0 final_fv_train.txt #for training with svm

