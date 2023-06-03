pembeli = input("Input nama pembeli : ")
noHp = input("Input no. Handphone : ")
jurusan = input("Input Jurusan [SBY/BL/LMP] : ")

if jurusan == "SBY":
    namaJurusan = "Surabaya"
    harga = 300000
elif jurusan == "BL":
    namaJurusan = "Bali"
    harga = 350000
else:
    namaJurusan = "Lampung"
    harga = 500000

jumlah = int(input("Masukkan jumlah beli : "))
if jumlah >= 3:
    potongan = (jumlah * harga) * 0.1
else:
    potongan = 0
total = (jumlah * harga) - potongan

# cetak hasil
print("----------------------------------")
print("         PENJUALAN TIKET BUS")
print("                XYZ")
print("----------------------------------")
print("Nama pembeli              : " + str(pembeli))
print("No. Handphone             : " + str(noHp))
print("Kode jurusan yang dipilih : " + str(jurusan))
print("Nama kota tujuan          : " + str(namaJurusan))
print("Harga                     : ", + (harga))
print("Jumlah beli               : ", + (jumlah))
print("----------------------------------")
print("Potongan yang didapat     : ", + (potongan))
print("Total bayar                : ", + (total))
uangBayar = int(input("Masukkan uang bayar : "))
uangKembali = uangBayar-total
print("Uang kembali : ", + uangKembali)
