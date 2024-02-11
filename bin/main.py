size = int(input())
buffernya = [-69 for i in range(size)]

rowcol = [int(i) for i in input().split()]
matrixnya = [[0 for i in range(rowcol[0])] for j in range(rowcol[1])]
for i in range(rowcol[1]):
    matrixnya[i] = [str(i) for i in input().split()]

size = int(input())
sequences = [["a", "b"] for j in range(size)]
for i in range(size):
    sequences[i][0] = input(); sequences[i][1] = input()

print("end")
print(matrixnya)
print(sequences)

maxval = -1
maxarr = ""
maxcoor = []

def evaluate(arr, coor):
    strtemp = ""
    for i in arr:
        strtemp = strtemp + i + " "
    valtemp = 0
    for i in sequences:
        if sequences[i][0] in strtemp:
            valtemp += sequences[i][1]
    if valtemp > maxval:
        maxarr = strtemp
        maxval = valtemp
        maxcoor = coor  

def uniquecoor(coor):
    for i in range(len(coor)):
        for j in range(i+1, len(coor)):
            if coor[i] == coor[j]:
                return False
    return True