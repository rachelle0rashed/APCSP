"""
 This program shows how DNA sequences encode proteins
"""
 
# Stores the mappings of given nucleotides to the corresponding amino acids
NUCLEOTIDE_TO_AMINO = dict({
    "GCT GCC GCA GCG": "A",
    "CGT CGC CGA CGG AGA AGG": "R",
    "AAT AAC": "N",
    "GAT GAC": "D",
    "TGT TGC": "C",
    "CAA CAG": "Q",
    "GAA GAG": "E",
    "GGT GGC GGA GGG": "G",
    "CAT CAC": "H",
    "ATT ATC ATA": "I",
    "ATG": "M/start",
    "TTA TTG CTT CTC CTA CTG": "L",
    "AAA AAG": "K",
    "TTC TTT": "F",
    "CCT CCC CCA CCG": "P",
    "TCT TCC TCA TCG AGT AGC": "S",
    "ACT ACC ACA ACG": "T",
    "TGG": "W",
    "TAT TAC": "Y",
    "GTT GTC GTA GTG": "V",
    "TAA TGA TAG": "stop"})

# Stores the mappings of amino chains to the corresponding proteins
# Currently only one stored. There exist hundreds of thousands of proteins in the human body alone.
AMINO_TO_PROTEIN = dict({"NLYIQWLKDGGPSSGRPPPS": "TRP-Cage"})
 

# Translates a group of 3 nucleotides into the corresponding amino acid
def nucleotides_to_amino_acid(nucleotides):
    for key in NUCLEOTIDE_TO_AMINO:
        if nucleotides in key:
            return NUCLEOTIDE_TO_AMINO[key];
    return ""


# Translates a given amino acid chain to the corresponding protein
def amino_chain_to_protein(amino_chain):
    return AMINO_TO_PROTEIN[amino_chain]

# Translates a DNA chain into the corresponding amino acid chain
def DNA_to_amino_chain(dna):
    result_chain = ""
    
    #Every three nucleotides in the DNA chain encodes a single amino acid
    for i in range(0, len(dna), 3):
        nucleotides = dna[i:i+3]
        amino_acid = nucleotides_to_amino_acid(nucleotides)
        result_chain += amino_acid
    return result_chain


# This represents a sequence of nucleotides, the building blocks of DNA
dna = "AACCTTTACATTCAGTGGCTGAAGGACGGGGGTCCGAGTTCTGGGCGTCCTCCTCCGTCT"

# This is the amino acid chain that results from this DNA
amino_chain = DNA_to_amino_chain(dna)
print(amino_chain)
# This is the protein that is encoded by the given amino chain
protein = amino_chain_to_protein(amino_chain)

print("The DNA sequence:")
print(dna)
print("Encodes the following amino acids:")
print(amino_chain)
print("Which encodes the folowing protein:")
print(protein)