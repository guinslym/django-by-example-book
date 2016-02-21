import os
import os.path
clear = lambda: os.system('clean')
def RNA2ENZ(RNA, number):
    if RNA[0][number:number + 3] == "UUU" or  RNA[0][number:number + 3] == "UUC":
        letter = "F"
        return letter
    elif RNA[0][number:number + 3] == "UUA" or  RNA[0][number:number + 3] == "UUG":
        letter = "L"
        return letter
    elif RNA[0][number:number + 3] == "CUU" or  RNA[0][number:number + 3] == "CUC" or RNA[0][number:number + 3] == "CUG" or RNA[0][number:number + 3] == "CUA":
        letter = "L"
        return letter
    elif RNA[0][number:number + 3] == "AUU" or  RNA[0][number:number + 3] == "AUC" or RNA[0][number:number + 3] == "AUA":
        letter = "I"
        return letter
    elif RNA[0][number:number + 3] == "AUG":
        letter = "M"
        return letter 
    elif RNA[0][number:number + 3] == "GUU" or  RNA[0][number:number + 3] == "GUC" or RNA[0][number:number + 3] == "GUA" or RNA[0][number:number + 3] == "GUG":
        letter = "V"
        return letter
    elif RNA[0][number:number + 3] == "UCU" or  RNA[0][number:number + 3] == "UCC" or RNRNA[0][number:number + 3] == "UCA" or RNA[0][number:number + 3] == "UCG":
        letter = "S"
        return letter
    elif RNA[0][number:number + 3] == "CCG" or  RNA[0][number:number + 3] == "CCC" or RNA[0][number:number + 3] == "CCA" or RNA[0][number:number + 3] == "CCU":
        letter = "P"
        return letter
    elif RNA[0][number:number + 3] == "ACG" or  RNA[0][number:number + 3] == "ACA" or RNA[0][number:number + 3] == "ACC" or RNA[0][number:number + 3] == "ACU":
        letter = "T"
        return letter
    elif RNA[0][number:number + 3] == "GCU" or  RNA[0][number:number + 3] == "GCC" or RNA[0][number:number + 3] == "GCA" or RNA[0][number:number + 3] == "GCG":
        letter = "A"
        return letter
    elif RNA[0][number:number + 3] == "UAU" or  RNA[0][number:number + 3] == "UAC":
        letter = "Y"
        return letter
    elif RNA[0][number:number + 3] == "UAA" or  RNA[0][number:number + 3] == "UAG":
        letter = "."
        return letter
    elif RNA[0][number:number + 3] == "CAU" or  RNA[0][number:number + 3] == "CAC":
        letter = "H"
        return letter
    elif RNA[0][number:number + 3] == "CAA" or  RNA[0][number:number + 3] == "CAG":
        letter = "Q"
        return letter
    elif RNA[0][number:number + 3] == "AAU" or  RNA[0][number:number + 3] == "AAC":
        letter = "N"
        return letter
    elif RNA[0][number:number + 3] == "AAA" or  RNA[0][number:number + 3] == "AAG":
        letter = "K"
        return letter
    elif RNA[0][number:number + 3] == "GAU" or  RNA[0][number:number + 3] == "GAC":
        letter = "D"
        return letter
    elif RNA[0][number:number + 3] == "GAA" or  RNA[0][number:number + 3] == "GAG":
        letter = "E"
        return letter
    elif RNA[0][number:number + 3] == "UGU" or  RNA[0][number:number + 3] == "UGC":
        letter = "C"
        return letter
    elif RNA[0][number:number + 3] == "UGA":
        letter = "."
        return letter
    elif RNA[0][number:number + 3] == "UGG":
        letter = "W"
        return letter
    elif RNA[0][number:number + 3] == "CGU" or  RNA[0][number:number + 3] == "CGC" or RNA[0][number:number + 3] == "CGA" or RNA[0][number:number + 3] == "CGG":
        letter = "R"
        return letter
    elif RNA[0][number:number + 3] == "GGU" or  RNA[0][number:number + 3] == "GGC" or RNA[0][number:number + 3] == "GGA" or RNA[0][number:number + 3] == "GGG":
        letter = "G"
        return letter
    elif RNA[0][number:number + 3] == "AGU" or  RNA[0][number:number + 3] == "AGC":
        letter = "S"
        return letter
    elif RNA[0][number:number + 3] == "AGA" or  RNA[0][number:number + 3] == "AGG":
        letter = "R"
        return letter
    else:
        letter = "-"
        return letter
