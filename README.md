# Text Mining for Identification of Biological Entities Related to Antibiotic Resistant Organisms

Antimicrobial resistance is an important public health problem worldwide. In recent years, the scientific community has been intensifying efforts to combat this problem; many experiments have been developed and a large number of articles are being published in this area. However, the growing volume of biological literature makes the work of researchers and biocurators increasingly difficult due to the cost and time required. As result, modern text mining tools with the adoption of artificial intelligence technology have been increasingly required to assist in the evolution of research. Thus, in this article we propose a text mining model capable of identifying and prioritizing scientific articles in the context of antimicrobial resistance. For this, we retrieved scientific articles from the PubMed Central database, adopted machine learning techniques to generate the vector representation of the retrieved scientific articles and identify their similarity with the context. As result of this process, we obtained a dataset labeled with the classes "Relevant" and “Irrelevant” and use this dataset to implement two supervised learning algorithms to classify new records. The overall performance of the model reached 90% accuracy and f-measure (harmonic mean between the metrics) reached 82% accuracy for class positive, showing quality in the identification of scientific articles relevant to the context.

#Overview

![alt text](https://github.com/engbiopct/TextMiningAMR/blob/main/figure/Figure%201.png?raw=true)
</br>A Figura 1 mostra as etapas da MT implementadas neste trabalho. 

 
Figure 1. Modelo de TM proposto. As etapas (A) e (B) incluem a recuperação das informações. As etapas (C) e (D) contemplam o reconhecimento das entidades e a descoberta de conhecimentos, resultando em uma métrica (similaridade cosseno) responsável por determinar a classificação binária realizada na etapa (E).

Results

A Table 3 apresenta o percentual de acertos das predições, tanto na etapa de rotulação quanto na etapa de classificação, em comparação com os dados rotulados por especialistas e valida a hipótese de que o uso de Paragraph Vector, Distributed Representations of Sentences and Documents associados a similaridade com um contexto específico é capaz de, não somente, realizar a classificação binária de grandes volumes de dados, como também otimizar o percentual de acertos de classificadores supervisionados. Já o classificador SVM_2 apresentou uma redução no número de acertos em relação a etapa de Rotulação, embora tenhamos adotado em ambos os experimentos o mesmo vetor de atributos e a mesma representação (bag of words, ponderada com TF-IDF).

# Materiais Suplementares

[Table S1 - Initial Dataset](https://github.com/kellecosta/model_amr/blob/main/teste.csv)
[Table S2 - CARD and the Gene Ontology Database](https://github.com/kellecosta/model_amr/blob/main/teste.csv)  
[Table S3 - Dataset Doc2vec Label](https://github.com/engbiopct/TextMiningAMR/blob/main/scripts/results/3_dataset_doc2vec_label.csv)
[Table S4 - Dataset TF-IDF Label](https://github.com/engbiopct/TextMiningAMR/blob/main/scripts/results/4_dataset_tfidf_label.csv)
[Table S5 - 4_Experiments_vs_Specialists.csv](https://github.com/kellecosta/model_amr/blob/main/teste.csv)

# Document Embedding (AMR Context)
[Document Embedding]
