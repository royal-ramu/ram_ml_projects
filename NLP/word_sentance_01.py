import nltk
from nltk import word_tokenize,sent_tokenize
nltk.download('punkt_tab')

sample_sent="I am achieving great heights. Thank to god for all the good things"
print(word_tokenize(sample_sent))
print(sent_tokenize(sample_sent))