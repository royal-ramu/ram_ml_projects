import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("playing","v"))
print(lemmatizer.lemmatize("play","v"))
print(lemmatizer.lemmatize("Communication","v"))
print(lemmatizer.lemmatize("running","v"))
print(lemmatizer.lemmatize("cats","n"))
print(lemmatizer.lemmatize("better","a"))
print(lemmatizer.lemmatize("information","a"))