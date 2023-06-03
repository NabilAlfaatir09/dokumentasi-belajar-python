pembeli = input("Masukkan nama Pembeli: ")
print("Nama Pembeli :", pembeli)


def fungsimakanan():
    global totalMakan
    global porsi
    global makanan
    print("\n----------------- Menu Makanan -----------------")
    print("1. Nasi Goreng - Rp 15000")
    print("2. Soto        - Rp 9000")
    print("3. Mie Ayam    - Rp 11000")
    pilihanMakanan = int(input("Masukan Pilihan[1/2/3] : "))
    porsi = int(input("Berapa Porsi : "))

    if pilihanMakanan == 1:
        totalMakan = porsi*15000
        print(porsi, " porsi Nasi Goreng Telur = Rp", totalMakan)
        makanan = ("Nasi Goreng")
    elif pilihanMakanan == 2:
        totalMakan = porsi*9000
        print(porsi, " porsi Soto = Rp", totalMakan)
        makanan = ("Soto")
    elif pilihanMakanan == 3:
        totalMakan = porsi*11000
        print(porsi, " porsi Mie Ayam = Rp", totalMakan)
        makanan = ("Mie Ayam")
    else:
        print("Pilihan yang anda pilih tidak ada, silahkan masukan lagi!!")
        fungsimakanan()


def fungsiminuman():
    global totalMinum
    global minum
    global gelas
    print("\n----------------- Menu Minuman -----------------")
    print("1. Es teh    - Rp 2000")
    print("2. Es jeruk  - Rp 3500")
    print("3. Es kopi   - Rp 4000")
    nomor = int(input("Masukan Pilihan[1/2/3]: "))
    gelas = int(input("Berapa Gelas: "))

    if nomor == 1:
        totalMinum = gelas*2000
        print(gelas, " Es Teh = Rp", totalMinum)
        minum = (" Gelas Es Teh")
    elif nomor == 2:
        totalMinum = gelas*3500
        print(gelas, " Gelas Es Jeruk = Rp", totalMinum)
        minum = ("Es Jeruk")
    elif nomor == 3:
        totalMinum = gelas*4000
        print(gelas, " Gelas Es Kopi = Rp", totalMinum)
        minum = ("Es Kopi")
    else:
        print("Pilihan tidak ada, silahkan masukan lagi!!")
        fungsiminuman()


fungsimakanan()
fungsiminuman()
totalsemua = totalMakan+totalMinum

print("\nTotal harus Dibayar: Rp", totalsemua)
uang = int(input("Uang Tunai Pembeli: Rp "))
kembalian = int(uang-totalsemua)
print("Kembalian :", kembalian)

print("\n==================================")
print("========== S T R U K   B E L I =============")
print("==================================")
print("Nama\t\t:", pembeli)
print("Beli\t\t:", porsi, makanan, "( Rp", totalMakan, ")")
print("\t\t ", gelas, minum, "( Rp", totalMinum, ")")
print("Tagihan\t\t: Rp", totalsemua)
print("Dibayar\t\t: Rp", uang)
print("Kembalian\t: Rp", kembalian)
print("==================================")
print("==================================")
