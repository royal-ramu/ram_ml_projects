from nltk.stem import PorterStemmer
porter = PorterStemmer()
print(porter.stem("I am achieving great heights"))
print(porter.stem("play"))
print(porter.stem("playing"))
print(porter.stem("played"))
print(porter.stem("communication"))
print(porter.stem("information"))
