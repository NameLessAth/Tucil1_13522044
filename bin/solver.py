import time


def txtParse(txtString):
    line = 1



size = int(input())
sizebuffer = size

colrow = [int(i) for i in input().split()]
matrixnya = [[0 for i in range(colrow[0])] for j in range(colrow[1])]
for i in range(colrow[1]):
    matrixnya[i] = [str(i) for i in input().split()]

size = int(input())
sequences = [["a", "b"] for j in range(size)]
for i in range(size):
    sequences[i][0] = input(); sequences[i][1] = int(input())

maxval = 20
maxarr = "BD BD BD"
maxcoor = [(1,1), (1,3), (2,3)]

def evaluate(arr, coor):
    global maxval; global maxarr; global maxcoor
    strtemp = ""
    for i in arr:
        strtemp = strtemp + i + " "
    valtemp = 0
    for i in range(len(sequences)):
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

def iterate(arrtemp, coortemp, rowbool):
    # jika buffer penuh
    if len(arrtemp) == sizebuffer and uniquecoor(coortemp):
        evaluate(arrtemp, coortemp)
    # jika buffer kosong
    elif len(arrtemp) == 0:
        for i in range(colrow[0]):
            arrtemp2 = arrtemp.copy()
            coortemp2 = coortemp.copy()
            arrtemp2.append(matrixnya[0][i])
            coortemp2.append((0, i))
            iterate(arrtemp2, coortemp2, True)
    # jika buffer belum penuh
    elif len(arrtemp) < sizebuffer:
        coorrecent = coortemp[len(coortemp)-1]
        if rowbool:
            for i in range(colrow[1]):
                if i != coorrecent[0]:
                    arrtemp2 = arrtemp.copy()
                    coortemp2 = coortemp.copy()
                    arrtemp2.append(matrixnya[i][coorrecent[1]])
                    coortemp2.append((i, coorrecent[1]))
                    iterate(arrtemp2, coortemp2, False)
        else:
            for i in range(colrow[0]):
                if i != coorrecent[1]:
                    arrtemp2 = arrtemp.copy()
                    coortemp2 = coortemp.copy()
                    arrtemp2.append(matrixnya[coorrecent[0]][i])
                    coortemp2.append((coorrecent[1], i))
                    iterate(arrtemp2, coortemp2, True)

start_time = time.perf_counter()
iterate([], [], True)
print("end")
print(maxval)
print(maxarr)
print(maxcoor)
end_time = time.perf_counter()
print("\nElapsed time : ", (end_time-start_time))