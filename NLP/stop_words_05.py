import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')

sample_setence="All is well when you keep learning every day.Growth comes when you challenge yourself beyond comfort.Move forward with courage, even when things feel uncertain.Success follows those who stay consistent and never give up."
tokenized_text=list(map(str.lower,word_tokenize(sample_setence)))
stop_words = set(stopwords.words('english'))
print([word for word in tokenized_text if word not in stop_words])