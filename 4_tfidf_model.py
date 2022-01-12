import csv
import numpy as np
import pandas as pd
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import sys

maxInt = sys.maxsize
#uuuu
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
    text_ = []

    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      id.append(row[0])
      text_.append(row[1])


with open('1_card_ontology.csv') as csv_file:
    my_vocabulary = []
    termos = []
    termos2 = []
    
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      terms.append(row[0].split())

for term in terms:
 terms2.extend (term)

for i in terms2 :
  if i not in my_vocabulary:
    my_vocabulary.append(i)

"""### **2) Model TF-IDF (Text)**"""

#STEP 1 - Obtain the vector representation TF-IDF and AMR vocabulary
# list of words that should be disregarded
ignored_words = ['abstract', 'introduction', 'Genomics', 'keywords', 'conclusions', 'references', 'review', 'author', 'table', 'discussion', 'funding', 'page', 'vol', 'article', 'et', 'al', 'years', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'jan','feb','mar','apr','may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'http']
my_stop_words = text.ENGLISH_STOP_WORDS.union(ignored_words)
cv = CountVectorizer(vocabulary=my_vocabulary, ngram_range=(1, 1)) #com my_vocabulary AMR
# this steps generates word counts for the words in your docs
word_count_vector=cv.fit_transform(text_) # Matrix with all documents (rows) x Unique words in the document (columns)

# Initialize a vectorizer
vectorizer = TfidfVectorizer(use_idf=True, vocabulary=my_vocabulary, stop_words=my_stop_words)
X = vectorizer.fit_transform(text_)#training with vocabulary card

weights_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())
weights_df['Ranking'] = weights_df.mean(axis=1) # Average of word weights in doc (line)
mean = weights_df["Ranking"].mean()  # Average Ranking Column
weights_df['Class_mean'] = np.where(weights_df['Ranking']>=mean, 'Relevant', 'Irrelevant') #If greater than average Relevant, if not Irrelevant
weights_df['PMCID'] = id

#Order the grid columns (PCMID and Ranking will be the first displayed)
cols = weights_df.columns.tolist()
cols = cols[-1::-1]
weights_df = weights_df[cols]

df_ordenado = weights_df.sort_values(by='Ranking', ascending=False)
df = pd.DataFrame(df_ordenado, columns=['PMCID', 'Class_mean'])
df.to_csv('4_dataset_tfidf_label.csv')