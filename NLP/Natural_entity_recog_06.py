import spacy
spacy.cli.download("en_core_web_sm")
nlp = spacy.load("en_core_web_sm")
sentence="Apple Inc. CEO is Steve Jobs running the company from the year 1982"
result = nlp(sentence)
for data in result.ents:
    print(f"{data.text}:{data.label_}")