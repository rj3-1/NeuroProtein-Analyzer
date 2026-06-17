from Bio import Entrez, SeqIO
import json
from pathlib import Path

Entrez.email='ruchirajoshi06@gmail.com'

data_path = Path(__file__).resolve().parent.parent / "data" / "gene_panel.json"

with open(data_path,'r') as data_file:
    data=json.load(data_file)

summary=[SeqIO.read(Entrez.efetch(db="protein", id=value, rettype="fasta", retmode="text"),'fasta') for (key,value) in data['disease'].items()]

protein_sequences = {key:str(item.seq) for (key, value), item in zip(data['disease'].items(), summary)}
