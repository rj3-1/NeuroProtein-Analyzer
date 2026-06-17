# NeuroProtein Analyzer

A bioinformatics pipeline that retrieves protein sequences associated with neurodegenerative diseases from NCBI and compares their sequence-derived physicochemical properties against housekeeping proteins using Biopython.

## Motivation

Protein misfolding and aggregation are hallmarks of many neurodegenerative diseases, including Alzheimer's disease, Parkinson's disease, Huntington's disease, and ALS. This project explores whether proteins implicated in these disorders exhibit distinguishable sequence-level characteristics when compared to housekeeping proteins.

## Research Question

Do proteins associated with neurodegenerative diseases exhibit distinct sequence-derived physicochemical properties compared to housekeeping proteins?

## Protein Panels

### Disease-Associated Proteins

| Gene   | Disease                           |
| ------ | --------------------------------- |
| APP    | Alzheimer's Disease               |
| MAPT   | Alzheimer's Disease / Tauopathies |
| SNCA   | Parkinson's Disease               |
| HTT    | Huntington's Disease              |
| TARDBP | ALS / Frontotemporal Dementia     |

### Control Proteins

| Gene   |
| ------ |
| GAPDH  |
| ACTB   |
| HPRT1  |
| RPLP0  |
| TUBA1B |

## Pipeline

Gene Panel
→ Retrieve Protein Sequences from NCBI
→ Parse Sequences with Biopython
→ Calculate ProtParam Descriptors
→ Analyze Amino Acid Composition
→ Compare Disease and Control Groups
→ Generate Visualizations
→ Export Results

## Features

* Automated protein sequence retrieval using NCBI Entrez
* Sequence parsing with Biopython
* Physicochemical property analysis using ProtParam
* Amino acid composition profiling
* Comparative analysis of disease and control proteins
* CSV export of computed metrics
* Automated visualization generation

## Technologies

* Python
* Biopython
* pandas
* matplotlib

## Outputs

### Protein Properties

* Sequence Length
* Molecular Weight
* Isoelectric Point (pI)
* Aromaticity
* Instability Index
* GRAVY Score

### Amino Acid Analysis

* Amino acid frequencies
* Comparative composition analysis
* Summary visualizations

## Limitations

ProtParam descriptors are sequence-derived physicochemical properties and are not direct measurements of protein aggregation propensity. Results should be interpreted as exploratory analyses rather than mechanistic evidence.

## Repository Structure

```text
src/
├── fetch.py
├── analyze.py
├── compare.py
└── visualize.py

data/
results/

README.md
requirements.txt
```
