from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pandas as pd

def analyse_sequences(gene_seq, gene_type):
    protein_details = {}
    for gene, sequence in gene_seq.items():
        analysis = ProteinAnalysis(sequence)
        secondary_structure = analysis.secondary_structure_fraction()
        amino_acid_counts = analysis.count_amino_acids()
        protein_details[gene] = {
            "group": gene_type,
            "protein_length": len(sequence),
            "molecular_weight": analysis.molecular_weight(),
            "isoelectric_point": analysis.isoelectric_point(),
            "aromaticity": analysis.aromaticity(),
            "instability_index": analysis.instability_index(),
            "gravy": analysis.gravy(),
            "alpha_structure_fraction": secondary_structure[0],
            "turn_structure_fraction": secondary_structure[1],
            "beta_structure_fraction": secondary_structure[2],
        } | amino_acid_counts
    
    return protein_details

def save_protein_details(prot_det,output_file):
    df = pd.DataFrame.from_dict(prot_det, orient="index")
    df.index.name = "gene"
    df.to_csv(output_file)