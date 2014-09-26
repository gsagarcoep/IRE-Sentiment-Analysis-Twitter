cat parsed_tweets.txt > training.txt

cat numericalSentiments.txt > features/training_labels.txt

python get_tokens_or_tags.py training.txt 0 > tokenized_tweet.txt
python get_tokens_or_tags.py training.txt 1 > tags_of_tweet.txt

python normalize_url_username_emoticon.py tokenized_tweet.txt > norm_tok_tweet.txt #step 1, normalize

python add_negation_tw.py norm_tok_tweet.txt > neg_norm_tok.txt # step2, add negation context

python convert_lower_and_count.py neg_norm_tok.txt > final_lnnt.txt # step3, count all CAPS, and convert to lower.





