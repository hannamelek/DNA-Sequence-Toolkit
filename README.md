# 🧬 DNA Sequence Toolkit

A command-line bioinformatics toolkit written in **Python** for analyzing DNA sequences from FASTA files.

This project performs common molecular biology analyses, including nucleotide composition, GC/AT content calculation, reverse complement generation, RNA transcription, Open Reading Frame (ORF) detection, protein translation, and restriction enzyme site analysis. Results are exported as a text report, CSV summary, and nucleotide count visualization.

---

## ✨ Features

- Read DNA sequences from FASTA files
- Validate DNA sequences
- Count nucleotides (A, T, G, C)
- Calculate GC content (%)
- Calculate AT content (%)
- Generate the reverse complement
- Transcribe DNA to RNA
- Detect Open Reading Frames (ORFs)
- Translate RNA into a protein sequence
- Detect common restriction enzyme recognition sites
- Generate a nucleotide count bar chart
- Export results to:
  - Text report (`sample_report.txt`)
  - CSV summary (`results.csv`)
  - PNG visualization (`nucleotide_counts.png`)
- Accept FASTA files using **command-line arguments (argparse)**

---

## Project Structure

```text
DNA Sequence Toolkit/
│
├── output/
│   ├── nucleotide_counts.png
│   ├── results.csv
│   ├── sample_report.txt
│
├── codon_table.py
├── dna_toolkit.py
├── sample_sequences.fasta
├── restriction_test.fasta
├── requirements.txt
└── README.md
```

---

##  Technologies Used

- Python 3
- Matplotlib
- argparse
- CSV
- File Handling
- Functions
- Dictionaries
- Loops

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/hannamelek/DNA-Sequence-Toolkit.git
```

Navigate into the project directory:

```bash
cd DNA-Sequence-Toolkit
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

##  Usage

This project uses Python's **argparse** module to accept an input FASTA file directly from the command line.

General syntax:

```bash
python dna_toolkit.py <input_fasta_file>
```

### Example 1

Analyze the sample DNA sequence:

```bash
python dna_toolkit.py sample_sequences.fasta
```

### Example 2

Analyze the restriction enzyme test sequence:

```bash
python dna_toolkit.py restriction_test.fasta
```

### Example 3

Analyze your own FASTA file:

```bash
python dna_toolkit.py your_sequence.fasta
```

---

##  Example FASTA File

```fasta
>Sample_Sequence
ATGGCTAACCGTTAGCGATCGATCGTAGCTA
```

---

##  Example Output

The toolkit performs the following analyses:

- Sequence Length
- Nucleotide Counts
- GC Content
- AT Content
- Restriction Enzyme Analysis
- Reverse Complement
- RNA Transcription
- ORF Detection
- Protein Translation

Example:

```text
========== DNA Sequence Toolkit ==========

Input File          : sample_sequences.fasta
Sequence Name       : Sample_Sequence

Sequence Length     : 31 bp
GC Content          : 48.39%
AT Content          : 51.61%

Restriction Enzymes
EcoRI      : Found at position 4
BamHI      : Found at position 13
HindIII    : Not Found
NotI       : Not Found

Reverse Complement:
TAGCTACGATCGATCGCTAACGGTTAGCCAT

RNA Sequence:
AUGGCUAACCGUUAGCGAUCGAUCGUAGCUA

ORF:
AUGGCUAACCGUUAG

Protein Sequence:
MAN

Status:
Analysis completed successfully.
```

---

##  Output Files

After execution, the following files are automatically generated inside the **output/** folder.

| File | Description |
|------|-------------|
| `sample_report.txt` | Human-readable analysis report |
| `results.csv` | Summary of all calculated results |
| `nucleotide_counts.png` | Bar chart showing nucleotide frequencies |

---

## Restriction Enzymes Included

| Enzyme | Recognition Sequence |
|---------|----------------------|
| EcoRI | GAATTC |
| BamHI | GGATCC |
| HindIII | AAGCTT |
| NotI | GCGGCCGC |

---

##  Biological Analyses Performed

The toolkit demonstrates several fundamental bioinformatics workflows:

- DNA sequence validation
- Nucleotide composition analysis
- GC and AT content calculation
- Reverse complement generation
- DNA → RNA transcription
- Open Reading Frame (ORF) identification
- RNA → Protein translation using the genetic code
- Restriction enzyme recognition site analysis

---

## Programming Concepts Practiced

This project demonstrates the use of:

- Python functions
- Dictionaries
- Loops
- Conditional statements
- String manipulation
- File handling
- CSV file generation
- Command-line argument parsing (`argparse`)
- Data visualization using Matplotlib
- FASTA file parsing

---

##  Future Improvements

Possible future enhancements include:

- Support for multi-FASTA files
- Additional restriction enzymes
- Amino acid composition analysis
- Protein molecular weight calculation
- Codon usage statistics
- GC content sliding-window analysis
- Interactive Streamlit web application
- PDF report generation

---

##  Author

**Hanna Melek**

B.Tech Biotechnology  
SRM Institute of Science and Technology

Aspiring Bioinformatics Scientist with interests in computational biology, genomics, and Python-based bioinformatics tool development.

---



⭐ If you found this project useful, consider giving the repository a star!
