from Bio import Entrez, SeqIO

def fetch_sequences(data):
    protein_sequences = {}
    for gene, accession in data.items():
        handle = Entrez.efetch(db="protein", id=accession, rettype="fasta", retmode="text")
        protein_sequences[gene] = str(SeqIO.read(handle, "fasta").seq)
        handle.close()
    return protein_sequences