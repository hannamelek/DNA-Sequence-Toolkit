#Project name:DNA Sequence Toolkit

#%%

def read_fasta(filename):
    header = ""
    sequence = ""

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                header = line[1:]      
            else:
                sequence += line

    return header, sequence


#DNA input
import argparse

parser = argparse.ArgumentParser(description="DNA Sequence Toolkit")
parser.add_argument("filename", help="Input FASTA file")

args = parser.parse_args()

filename = args.filename

sequence_name, dna = read_fasta(filename)

dna = dna.upper()

#validation of DNA sequence
valid_bases = "ATGC"

for base in dna:
    if base not in valid_bases:
        print("Invalid DNA sequence!")
        exit()

length = len(dna)

print("Sequence Length:", length)

#counting nucleotides

a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")

print("A:", a)
print("T:", t)
print("G:", g)
print("C:", c)

#%%
#Visualizing Nucleotide counts

import matplotlib.pyplot as plt

bases = ["A", "T", "G", "C"]
counts = [a, t, g, c]

plt.figure(figsize=(6,4))
plt.bar(bases, counts, color=["green", "red", "yellow", "blue"])

plt.title("Nucleotide Counts")
plt.xlabel("Bases")
plt.ylabel("Count")

plt.savefig("output/nucleotide_counts.png")


#%%
#GC content calculation

gc = (g + c)/ length * 100
print(f"GC Content: {gc:.2f}%")

#%%
# AT content calculation

at = ( a + t) / length * 100
print(f"AT Content: {at:.2f}%")

#%%
# Restriction Enzyme Analysis

restriction_enzymes = {
    "EcoRI": "GAATTC",
    "BamHI": "GGATCC",
    "HindIII": "AAGCTT",
    "NotI": "GCGGCCGC"
}

restriction_reports = ""

print("\nRestriction Enzyme Analysis")

for enzyme, site in restriction_enzymes.items():

    if site in dna:

        position = dna.find(site) + 1

        print(f"{enzyme} site found at position {position}")

        restriction_reports += f"{enzyme} Found at position {position}\n"
    else:

        print(f"{enzyme} site not found.")
        restriction_reports += f"{enzyme} Not Found\n"

# %%
# reverse complement

complement = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G",
}

reverse = ""
for base in dna:
    reverse += complement[base]

reverse = reverse[::-1]

print("Reverse Complement:", reverse)

# %%
#Transcription to RNA
rna = dna.replace("T", "U")
print("RNA Sequence:", rna)

#%%
#finding ORFs

stop_codons = ["UAA", "UAG", "UGA"]

start = rna.find("AUG")

if start == -1:
    print("No ORF found!")

else:

    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]

        if codon in stop_codons:
            orf = rna[start:i+3]
            break
    print("ORF:", orf)
        


#%%
#translation to Protein

from codon_table import CODON_TABLE

protein = ""
for i in range(0,len(orf), 3):
    codon = orf[i:i+3]

    if len(codon) < 3:
        break

    amino = CODON_TABLE.get(codon, "?")
    
    if amino == "*":
        break

    if amino:
        protein += amino

print("Protein Sequence:", protein)

#%%
report = f"""
=========== DNA Sequence Toolkit ===========

Input File          : {filename}
Sequence Name       : {sequence_name}
DNA Sequence        : {dna}
Sequence Length     : {length} bp
GC Content          : {gc:.2f}%
AT Content          : {at:.2f}%
Restriction Enzymes : {restriction_reports}

Reverse Complement  : {reverse}
RNA Sequence        : {rna}
ORF                 : {orf}
Protein Sequence    : {protein}

Status              : Analysis completed successfully.
"""

print(report)

with open("output/output.txt", "w") as file:
    file.write(report)


#%%
#csv results
import csv
with open("output/results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Sequence Name",
        "Length(bp)",
        "A",
        "T",
        "G",
        "C",
        "GC Content(%)",
        "AT Content(%)",
        "Restriction Enzymes",
        "Reverse Complement",
        "RNA Sequence",
        "ORF",
        "Protein Sequence"
   ])
    
    writer.writerow([
        sequence_name,
        length,
        a,
        t,
        g,
        c,
        f"{gc:.2f}",
        f"{at:.2f}",
        restriction_reports.replace("\n", "; "),
        reverse,
        rna,
        orf,
        protein
    ])

# %%
