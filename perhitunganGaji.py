# input data karyawan
print("PROGRAM HITUNG GAJI KARYAWAN")
namaKaryawan = input("Nama karyawan : ")
golonganJabatan = input("Golongan jabatan[1/2/3] : ")
pendidikan = input("Pendidikan[SMA/D1/D3/S1] : ").upper()
jamKerja = int(input("jumlah jam kerja : "))
gaji = 300000
gajiPersen = gaji / 100

# proses perhitungan gaji
if golonganJabatan == "3":
    tunjanganJabatan = gajiPersen * 15
elif golonganJabatan == "2":
    tunjanganJabatan = gajiPersen * 10
elif golonganJabatan == "1":
    tunjanganJabatan = gajiPersen * 5
if pendidikan == "S1":
    tunjanganPendidikan = gajiPersen * 30
elif pendidikan == "D3":
    tunjanganPendidikan = gajiPersen * 20
elif pendidikan == "D1":
    tunjanganPendidikan = gajiPersen * 5
elif pendidikan == "SMA":
    tunjanganPendidikan = gajiPersen * 2.5
if jamKerja > 8:
    lembur = jamKerja - 8
    gajiLembur = lembur * 3500
else:
    gajiLembur = 0

totalGaji = gaji + tunjanganJabatan + tunjanganPendidikan + gajiLembur

# tampilan hasil gaji karyawan
print("\n==============================================")
print("Karyawan yang bernama : " + str(namaKaryawan))
print("Honor yang diterima")
print("Tunjangan jabatan     : Rp.", tunjanganJabatan)
print("Tunjangan pendidikan  : Rp.", tunjanganPendidikan)
print("Honor lembur          : Rp.", gajiLembur)
print("Total gaji            : Rp.", totalGaji)
print("\n==============================================")
