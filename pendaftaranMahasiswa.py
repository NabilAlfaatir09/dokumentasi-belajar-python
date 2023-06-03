# Input 
print("PENDAFTARAN MAHASISWA BARU")
nama = input("Masukkan nama  : ")
nis = input("Masukkan nis : ")
jurusan = input("Masukkan jurusan[SI/SIA] : ").upper()

# Pilihan jurusan
if jurusan == "SI":
    Prodi = "Sistem Informasi"
    harga = "2,400,000"
elif jurusan == "SIA":
    Prodi = "Sistem Informasi akutansi"
    harga = "2,000,000"

# Hasil
print("\n=====================================")
print("Nama : " + nama)
print("NIS  :  " + nis)
print("""Kode               Nama Prodi                  Harga\n""", jurusan, "           ", Prodi, "           ", harga)
print("=======================================")
