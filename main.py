import json
from Bio import Entrez
from src.analyze import analyse_sequences, save_protein_details
from src.fetch import fetch_sequences

with open('./data/gene_panel.json','r') as data_file:
    data=json.load(data_file)

Entrez.email='ruchirajoshi06@gmail.com'
    
d_protein_sequences=fetch_sequences(data['disease'])
c_protein_sequences=fetch_sequences(data['control'])

protein_details = analyse_sequences(d_protein_sequences, 'disease') | analyse_sequences(c_protein_sequences, 'control')

save_protein_details(protein_details,'./results/tables/protein_details.csv')    