def DNA2RNA(Strand, numb):
        if Strand[0][numb] == "G":
            letter = "G"
            return letter
        elif Strand[0][numb] == "C":
            letter = "C"
            return letter
        elif Strand[0][numb] == "T":
            letter = "U"
            return letter
        elif Strand[0][numb] == "A":
            letter = "A"
            return letter
def DNAfilp(DNA, num):
        if DNA[0][num] == "G":
            letter = "C"
            return letter
        elif DNA[0][num] == "C":
            letter = "G"
            return letter
        elif DNA[0][num] == "T":
            letter = "A"
            return letter
        elif DNA[0][num] == "A":
            letter = "T"
            return letter
clear()
print("please delete the 5' and 3' from the file")
filename = input("please enter file name to convert:")
clear()
intron = input("are there any introns? If so enter 'yes' else enter 'no':")
if intron == "yes":
    clear()
    intronfile = input("please enter the file name with the introns and please make sure there is a space inbetween each intron (tip:max of five):")
else:
    print("")
clear()
outputfileDNA = input("please enter outputfile for DNA name:")
clear()
outputfileRNA = input("please enter outputfile for RNA name:")
clear()
outputfileENZ = input("please enter outputfile for ENZ name:")
clear()
prime = input("which is first 5' or 3' (tip: just enter the number):")
clear()
file = open(filename, 'r')
DNA = file.read()
DNAlength = len(DNA)
DNA = DNA.split()
intfile = open(intronfile, 'r')
introns = intfile.read()
introns = introns.split()
print(introns)
num = 0
code = ""
input()
clear()
for number in range(0, DNAlength):
    code = code + DNAfilp(DNA, num)
    num = num + 1
if prime == 5:
    realcode = "3'" +code + "5'"
elif prime == 3:
    realcode = "5'" + code + "3'"
else:
    realcode = code
if prime == 5:
    DNAtop = "5'" + DNA[0] + "3'"
elif prime == 3:
    DNAtop = "3'" + DNA[0] + "5'"
else:
    DNAtop = DNA[0]
outputDNAstrand = DNAtop + " " + realcode
DNAstrand = code + " " + DNA[0]
realcode = realcode.split()
code = code.split()
RNA = ""
numb = 0
if prime == 5:
    Strand = DNA
elif prime == 3:
    Strand = code
else:
    Strand = DNA
for number in range(0, DNAlength):
    RNA = RNA + DNA2RNA(Strand, numb)
    numb = numb + 1
count = 0

input()
RNA = str(RNA)

for number in range(0, len(introns)):
    RNA = RNA.replace(introns[count], "")
    count = count + 1
RNA = RNA.split()
print(RNA[0])

ENZlength = len(RNA)/3
number1 = 0
number2 = 1
number3 = 2
ENZ1 = ""
ENZ2 = ""
ENZ3 = ""
input()

for number in range(0, ENZlength):
    ENZ1 = ENZ1 + RNA2ENZ(RNA, number1)
    number1 = number1 + 3
    input()
input()
for number in range(0, ENZlength):
    ENZ2 = ENZ2 + RNA2ENZ(RNA, number2)
    number2 = number2 + 3
for number in range(0, ENZlength):
    ENZ3 = ENZ3 + RNA2ENZ(RNA, number3)
    number3 = number3 + 3


outputENZ = " ENZ1:  " + ENZ1 + " ENZ2:  " + ENZ2 + " ENZ3:  " + ENZ3
outputRNA = "RNA: " + str(RNA[0])
if os.path.isfile(outputfileDNA) == True:
    os.remove(outputfileDNA)
out_file = open(outputfileDNA, "w")
out_file.write(outputDNAstrand)
out_file.close()
if os.path.isfile(outputfileRNA) == True:
    os.remove(outputfileRNA)
out_file = open(outputfileRNA, "w")
out_file.write(outputRNA)
out_file.close()
if os.path.isfile(outputfileENZ) == True:
    os.remove(outputfileENZ)
out_file = open(outputfileENZ, "w")
out_file.write(outputENZ)
out_file.close()
input("all done!")


"""
RNA = str(RNA)

for number in range(0, len(introns)):
    RNA = RNA.replace(introns[count], "")
    count = count + 1
RNA = RNA.split()
"""