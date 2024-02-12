import time

sizebuffer = 0
colrow = []
matrixnya = []
size = 0
sequences = []

def txtParse(txtString):
    arrRes = []
    strtemp = ""
    for i in txtString:
        if i == "\n":
            arrRes.append(strtemp)
            strtemp = ""
        else:
            strtemp += i
    if strtemp != "":
        arrRes.append(strtemp)
    return arrRes

def proses(arrRes):
    global size; global sizebuffer; global colrow; global matrixnya; global sequences
    sizebuffer = int(arrRes[0])
    colrow = [int(i) for i in arrRes[1].split()]
    matrixnya = [[0 for i in range(colrow[0])] for j in range(colrow[1])]
    for i in range(colrow[1]):
        matrixnya[i] = [str(a) for a in arrRes[2+i].split()]
    size = int(arrRes[2+colrow[1]])
    sequences = [["a", "b"] for j in range(size)]
    for i in range(size):
        sequences[i][0] = arrRes[3+colrow[1]+(2*i)]
        sequences[i][1] = int(arrRes[4+colrow[1]+(2*i)])

maxval = -1
maxarr = ""
maxcoor = []

def evaluate(arr, coor):
    global maxval; global maxarr; global maxcoor
    strtemp = ""
    for i in range(len(arr)):
        strtemp += arr[i]
        if i != len(arr)-1:
            strtemp += " "
    valtemp = 0
    for i in range(len(sequences)):
        if sequences[i][0] in strtemp:
            valtemp += sequences[i][1]
    if valtemp > maxval or (valtemp == maxval and len(strtemp) < len(maxarr)):
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
    # jika buffer kosong
    if len(arrtemp) == 0:
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
                    if uniquecoor(coortemp2):
                        evaluate(arrtemp2, coortemp2)
                    iterate(arrtemp2, coortemp2, False)
        else:
            for i in range(colrow[0]):
                if i != coorrecent[1]:
                    arrtemp2 = arrtemp.copy()
                    coortemp2 = coortemp.copy()
                    arrtemp2.append(matrixnya[coorrecent[0]][i])
                    coortemp2.append((coorrecent[0], i))
                    if uniquecoor(coortemp2):
                        evaluate(arrtemp2, coortemp2)
                    iterate(arrtemp2, coortemp2, True)

def executeSol(txtString):
    arg = txtParse(txtString)
    proses(arg)
    start_time = time.perf_counter()
    iterate([], [], True)
    print()
    print(maxval)
    print(maxarr)
    for i in maxcoor:
        print(f"{i[1]+1}, {i[0]+1}")
    end_time = time.perf_counter()
    print(f"\nElapsed time : {round((end_time-start_time)*1000, 2)}ms")
    verif = input("Apakah ingin menyimpan solusi? (y/n): ")
    if verif == "y":
        patharg = input("Masukkan nama file untuk disimpan: ")
        f = open("test/"+patharg, "w")
        f.write(f"{maxval}\n{maxarr}")
        for i in maxcoor:
            f.write(f"\n{i[1]+1}, {i[0]+1}")
        f.close()
        print("Solusi berhasil disimpan!")