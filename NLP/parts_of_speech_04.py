import nltk
from nltk import pos_tag
from nltk import word_tokenize
nltk.download('averaged_perceptron_tagger_eng')

sample_word = "All good moving forward with courage"
tokenized_sentence = word_tokenize(sample_word)
print(pos_tag(tokenized_sentence))