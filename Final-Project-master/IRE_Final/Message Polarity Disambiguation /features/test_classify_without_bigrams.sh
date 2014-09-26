
#paste testing_labels.txt fv_svm_1_unigram.txt fv_svm_2_bigram.txt fv_svm_3_trigram.txt fv_svm_3to9.txt fv_svm_10.txt -d " " > final_fv_test.txt #for merging the features

paste testing_labels.txt fv_svm_1_unigram.txt fv_svm_3to9.txt fv_svm_10.txt -d " " > final_fv_test.txt #for merging the features

svm-predict final_fv_test.txt final_fv_train.txt.model output
