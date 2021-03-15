PRODIGY 1.8.5   
PYTHON 3.7.9
SPACY 2.3.2

Overview: 
Exploratory research for custom named entity recognition (NER) to extract methods from model data catalog abstracts and/or summaries using SpaCy Prodigy.

Run the following prodigy commands to test the models on model data catalog abstracts or arxiv machine learning article abstracts. 

MODEL 1: method_model
Prodigy ner.print-stream method_model test20.jsonl  --label METHOD

MODEL 2: geo_model
Prodigy ner.print-stream geo_model test20.jsonl  --label METHOD

MODEL 3: geo3_model
Prodigy ner.print-stream geo3_model test20.jsonl  --label GEO

MODEL 4: ml_model
Prodigy ner.print-stream ml_model test20.jsonl  --label ML
Prodigy ner.print-stream ml_model arxiv_test_small.jsonl  --label ML

MODEL 5: geo6_model
Prodigy ner.print-stream geo6_model test20.jsonl  --label GEO

MODEL 6: geo7_model
Prodigy ner.print-stream geo7_model test20.jsonl  --label GEO

MODEL 7: algo_model2
Prodigy ner.print-stream algo_model2 test20.jsonl  --label ALGO
Prodigy ner.print-stream algo_model2 arxiv_test.jsonl  --label ALGO

MODEL 8: algo_model3
Prodigy ner.print-stream algo_model3 test20.jsonl  --label ALGO
Prodigy ner.print-stream algo_model3 arxiv_test_small.jsonl  --label ALGO

MODEL 9: algo_model4
Prodigy ner.print-stream algo_model4 test20.jsonl  --label ALGO
Prodigy ner.print-stream algo_model4 arxiv_test_small.jsonl  --label ALGO
 
MODEL 10: algo_model5
Prodigy ner.print-stream algo_model5 arxiv_test_small.jsonl  --label ALGO
Prodigy ner.print-stream algo_model5 test20.jsonl  --label ALGO

