import wget
#import ssl
import requests
from bs4 import BeautifulSoup
import os
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
from Bio import AlignIO
import matplotlib.pyplot as plt
import numpy as np
from Bio import SeqIO

all_entries = os.listdir("D:\\plasmid\\")
kozak_list = []

#len(all_entries)-1

for file_index in range(500):
    Plasmid_file = f"D:\plasmid\{all_entries[file_index]}"

    for seq_record in SeqIO.parse(Plasmid_file, "genbank"):
        pass
        #print(seq_record.id)
        #print(repr(seq_record.seq))
        #print(len(seq_record))

    identifiers = [seq_record.id for seq_record in SeqIO.parse(Plasmid_file, "genbank")]
    records = list(SeqIO.parse(Plasmid_file, "genbank"))
    first_record = records[0] 
    try:
        if (seq_record.seq.index("ATG")>12) and (seq_record.seq.index("ATG") < len(seq_record)-14):
            kozak_list.append(first_record[first_record.seq.index("ATG") - 10 : first_record.seq.index("ATG") + 13][-25:-2])
        #print(first_record[first_record.seq.index("ATG") - 10 : first_record.seq.index("ATG") + 13])
    except ValueError:
        continue

msa = MultipleSeqAlignment(kozak_list)

alignment_length = msa.get_alignment_length()
nucleotides = ["A", "T", "G", "C"]
counts = {nuc: [str(msa[:, i]).count(nuc) for i in range(alignment_length)] for nuc in nucleotides}

# Plotting nucleotide counts across alignment positions
plt.figure(figsize=(10, 6))
for nuc in nucleotides:
    plt.plot(range(alignment_length), counts[nuc], label=f"{nuc} count")
plt.xlabel("Alignment Position")
plt.ylabel("Count")
plt.title("Nucleotide Composition Across Alignment")
plt.legend()
plt.show()
