import csv
import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt 
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import seaborn as sns
import joblib
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

Class_train=[]
Class_test=[]
id_train=[]
text_train=[]
Class_mean_train= []
id_test=[]
text_test=[]
Class_mean_test=[]

#1. Dataset test
with open('results/5_experiments_vs_specialists.csv') as csv_file_sample:
  csv_reader_sample = csv.reader(csv_file_sample, delimiter=',')
  for row_sample in csv_reader_sample:
    #id_sample.append(row_sample[0]) # 62 papers lables experts
    Class_test.append([row_sample[0], row_sample[1]]) # PMCID and Class - 62 papers lables experts

#2. Dataset train
with open('results/3_dataset_doc2vec_label.csv') as csv_file_:       
    csv_reader_ = csv.reader(csv_file_, delimiter=',')
    next(csv_reader_)
    for row_ in csv_reader_:
      f_1 = row_[1].replace('[', '')#PCMID
      y__ = f_1.replace(']', '')
      id_clean = eval(y__)
      
      for y in Class_test:
        if id_clean != y[0]: # PMCID ==> x[0]
            Class_train.append([id_clean, row_[2]]) #PCMID and Label 
      
      #if id_clean not in id_sample: #only Train (without Samples Experts)
        #Class_train.append([id_clean, row_[3], row_[5], row_[6]]) #3886 - 62 = 3824
      
      #if id_clean in id_sample: #only Samples Experts
      #  Class_test.append([id_clean, row_[3], row_[5], row_[6]]) #62

#3. Joint Text (Train and Test)
with open('results/1_initial_dataset') as csv_file_dataset:
  csv_reader_dataset = csv.reader(csv_file_dataset, delimiter=',')
  for row_dataset in csv_reader_dataset:
    x_1 = row_dataset[0].replace('[', '')
    z__ = x_1.replace(']', '')
    id_dataset_clean = eval(z__)
    for x in Class_train:
      if id_dataset_clean == x[0]: # PMCID == x[0]
        id_train.append(id_dataset_clean)
        text_train.append(row_dataset[1])
        Class_mean_train.append(x[1])
    
    for y in Class_test:
      if id_dataset_clean == y[0]: # PMCID == x[0]
        id_test.append(id_dataset_clean)
        text_test.append(row_dataset[1])
        Class_mean_test.append(y[1])


"""## **1) Dataset Train (lables by Doc2Vec+mean and without samples test)**"""

df_train = pd.DataFrame()
df_train['PMCID_train'] = id_train
df_train['Paper_train'] = text_train
df_train['Class_meanx_train'] = Class_mean_train
df_train['Class_mean_train'] = np.where(df_train['Class_meanx_train'] == 'Relevant', 0, 1)
#df_train.to_csv('results/6_Dataset_train_svm.csv', index=False, encoding='utf-8', header=False, sep=',')

"""## **2) Dataset Test (62 samples random label by Experts)**"""
df_test = pd.DataFrame()
df_test['PMCID_test'] = id_test
df_test['Paper_test'] = text_test
df_test['Class_meanx_test'] = Class_mean_test
df_test['Class_mean_test'] = np.where(df_test['Class_meanx_test'] == 'Relevant', 0, 1)
#df_test.to_csv('results/6_Dataset_test_svm.csv', index=False, encoding='utf-8', header=False, sep=',')

#CARD vocabulary
with open('data_source/0_card_ontology.csv') as csv_file:
    my_vocabulary = []
    termos = []
    termos2 = []    
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
      termos.append(row[0].split()) 

for termo in termos:
 termos2.extend (termo) 

for i in termos2 :
  if i not in my_vocabulary:
    my_vocabulary.append(i)

cv = CountVectorizer(vocabulary=my_vocabulary, ngram_range=(1, 1))
# this steps generates word counts for the words in your docs
word_count_vector_train=cv.fit_transform(df_train['Paper_train'])
word_count_vector_test=cv.fit_transform(df_test['Paper_test'])

tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)

tfidf_train = tfidf_transformer.fit(word_count_vector_train)
tfidf_test = tfidf_transformer.fit(word_count_vector_test)

# tf-idf scores
tf_idf_vector_train=tfidf_train.transform(word_count_vector_train)
tf_idf_vector_test=tfidf_test.transform(word_count_vector_test)

X_train = tf_idf_vector_train
y_train_mean = df_train['Class_mean_train']

X_test = tf_idf_vector_test
y_test_mean = df_test['Class_mean_test']

param_grid = [
  {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
  {'C': [1, 10, 100, 1000], 'gamma': [0.0001, 0.0005, 0.001, 0.005], 'kernel': ['rbf']},
]

# Create a classifier object with the classifier and parameter candidates
clf = GridSearchCV(estimator=svm.SVC(), param_grid=param_grid, n_jobs=-1)

# Train the classifier on data1's feature and target data and save model mean
clf.fit(X_train, y_train_mean)
joblib.dump(clf, 'results/model_svm_1.pkl') # clf = model trained
result= clf.predict(X_test)

mat = confusion_matrix(y_test_mean, result)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False)
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.savefig('results/confusion_matrix_svm_1.png');

accuracy = metrics.accuracy_score(y_test_mean, result)

file_report = open('results/Results_svm_1.txt', 'w')
file_report.write("Metrics: "+metrics.classification_report(y_test_mean, result))
file_report.write("Accuracy: "+str(accuracy)+"\n")
file_report.write("Confusion matrix:"+"\n"+str(mat)+"\n")
file_report.close()
