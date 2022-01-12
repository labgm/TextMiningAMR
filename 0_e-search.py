import requests
from bs4 import BeautifulSoup
import pandas as pd
idList = []

def getListofIDs(query):
    r = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&term="+query+"&retmax=100000")
    
    soup = BeautifulSoup(r.text, 'html.parser')
    idList = soup.find_all('id')
    df = pd.DataFrame(idList) 
    df.to_csv('0_ids.csv', index=False, encoding='utf-8', header=False, sep=',')
    
    return 0
        
s= '("drug resistance, microbial"[MeSH Terms] OR ("drug"[All Fields] AND "resistance"[All Fields] AND "microbial"[All Fields]) OR "microbial drug resistance"[All Fields] OR ("drug"[All Fields] AND "resistance"[All Fields] AND "microbial"[All Fields]) OR "drug resistance, microbial"[All Fields]) AND "open access"[filter]'
getListofIDs(s)