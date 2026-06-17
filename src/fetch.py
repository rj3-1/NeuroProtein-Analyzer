from Bio import Entrez, SeqIO
import json

Entrez.email='ruchirajoshi06@gmail.com'

with open('../data/gene_panel.json','r') as data_file:
    data=json.load(data_file)

summary=[SeqIO.read(Entrez.efetch(db="protein", id=value, rettype="fasta", retmode="text"),'fasta') for (key,value) in data['disease'].items()]

for ((key,value),item) in zip(data['disease'].items(),summary):
    print(f'{key}    {item.description}')