from Bio import Entrez

input_gene=''
Entrez.esearch(db='taxonomy', term=input_gene)
