from Bio.SeqUtils.ProtParam import ProteinAnalysis
from fetch import protein_sequences
import pandas as pd

protein_details = {}

for gene, sequence in protein_sequences.items():
    analysis = ProteinAnalysis(sequence)
    secondary_structure = analysis.secondary_structure_fraction()
    amino_acid_counts = analysis.count_amino_acids()
    protein_details[gene] = {
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
    
df = pd.DataFrame.from_dict(protein_details, orient="index")