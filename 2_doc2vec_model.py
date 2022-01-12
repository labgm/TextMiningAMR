import csv
import re
import sys
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
import nltk
from unicodedata import normalize

nltk.download('punkt')
nltk.download('stopwords')
stopwordsnltk = nltk.corpus.stopwords.words('english')

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def removestopwords(text):
    phrases = []
    for word in text:
        clean_word = remover_acentos(word)
        clean_word_http = re.sub(r"http\S+", "", clean_word)
        clean_word_end = re.sub(r'[./?!,":;()\']',' ',clean_word_http)

        for p in clean_word_end.split():
            if p not in stopwordsnltk:
             semstop=p
             phrases.append(semstop)
    return phrases

maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

with open('1_initial_dataset.csv') as csv_file:
    id = []
    title =[]
    abstract = []
    text = []

    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    for row in csv_reader:
      id.append(row[0]) 
      text.append(row[1])

tagged_data = [TaggedDocument(words=removestopwords(word_tokenize(_d.lower())), tags=[str(i)]) for (i, _d) in zip(id,text)]

#model parameters
max_epochs = 30
vec_size = 300
alpha = 0.025
nthreads=18
min_count=3
model = Doc2Vec(vector_size=vec_size,
                alpha=alpha,
                min_alpha=0.00025,
                workers=nthreads,
                min_count=min_count,
                dm =1)

model.build_vocab(tagged_data)

for epoch in range(max_epochs):
    print('iteration {0}'.format(epoch))
    model.train(tagged_data,
                total_examples=model.corpus_count,
                epochs=model.epochs)
    # decrease the learning rate
    model.alpha -= 0.0002
    # fix the learning rate, no decay
    model.min_alpha = model.alpha

model.save("d2v_model.model")
print("Model Saved")
