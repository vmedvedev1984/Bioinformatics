from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

my_seq = Seq("GATCG")
for index, letter in enumerate(my_seq):
    print("%i %s" % (index, letter))

print(my_seq[0])  # first lette
print(my_seq[2])  # third letter
print(my_seq[-1])  # last letter
print(my_seq[4:12])
print(my_seq[2::3])
comlement_seq = my_seq[::-1] # sequence comlement
stringify_seq = str(my_seq)
fasta_format_string = ">Name\n%s\n" % my_seq

contigs = [Seq("ATG"), Seq("ATCCCG"), Seq("TTGCA")]
spacer = Seq("N" * 10)
spacer.join(contigs)

print("AAAA".count("AA")) #quik counting
print(Seq("AAAA").count("AA"))

lenght_of_seq = len(my_seq) #mesurement lenght of sequence
print(lenght_of_seq)
print(100 * (my_seq.count("G") + my_seq.count("C")) / len(my_seq)) # GC-content

print(gc_fraction(my_seq))
