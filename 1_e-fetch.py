import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import csv
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

id=[]
content=[]
result=[]

def removeTags(html):
    content = re.sub('[]\n<[^<]+?>', ' ', html)
    content = content.replace('\n', ' ')
    return content

with open('0_ids.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')  
  for id in csv_reader:
    r = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id='+str(id[0])+'&rettype=null&retmode=xml&api_key=a7bdae995dd4d02666337883898afd4f0208')
    content = BeautifulSoup(r.content,'html.parser').get_text()
    content = removeTags(content)
    result.append([id, content])
    df = pd.DataFrame(result) 
    df.to_csv('1.1_Dataset_MeSH.csv', mode='a', index=False, encoding='utf-8', header=False, sep=',')
