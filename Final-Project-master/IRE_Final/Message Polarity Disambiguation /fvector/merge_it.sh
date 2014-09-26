
paste fv_unigram.txt fv_bigram.txt -d " " > m1.txt
paste m1.txt fv_pos_capital.txt -d " " > m2.txt
paste numericalSentiments.txt m2.txt -d " " > final.txt

head -500 final.txt > testing.txt
tail -7722 final.txt > training.txt

rm m1.txt
rm m2.txt
