import random as rd

jmltokenunik = int(input())
token = [str(a) for a in input().split()]
ukuranbuffer = int(input())
colrow = [int(a) for a in input().split()]
jmlseq = int(input())
maxseq = int(input())

thematrix = [["" for i in range(colrow[1])] for j in range(colrow[0])]
for i in range(colrow[1]):
    for j in range(colrow[0]):
        thematrix[i][j] = rd.choice(token)
theseq = [["a", "b"] for i in range(jmlseq)]
for i in range(jmlseq):
    panjangseq = rd.randint(1, maxseq)
    seqtemp = ""
    for j in range(panjangseq):
        seqtemp += rd.choice(token)
        if j != panjangseq-1:
            seqtemp += " "
    theseq[i][0] = seqtemp
    theseq[i][1] = rd.randint(5, 50)

print("Didapatkan Matrix dengan bentuk berikut: ")
print("Buffer Size :", ukuranbuffer)
print(f"Matrix Width and Height : {colrow[0]} {colrow[1]}")
for i in range(colrow[1]):
    for j in range(colrow[0]):
        print(f"{thematrix[i][j]} ", end="")
    print()
print("Jumlah sequence :", jmlseq)
for i in range(jmlseq):
    print(theseq[i][0])
    print(theseq[i][1])
verif = input("Apakah ingin menyimpan solusi? (y/n): ")
if verif == "y":
    patharg = input("Masukkan nama file untuk disimpan: ")
    f = open(patharg, "w")
    