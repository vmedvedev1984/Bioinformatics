from Bio.Seq import Seq
my_seq = Seq("GATCG")
for index, letter in enumerate(my_seq):
    print("%i %s" % (index, letter))

print(my_seq[0])  # first lette
print(my_seq[2])  # third letter
print(my_seq[-1])  # last letter

print("AAAA".count("AA")) #quik counting
print(Seq("AAAA").count("AA"))

lenght_of_seq = len(my_seq) #mesurement lenght of sequence
print(lenght_of_seq)
print(100 * (my_seq.count("G") + my_seq.count("C")) / len(my_seq)) # GC-content
