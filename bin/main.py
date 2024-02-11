from solver import *
from generator import *
import os


print("Selamat datang di permainan Breach Protocol\n")
print("silahkan pilih aksi yang hendak dilakukan:\n1.Breach Protocol Solver\n2.Breach Protocol Generator")
val = input("silahkan pilih menu: ")
while(val != "1" and val != "2"):
    print("input anda tidak valid!")
    val = input("silahkan pilih menu: ")
val = int(val)

if val == 1:
    txtarg = input("Masukkan file txt yang hendak dimasukkan (gunakan .txt): ")
    if not os.path.isfile("test/"+txtarg):
        print("Tidak ditemukan file yang dimaksud!")
        exit()
    else:
        executeSol(open("test/"+txtarg, "r").read())
else:
    executeGen()
    