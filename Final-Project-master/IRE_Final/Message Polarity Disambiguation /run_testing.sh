bash preprocess_testing.sh $1

echo 
echo "Making feature vector"
bash build_model_featurefiles_testing.sh

echo 
echo "Running SVM"
echo
cd features/
bash classify_testing.sh
cd ..
python int_to_sent.py features/output
echo
