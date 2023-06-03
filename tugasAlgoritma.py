print("GEROBAK FRIED CHICKEN")
print("--------------------------")
print("Kode jenisPotong harga")
print("----------------------------")
print("D    Dada        Rp.2500")
print("P    Paha        Rp.2000")
print("S    Sayap        Rp.1500")

banyakJenis = int(input("Banyak jenis : "))
kodePotong = []
banyakPotong = []
jenisPotong = []
harga = []
jumlah = []

i = 0
while (i < banyakJenis):
    print("Jenis ke - ", i + 1)
    kodePotong.append(input("Kode potong [D/P/S] : "))
    banyakPotong.append(int(input("Banyak potong : ")))
    if kodePotong[i] == "D" or kodePotong[i] == "d":
        jenisPotong.append("Dada")
        harga.append("2500")
        jumlah.append(banyakPotong[i] * int("2500"))
    elif kodePotong[i] == "P" or kodePotong[i] == "p":
        jenisPotong.append("Paha")
        harga.append("2000")
        jumlah.append(banyakPotong[i] * int("2000"))
    elif kodePotong[i] == "H" or kodePotong[i] == "h":
        jenisPotong.append("Sayap")
        harga.append("1500")
        jumlah.append(banyakPotong[i] * int("1500"))
    else:
        jenisPotong.append("Kode salah")
        harga.append("0")
        jumlah.append(banyakPotong[i] * int("0"))
    i = i + 1

print("GEROBAK FRIED CHICKEN")
print("--------------------------")
print("NO   jenis   Harga   Banyak    Jumlah")
print("     Potong  Satuan  Beli      Harga")
print("----------------------------")


a = 0
while (a < banyakJenis):
    print("%i    %s     %s      %i     %i" %
          (a+1, jenisPotong[a], harga[a], banyakPotong[a], jumlah[a]))
    a = a + 1
