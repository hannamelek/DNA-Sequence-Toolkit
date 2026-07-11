# 🧬 DNA Sequence Toolkit

A beginner-friendly bioinformatics toolkit written in **Python** for analyzing DNA sequences from FASTA files.

This project performs common molecular biology analyses, including nucleotide composition, GC/AT content calculation, reverse complement generation, RNA transcription, ORF detection, protein translation, and restriction enzyme site analysis. The toolkit also generates a summary report, CSV output, and a nucleotide count visualization.

---

## ✨ Features

- Read DNA sequences from a FASTA file
- Validate DNA sequences
- Count nucleotides (A, T, G, C)
- Calculate GC content
- Calculate AT content
- Generate the reverse complement
- Transcribe DNA to RNA
- Detect Open Reading Frames (ORFs)
- Translate RNA into a protein sequence
- Detect common restriction enzyme recognition sites
- Generate a nucleotide count bar chart
- Save results as:
  - Text report (`sample_report.txt`)
  - CSV file (`results.csv`)
  - PNG visualization (`nucleotide_counts.png`)

---

##  Project Structure

```
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
- CSV module
- File Handling
- Dictionaries
- Loops
- Functions

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/DNA-Sequence-Toolkit.git
```

Move into the project folder:

```bash
cd DNA-Sequence-Toolkit
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

##  How to Run

Open `dna_toolkit.py` in VS Code and run the script.

The program reads the FASTA file specified in:

```python
filename = "sample_sequences.fasta"
```

To analyze another sequence, simply change the filename:

```python
filename = "restriction_test.fasta"
```

and run the program again.

---

##  Example FASTA

```fasta
>Sample_Sequence
ATGGCTAACCGTTAGCGATCGATCGTAGCTA
```

---

##  Example Output

The toolkit reports:

- Sequence length
- Nucleotide counts
- GC Content
- AT Content
- Reverse Complement
- RNA Sequence
- ORF
- Protein Sequence
- Restriction enzyme sites

Example:

```
Sequence Length : 31 bp
GC Content      : 48.39%
AT Content      : 51.61%

Restriction Enzymes
EcoRI      : Found at position 4
BamHI      : Found at position 13
HindIII    : Not Found
NotI       : Not Found

RNA Sequence:
AUGGCUAACCGUUAGCGAUCGAUCGUAGCUA

ORF:
AUGGCUAACCGUUAG

Protein:
MAN
```

---

##  Output Files

After running the program, the following files are generated inside the `output/` folder:

| File | Description |
|------|-------------|
| `sample_report.txt` | Human-readable analysis report |
| `results.csv` | Tabular summary of results |
| `nucleotide_counts.png` | Bar chart of nucleotide frequencies |

---

##  Restriction Enzymes Included

| Enzyme | Recognition Site |
|---------|------------------|
| EcoRI | GAATTC |
| BamHI | GGATCC |
| HindIII | AAGCTT |
| NotI | GCGGCCGC |

---

##  Concepts Practiced

This project helped reinforce:

- Python programming
- Functions
- Dictionaries
- Loops
- String manipulation
- File handling
- CSV file generation
- Data visualization with Matplotlib
- FASTA file parsing
- Molecular biology concepts
  - DNA transcription
  - ORF identification
  - Protein translation
  - Restriction enzyme analysis

---

##  Future Improvements

Possible future enhancements include:

- Command-line support using `argparse`
- Multi-sequence FASTA analysis
- Support for additional restriction enzymes
- Protein molecular weight calculation
- Amino acid composition analysis
- GUI using Tkinter or Streamlit
- Export results as PDF

---

##  Author

**Hanna Melek**

B.Tech Biotechnology  
SRM Institute of Science and Technology

Learning Bioinformatics, Python, and Computational Biology through hands-on projects.

---

⭐ If you found this project useful or interesting, feel free to star the repository!
