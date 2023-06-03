ulang = 2
for i in range(ulang):
    print("Data Ke -" + str(i+1))
    nama = input("Masukkan NIM anda : ")
    uts = int(input("Masukkan nilai UTS anda : "))
    uas = int(input("Masukkan nilai UAS : "))
    print("NIM anda adalah %s nilai UTS anda %i nilai URS anda %i" %
          (nama, uts, uas))
