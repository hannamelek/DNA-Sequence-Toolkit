#Project name:DNA Sequence Toolkit

#%%
#DNA input
dna = input("Enter a DNA Sequence:").upper()

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

plt.savefig("nucleotide_counts.png")

plt.show()

#%%
#GC content calculation

gc = (g + c)/ length * 100
print(f"GC Content: {gc:.2f}%")

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
#translation to Protein

from codon_table import CODON_TABLE

protein = ""
for i in range(0,len(rna), 3):
    codon = rna[i:i+3]

    if len(codon) != 3:
        break

    amino = CODON_TABLE.get(codon)
    
    if amino == "Stop":
        break

    if amino:
        protein += amino

print(protein)

#%%
print("\n===== DNA Sequence Toolkit =====")
print("DNA :", dna)
print("Length:", length)
print(f"GC Content: {gc:.2f}%")
print("Reverse Complement:", reverse)
print("RNA:", rna)
print("Protein:", protein)





# %%
