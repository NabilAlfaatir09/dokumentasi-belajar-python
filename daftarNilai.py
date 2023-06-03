from numpy import append
import pandas as pd

listNim = []
listNama = []
listUts = []
listUas = []
listTotal = []

ulang = 5
for i in range(ulang):
    print("Data ke - " + str(i + 1))
    listNim.append(input("Nim : "))
    listNama.append(input("Nama : "))
    listUts.append(int(input("Nilai UTS : ")))
    listUas.append(int(input("Nilai UAS : ")))

for i in range(ulang):
    listTotal.append(listUas[i] + listUts[i] / 2)

tamu = {
    "NIM": listNim,
    "Nama lengkap": listNama,
    "Nilai UTS": listUts,
    "Nilai UAS": listUas,
    "Rata-rata": listTotal
}
dataTamu = pd.DataFrame(tamu)
print("=========================DAFTAR NILAI===============================")
print(dataTamu)
print("=====================================================================")
