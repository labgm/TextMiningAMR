# Text Mining for Identification of Biological Entities Related to Antibiotic Resistant Organisms

Antimicrobial resistance is a significant public health problem worldwide. In recent years, the scientific community has been intensifying efforts to address this problem; many experiments have been developed, which generated many articles are being published in this area. However, the growing volume of biological literature makes researchers and biocurators increasingly difficult due to the cost and time required. As a result, modern text mining tools with the adoption of artificial intelligence technology have been increasingly required to assist in the evolution of research. Thus, we propose a text mining model capable of identifying and prioritizing scientific articles in the context of antimicrobial resistance. We retrieved scientific articles from the PubMed Central database, adopted machine learning techniques to generate the vector representation of the retrieved scientific articles, and identified their similarity with the context. As a result of this process, we obtained a dataset labeled "Relevant" and "Irrelevant". We used this dataset to implement two supervised learning algorithms to classify new records. The model's overall performance reached 90% accuracy. The f-measure (harmonic mean between the metrics) reached 82% accuracy for class positive, showing quality in identifying scientific articles relevant to the context.

# Overview

![alt text](https://github.com/engbiopct/TextMiningAMR/blob/main/figure/Figure%201.png?raw=true) Figure 1. Proposed TM model. 

</br>Figure 1 shows the TM steps implemented in this work in order to label the data. 
We retrieved a collection of relevant articles in the Drug Resistance and Microbial domain from the Pubmed Central (PMC) database of the National Library of Medicine and the US National Institutes of Health (NIH/NLM).
We used the MeSH hierarchy terms for antimicrobial resistance (https://meshb.nlm.nih.gov/record/ui?ui=D004352) and obtained a list of PMCIDs (unique identifiers provided by PubMed Central to each document) with which we will access the full texts of the articles through the E-Fetch utility.

We used the Doc2Vec unsupervised learning algorithm from the Gensim library, which implements the Paragraph Vector – Distributed Memory model, to obtain the embedding of the retrieved documents (Figure 1-C). With the pre-trained model, we inferred the similarity of the documents to the AMR context, represented by 4,290 terms extracted from CARD and the Gene Ontology Database (Figure 1-D), and automatically labeled each of the scientific articles (Figure 1-E) as relevant or irrelevant.

# Results
Table 3. Results of Labeling and Classification vs Experts steps

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none'>
 <tr style='height:14.2pt'>
  <td width=267 valign=top style='width:200.05pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormalCxSpFirst style='text-align:justify;line-height:normal'><b><span
  lang=EN-US style='font-size:12.0pt;font-family:"Times New Roman","serif"'>&nbsp;</span></b></p>
  </td>
  <td width=172 valign=top style='width:128.65pt;border:solid black 1.0pt;
  border-left:none;background:#F2F2F2;padding:0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormalCxSpMiddle align=center style='text-align:center;
  line-height:normal'><b><span lang=EN-US style='font-size:12.0pt;font-family:
  "Times New Roman","serif"'>Relevant</span></b></p>
  </td>
  <td width=184 valign=top style='width:138.15pt;border:solid black 1.0pt;
  border-left:none;background:#F2F2F2;padding:0cm 5.4pt 0cm 5.4pt;height:14.2pt'>
  <p class=MsoNormalCxSpMiddle align=center style='text-align:center;
  line-height:normal'><b><span lang=EN-US style='font-size:12.0pt;font-family:
  "Times New Roman","serif"'>Irrelevant</span></b></p>
  </td>
 </tr>
 <tr style='height:16.0pt'>
  <td width=267 valign=top style='width:200.05pt;border:solid black 1.0pt;
  border-top:none;background:#F2F2F2;padding:0cm 5.4pt 0cm 5.4pt;height:16.0pt'>
  <p class=MsoNormalCxSpMiddle style='text-align:justify;line-height:115%'><b><span
  lang=EN-US style='font-size:12.0pt;line-height:115%;font-family:"Times New Roman","serif"'>Labeling</span></b></p>
  </td>
  <td width=172 valign=top style='width:128.65pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:#F2F2F2;padding:0cm 5.4pt 0cm 5.4pt;height:16.0pt'>
  <p class=MsoNormalCxSpMiddle align=center style='text-align:center;
  line-height:115%'><b><span lang=EN-US style='font-size:12.0pt;line-height:
  115%;font-family:"Times New Roman","serif"'>&nbsp;</span></b></p>
  </td>
  <td width=184 valign=top style='width:138.15pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  background:#F2F2F2;padding:0cm 5.4pt 0cm 5.4pt;height:16.0pt'>
  <p class=MsoNormalCxSpMiddle align=center style='text-align:center;
  line-height:normal'><b><span lang=EN-US style='font-size:12.0pt;font-family:
  "Times New Roman","serif"'>&nbsp;</span></b></p>
  </td>
 </tr>
 <tr style='height:16.65pt'>
  <td width=267 valign=top style='width:200.05pt;border:solid black 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:16.65pt'>
  <p class=MsoNormalCxSpMiddle style='text-align:justify;line-height:115%'><span
  lang=EN-US style='font-size:12.0pt;line-height:115%;font-family:"Times New Roman","serif"'>Dataset_1</span></p>
  </td>
  <td width=172 valign=top style='width:128.65pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.65pt'>
  <p class=MsoNormalCxSpMiddle align=center style='text-align:center;
  line-height:115%'><span lang=EN-US style='font-size:12.0pt;line-height:115%;
  font-family:"Times New Roman","serif"'>80%</span></p>
  </td>
  <td width=184 valign=top style='width:138.15pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.65pt'>
  <p class=MsoNormalCxSpMiddle align=center style='text-align:center;
  line-height:normal'><span lang=EN-US style='font-size:12.0pt;font-family:
  "Times New Roman","serif"'>68%</span></p>
  </td>
 </tr>
 <tr style='height:16.0pt'>
  <td width=267 valign=top style='width:200.05pt;border:solid black 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:16.0pt'>
  <p class=MsoNormalCxSpMiddle style='text-align:justify;line-height:115%'><span
  lang=EN-US style='font-size:12.0pt;line-height:115%;font-family:"Times New Roman","serif"'>Dataset_2</span></p>
  </td>
  <td width=172 valign=top style='width:128.65pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.0pt'>
  <p class=MsoNormalCxSpMiddle align=center style='text-align:center;
  line-height:115%'><span lang=EN-US style='font-size:12.0pt;line-height:115%;
  font-family:"Times New Roman","serif"'>66%</span></p>
  </td>
  <td width=184 valign=top style='width:138.15pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.0pt'>
  <p class=MsoNormalCxSpMiddle align=center style='text-align:center;
  line-height:normal'><span lang=EN-US style='font-size:12.0pt;font-family:
  "Times New Roman","serif"'>34%</span></p>
  </td>
 </tr>
 <tr style='height:16.0pt'>
  <td width=267 valign=top style='width:200.05pt;border-top:none;border-left:
  solid black 1.0pt;border-bottom:solid windowtext 1.0pt;border-right:solid black 1.0pt;
  background:#F2F2F2;padding:0cm 5.4pt 0cm 5.4pt;height:16.0pt'>
  <p class=MsoNormalCxSpMiddle style='text-align:justify;line-height:115%'><b><span
  lang=EN-US style='font-size:12.0pt;line-height:115%;font-family:"Times New Roman","serif"'>Classification</span></b></p>
  </td>
  <td width=172 valign=top style='width:128.65pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid black 1.0pt;
  background:#F2F2F2;padding:0cm 5.4pt 0cm 5.4pt;height:16.0pt'>
  <p class=MsoNormalCxSpMiddle align=center style='text-align:center;
  line-height:115%'><b><span lang=EN-US style='font-size:12.0pt;line-height:
  115%;font-family:"Times New Roman","serif"'>&nbsp;</span></b></p>
  </td>
  <td width=184 valign=top style='width:138.15pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid black 1.0pt;
  background:#F2F2F2;padding:0cm 5.4pt 0cm 5.4pt;height:16.0pt'>
  <p class=MsoNormalCxSpMiddle align=center style='text-align:center;
  line-height:normal'><b><span lang=EN-US style='font-size:12.0pt;font-family:
  "Times New Roman","serif"'>&nbsp;</span></b></p>
  </td>
 </tr>
 <tr style='height:17.2pt'>
  <td width=267 valign=top style='width:200.05pt;border:solid black 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:17.2pt'>
  <p class=MsoNormalCxSpMiddle style='text-align:justify;line-height:115%'><span
  lang=EN-US style='font-size:12.0pt;line-height:115%;font-family:"Times New Roman","serif"'>SVM_1</span></p>
  </td>
  <td width=172 valign=top style='width:128.65pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:17.2pt'>
  <p class=MsoNormalCxSpMiddle align=center style='text-align:center;
  line-height:115%'><b><span lang=EN-US style='font-size:12.0pt;line-height:
  115%;font-family:"Times New Roman","serif"'>93%</span></b></p>
  </td>
  <td width=184 valign=top style='width:138.15pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:17.2pt'>
  <p class=MsoNormalCxSpMiddle align=center style='text-align:center;
  line-height:normal'><b><span lang=EN-US style='font-size:12.0pt;font-family:
  "Times New Roman","serif"'>89%</span></b></p>
  </td>
 </tr>
 <tr style='height:16.0pt'>
  <td width=267 valign=top style='width:200.05pt;border:solid black 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:16.0pt'>
  <p class=MsoNormalCxSpMiddle style='text-align:justify;line-height:115%'><span
  lang=EN-US style='font-size:12.0pt;line-height:115%;font-family:"Times New Roman","serif"'>SVM_2</span></p>
  </td>
  <td width=172 valign=top style='width:128.65pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.0pt'>
  <p class=MsoNormalCxSpMiddle align=center style='text-align:center;
  line-height:115%'><span lang=EN-US style='font-size:12.0pt;line-height:115%;
  font-family:"Times New Roman","serif";color:red'>60%</span></p>
  </td>
  <td width=184 valign=top style='width:138.15pt;border-top:none;border-left:
  none;border-bottom:solid black 1.0pt;border-right:solid black 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:16.0pt'>
  <p class=MsoNormalCxSpMiddle align=center style='text-align:center;
  line-height:normal'><span lang=EN-US style='font-size:12.0pt;font-family:
  "Times New Roman","serif";color:red'>29%</span></p>
  </td>
 </tr>
</table>

Table 3 presents the percentage of correct predictions, both in the labeling and in the classification stage, in comparison with the data labeled by experts and validates the hypothesis that the use of Paragraph Vector, Distributed Representations of Sentences, and Documents associated with similarity with a specific context is able not only to perform the binary classification of large volumes of data satisfactorily but also to optimize the percentage of correct answers when submitted to supervised classifiers.


# Complementary Materials

[Table S1 - Initial Dataset](https://github.com/kellecosta/model_amr/blob/main/1_initial_dataset.rar)

[Table S2 - CARD and the Gene Ontology Database](https://github.com/kellecosta/model_amr/blob/main/teste.csv)

[Table S3 - Dataset Doc2vec Label](https://github.com/engbiopct/TextMiningAMR/blob/main/scripts/results/3_dataset_doc2vec_label.csv)

[Table S4 - Dataset TF-IDF Label](https://github.com/engbiopct/TextMiningAMR/blob/main/scripts/results/4_dataset_tfidf_label.csv)

[Table S5 - Experiments vs Specialists](https://github.com/engbiopct/TextMiningAMR/blob/main/scripts/results/5_experiments_vs_specialists.csv)

# Document Embedding (AMR Context)
[Document Embedding 1](https://github.com/kellecosta/model_amr/blob/main/1_document_embedding.rar)

[Document Embedding 2](https://github.com/kellecosta/model_amr/blob/main/2_document_embedding.rar)

[Document Embedding 3_part1](https://github.com/kellecosta/model_amr/blob/main/3_document_embedding.part1.rar)

[Document Embedding 3_part2](https://github.com/kellecosta/model_amr/blob/main/3_document_embedding.part2.rar)

[Document Embedding 3_part3](https://github.com/kellecosta/model_amr/blob/main/3_document_embedding.part3.rar)

[Document Embedding 3_part4](https://github.com/kellecosta/model_amr/blob/main/3_document_embedding.part4.rar)

[Document Embedding 4_part1](https://github.com/kellecosta/model_amr/blob/main/4_document_embedding.part1.rar)

[Document Embedding 4_part2](https://github.com/kellecosta/model_amr/blob/main/4_document_embedding.part2.rar)

[Document Embedding 4_part3](https://github.com/kellecosta/model_amr/blob/main/4_document_embedding.part3.rar)

[Document Embedding 4_part4](https://github.com/kellecosta/model_amr/blob/main/4_document_embedding.part4.rar)

* ATTENTION:

 *1. Download the template files (Document Embedding) in the "results" directory

 *2. Select all zipped files and use the unzip option here, this will merge the files that needed to be split into files of up to 1 GB to be uploaded to github. 

# Figures and Tables

[Figures](https://github.com/engbiopct/TextMiningAMR/tree/main/figure)

[Tables](https://github.com/engbiopct/TextMiningAMR/tree/main/table)
