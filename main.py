import json, pandas as pd
from Bio import Entrez
from src.analyze import analyse_sequences, summarize
from src.fetch import fetch_sequences
from src.visualize import plot_aromaticity, plot_gravy, plot_instability_index, plot_protein_length, plot_correlation_matrix, plot_amino_acid_heatmap

with open('./data/gene_panel.json','r') as data_file:
    data=json.load(data_file)

Entrez.email='ruchirajoshi06@gmail.com'
    
d_protein_sequences=fetch_sequences(data['disease'])
c_protein_sequences=fetch_sequences(data['control'])

protein_details = analyse_sequences(d_protein_sequences, 'disease') | analyse_sequences(c_protein_sequences, 'control')

df = pd.DataFrame.from_dict(protein_details, orient="index")
df.index.name = "gene"
df = df.reset_index()
df.to_csv('./results/tables/protein_details.csv')

plot_aromaticity(df)
plot_gravy(df) 
plot_instability_index(df) 
plot_protein_length(df)
plot_correlation_matrix(df)
plot_amino_acid_heatmap(df)

summary_stats=summarize(df)
summary_stats.to_csv("./results/tables/summary_stats.csv")