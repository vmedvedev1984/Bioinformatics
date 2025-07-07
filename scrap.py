import wget
#import ssl
import requests
from bs4 import BeautifulSoup
'''
for i in range(14559, 20000):
    print(i)
    url = f'https://www.addgene.org/{i}/sequences/'
    page = requests.get(url)
    if page.status_code == 200:
        
        plasmid_name = []
        soup = BeautifulSoup(page.text, "html.parser")
        try:
            # Code that might raise an exception
            plasmid_name = repr(soup.find_all('span', class_='material-name')[0].string)  # This will raise a ZeroDivisionError
        except IndexError:
            # Code to execute if ExceptionType occurs in the try block
            print("КРИТИЧЕСКАЯ ОШИБКА В")
            print(soup.find_all('span', class_='material-name'))
            continue
        
        try:
            # Code that might raise an exception
            links = soup.find_all('a', class_='genbank-file-download')[0].get('href')  # This will raise a ZeroDivisionError
        except IndexError:
            # Code to execute if ExceptionType occurs in the try block
            print("Ошибка в " + plasmid_name)
            continue
        #links = soup.find_all('a', class_='genbank-file-download')[0].get('href')
        print(i)
        print(plasmid_name)
        plasmid_name = plasmid_name.replace("/", '_').replace(":", '_').replace("'","_").replace('"',"").replace('>',"")
        r = requests.get(links)
        with open(f'D:\\plasmid\\{plasmid_name}.gbk', "wb") as file:
            file.write(r.content)

'''

from Bio import SeqIO

Plasmid_file = "D:\plasmid\_223 pCS EGFP DEST_.gbk"

for seq_record in SeqIO.parse(Plasmid_file, "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

identifiers = [seq_record.id for seq_record in SeqIO.parse(Plasmid_file, "genbank")]
print(identifiers)

records = list(SeqIO.parse(Plasmid_file, "genbank"))

print("Found %i records" % len(records))

print("The first record")
first_record = records[0] 
print(first_record.id)
print(repr(first_record.seq))
print(len(first_record))

all_species = [seq_record.annotations["comment"] for seq_record in SeqIO.parse(Plasmid_file, "genbank")]
print(all_species)

from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
from Bio import AlignIO
import matplotlib.pyplot as plt
import numpy as np

print("Pairwise Sequence Alignment using `pairwise2` with Custom Scoring:\n")

seq1 = "AAAATG"
seq2 = str(all_species)

alignments = pairwise2.align.globalms(seq1, seq2, 2, -1, -0.5, -0.1)
for alignment in alignments:
    print(format_alignment(*alignment))

###---MSA---###

print("\nMultiple Sequence Alignment (MSA):\n")


# Step 1: Create individual sequences
sequence1 = Seq("AGTACACTG")
sequence2 = Seq("CCTAGACTG")
sequence3 = Seq("AGTACGCTG")
sequence4 = Seq("TTTACACTA")

# Step 2: Wrap sequences into SeqRecords
align1 = SeqRecord(sequence1, id="seq1")
align2 = SeqRecord(sequence2, id="seq2")
align3 = SeqRecord(sequence3, id="seq3")
align4 = SeqRecord(sequence4, id="seq4")

# Create an MSA using Biopython's MultipleSeqAlignment class
msa = MultipleSeqAlignment([align1, align2, align3, align4])
print(msa)
# Visualizing the MSA nucleotide counts
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
