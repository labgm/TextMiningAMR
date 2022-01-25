import csv
import pandas as pd
import numpy as np

#Datasets labels
doc2vec = pd.read_csv('results/3_dataset_doc2vec_label.csv')
TfIdf= pd.read_csv('results/4_dataset_tfidf_label.csv')

x=[]
x_index=[]
class_doc2vec_mean=[]

y=[]
y_index=[]
class_TfIdf_mean=[]

result=[]

with open('data_source/samples.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader) 
    for i in csv_reader:
      id_0 = i[0].replace('<id>', '')
      id = id_0.replace('</id>', '')
      for indice, f in enumerate(doc2vec['PMCID']):
        f_0 = f.replace('[', '')
        x__ = f_0.replace(']', '')
        output=eval(x__)
        if id == output:
          x.append(output)
          x_index.append(indice)
          class_doc2vec_mean.append(doc2vec['Class_mean'][indice])
      
      for indice_, f_ in enumerate(TfIdf['PMCID']):
        f_1 = f_.replace('[', '')
        y__ = f_1.replace(']', '')
        output2=eval(y__)
        if id == output2:
          y.append(output2)
          y_index.append(indice_)
          class_TfIdf_mean.append(TfIdf['Class_mean'][indice_])

"""**1.1) Experiments A (Doc2Vec_Mean) and B (TF-IDF_Mean) **"""
df_experiments = pd.DataFrame([x, x_index,class_doc2vec_mean, y, y_index, class_TfIdf_mean])
df_experiments.columns = list(range(1, 101, 1))

"""**1.2) Expert Answers**"""
option=[]
with open('data_source/specialists.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';') 
    for i in csv_reader:
      option.append(i)

df_specialists = pd.DataFrame(option)
df_specialists = df_specialists.replace({'Irrelevante': 'Irrelevant'})
df_specialists = df_specialists.replace({'Relevante': 'Relevant'})
df_specialists= df_specialists.iloc[:, 1:101]
df_specialists.index = ['E1', 'E2', 'E3']

#Concatenate Dataframes and transposed
result = pd.concat([df_experiments, df_specialists])
df_concat = result.T

#Validations
df_final = pd.DataFrame()
df_final['PMCID'] = df_concat[0]
df_final['E1'] = df_concat['E1']
df_final['E2'] = df_concat['E2']
df_final['E3'] = df_concat['E3']
df_final['E'] = np.where((df_concat['E1'] == df_concat['E2']) & (df_concat['E1'] == df_concat['E3']), 1, 0) #Consensus = 1, NoConsensus=0
df_final['A.Doc2Vec_Mean'] = df_concat[2]
df_final['E x A'] = np.where((df_concat['E1'] == df_concat['E2']) & (df_concat['E1'] == df_concat['E3']) & (df_concat['E1'] == df_concat[2]), 1, 0) 
df_final['B.TF-IDF_Mean'] = df_concat[7]
df_final['E x B'] = np.where((df_concat['E1'] == df_concat['E2']) & (df_concat['E1'] == df_concat['E3']) & (df_concat['E1'] == df_concat[7]), 1, 0)

# Get names of indexes for which column Stock has value No
indexNames = df_final[ df_final['E'] == 0 ].index
# Delete these row indexes from dataFrame
df_final.drop(indexNames , inplace=True)
sums = df_final.select_dtypes(pd.np.number).sum().rename('total')
df_final = df_final.append(sums)
df_final.to_csv('results/5_Experiments_vs_Specialists.csv', index=False, encoding='utf-8', header=False, sep=',')
df_final