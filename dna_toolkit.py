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







# %%
