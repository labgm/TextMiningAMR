# Text Mining for Identification of Biological Entities Related to Antibiotic Resistant Organisms

Antimicrobial resistance is an important public health problem worldwide. In recent years, the scientific community has been intensifying efforts to combat this problem; many experiments have been developed and a large number of articles are being published in this area. However, the growing volume of biological literature makes the work of researchers and biocurators increasingly difficult due to the cost and time required. As result, modern text mining tools with the adoption of artificial intelligence technology have been increasingly required to assist in the evolution of research. Thus, in this article we propose a text mining model capable of identifying and prioritizing scientific articles in the context of antimicrobial resistance. For this, we retrieved scientific articles from the PubMed Central database, adopted machine learning techniques to generate the vector representation of the retrieved scientific articles and identify their similarity with the context. As result of this process, we obtained a dataset labeled with the classes "Relevant" and “Irrelevant” and use this dataset to implement two supervised learning algorithms to classify new records. The overall performance of the model reached 90% accuracy and f-measure (harmonic mean between the metrics) reached 82% accuracy for class positive, showing quality in the identification of scientific articles relevant to the context.

#Overview

![alt text](https://github.com/engbiopct/TextMiningAMR/blob/main/figure/Figure%201.png?raw=true)
</br>A Figura 1 mostra as etapas da MT implementadas neste trabalho. 

Recuperamos uma coleção de artigos relevantes no domínio Drug Resistance, Microbial, do banco de dados Pubmed Central (PMC), onde são disponibilizados arquivos de texto completo e gratuitos da literatura biomédica da Biblioteca Nacional de Medicina e do Instituto Nacional de Saúde dos EUA (NIH / NLM). 
Utilizamos os termos da hierarquia MeSH para resistência antimicrobiana (https://meshb.nlm.nih.gov/record/ui?ui=D004352) e obtivemos uma lista de PMCIDs (identificadores únicos fornecidos pelo PubMed Central a cada documento) com os quais acessaremos os textos completos dos artigos através do utilitário E-Fetch. 

Utilizamos o algoritmo de aprendizagem não supervisionada Doc2Vec da biblioteca Gensim, que implementa o modelo Paragraph Vector – Distributed Memory, para obter o embedding dos documentos recuperados (Figure 1-C). Com o modelo pré-treinado, inferimos a similaridade dos documentos ao contexto AMR, representado por 4.290 termos extraídos do CARD e do Gene Ontology Database (Figure 1-D) e rotulamos automaticamente cada um dos artigos científicos (Figure 1-E) como relevantes ou irrelevantes.

# Results
Table 3. Resultados das etapas de Rotulação e Classificação vs Especialistas

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
  lang=EN-US style='font-size:12.0pt;line-height:115%;font-family:"Times New Roman","serif"'>Rotulação</span></b></p>
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
  lang=EN-US style='font-size:12.0pt;line-height:115%;font-family:"Times New Roman","serif"'>Classificação</span></b></p>
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

A Table 3 apresenta o percentual de acertos das predições, tanto na etapa de rotulação quanto na etapa de classificação, em comparação com os dados rotulados por especialistas e valida a hipótese de que o uso de Paragraph Vector, Distributed Representations of Sentences and Documents associados a similaridade com um contexto específico é capaz de, não somente, realizar a classificação binária de grandes volumes de dados, como também otimizar o percentual de acertos de classificadores supervisionados. Já o classificador SVM_2 apresentou uma redução no número de acertos em relação a etapa de Rotulação, embora tenhamos adotado em ambos os experimentos o mesmo vetor de atributos e a mesma representação (bag of words, ponderada com TF-IDF).


# Materiais Suplementares

[Table S1 - Initial Dataset](https://github.com/kellecosta/model_amr/blob/main/teste.csv)

[Table S2 - CARD and the Gene Ontology Database](https://github.com/kellecosta/model_amr/blob/main/teste.csv)

[Table S3 - Dataset Doc2vec Label](https://github.com/engbiopct/TextMiningAMR/blob/main/scripts/results/3_dataset_doc2vec_label.csv)

[Table S4 - Dataset TF-IDF Label](https://github.com/engbiopct/TextMiningAMR/blob/main/scripts/results/4_dataset_tfidf_label.csv)

[Table S5 - 4_Experiments_vs_Specialists.csv](https://github.com/kellecosta/model_amr/blob/main/teste.csv)

# Document Embedding (AMR Context)
[Document Embedding]

# Figures and Tables

[Figures](https://github.com/engbiopct/TextMiningAMR/tree/main/figure)

[Tables](https://github.com/engbiopct/TextMiningAMR/tree/main/table)
