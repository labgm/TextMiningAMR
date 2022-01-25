import csv
import re
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sb

import sys
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

text_=[]
# Dictionary
with open('data_source/card_ontology.csv') as csv_file:
    my_vocabulary = []
    terms = []
    terms2 = []
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
      terms.append(row[0].split())

for term in terms:
 terms2.extend(term)
#remove duplicates
for i in terms2 :
  if i not in my_vocabulary:
    my_vocabulary.append(i)

## Load Model
model = Doc2Vec.load("results/d2v_model.model")
#STEP 1 - use infer_vector() to obtain the vector representation of the AMR vocabulary - which does not change the underlying model.
v1 = model.infer_vector(my_vocabulary)
sims = model.docvecs.most_similar([v1], topn=100000)
id_ = [] #Texts Ids
X = [] #Array with similarity values

for i, d in sims:
  id_.append(i)
  X.append([d]) #X receives the value of similarities

X = np.array(X)
df = pd.DataFrame(X) #dataframe results

#STEP 2: MEAN
#Calculates the arithmetic mean of the similarities and Labels the above-average items as Relevant and the below-average items as Irrelevant
mean = X.mean()
df['PMCID'] = id_
df['Class_mean'] = np.where(X>=mean, 'Relevant', 'Irrelevant')

##SAVE
df.to_csv('results/3_dataset_doc2vec_label.csv')
