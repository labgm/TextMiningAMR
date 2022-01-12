import csv
import pandas as pd
import numpy as np

doc2vec = pd.read_csv('csv/3_dataset_doc2vec_label.csv')

x=[]
x_index=[]
class_doc2vec_mean=[]
result=[]

with open('csv/samples.csv') as csv_file:
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
         
"""** 1) Test samples labeled by Doc2Vec**"""
df_experiments = pd.DataFrame([x, x_index,class_doc2vec_mean)
df_experiments.columns = list(range(1, 101, 1))

"""** 2) Test samples labeled by experts**"""
option=[]
with open('specialists.csv') as csv_file:

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

"""** 2) expert data consolidation vs Doc2Vec label **"""
df_final = pd.DataFrame()
df_final['PMCID'] = df_concat[0]
df_final['E1'] = df_concat['E1']
df_final['E2'] = df_concat['E2']
df_final['E3'] = df_concat['E3']
df_final['E'] = np.where((df_concat['E1'] == df_concat['E2']) & (df_concat['E1'] == df_concat['E3']), 1, 0) #Consensus = 1, NoConsensus=0

df_final['A1.Doc2Vec_Mean'] = df_concat[2]
df_final['E x A1'] = np.where((df_concat['E1'] == df_concat['E2']) & (df_concat['E1'] == df_concat['E3']) & (df_concat['E1'] == df_concat[2]), 1, 0) 

#excludes lines without expert consensus (reduces the sample from 100 to 62 articles)
indexNames = df_final[ df_final['E'] == 0 ].index
df_final.drop(indexNames , inplace=True)

sums = df_final.select_dtypes(pd.np.number).sum().rename('total')
df_final = df_final.append(sums)
df_final.to_csv('4_Experiments_vs_Specialists.csv', index=False, encoding='utf-8', header=False, sep=',')
df_final
