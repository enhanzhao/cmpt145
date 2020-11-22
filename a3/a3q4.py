#a3q4 Enhan Zhao enz889 cmpt145

import a3q3 as Exp

file_name = "sequences2.txt"
mini = 40
maxi = 60
f = Exp.create(file_name)
dict = Exp.lengthDistribution(f)

print("Initial Statistics---------------------------------")
print("   ", "Number of Sequences:", Exp.numSequences(f))
print("   ", "Average GC content:", Exp.averageGCcontent(f))
print("   ", "Average Sequence Length:", Exp.averageLength(f))
print("   ", "Sequence Length Distribution:")
print("      ", "Length : Number of Sequences")
for i in dict:
    print("         ", i, ":", dict[i])
print("Removing Sequences with GC content below", mini, "or above", maxi, "\n"+"Updated Statistics-------------------")

Exp.removeLowQuality(f, mini, maxi)
dict = Exp.lengthDistribution(f)

print("   ", "Number of Sequences:", Exp.numSequences(f))
print("   ", "Average GC content:", Exp.averageGCcontent(f))
print("   ", "Average Sequence Length:", Exp.averageLength(f))
print("   ", "Sequence Length Distribution:")
print("      ", "Length : Number of Sequences")
for i in dict:
    print("         ", i, ":", dict[i])