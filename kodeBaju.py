kodeBaju = input("Masukkan kode baju [SP/AD] :")
ukuran = input("Masukkan ukuran baju [S/M] :")

if kodeBaju == "SP" or kodeBaju == "sp":
    merk = "SuperDry"
    if ukuran == "S" or ukuran == "s":
        harga = 450000
    elif ukuran == "M" or ukuran == "m":
        harga = 500000
    else:
        harga = 0
elif kodeBaju == "AD" or kodeBaju == "ad":
    merk = "Adidas"
    if ukuran == "S" or ukuran == "s":
        harga = 650000
    elif ukuran == "M" or ukuran == "m":
        harga = 700000
    else:
        harga = 0
else:
    merk = "Anda salah input kode merk"
    harga = 0

print("---------------------------------")
print("Merk Baju : " + str(merk))
print("harga baju : Rp.", harga)
