print("             TOKO MAINAN ANAK")
print('\n       ****************************')
# input nama pembeli
nama = input('masukkan nama pembeli :')
# input kode mainan
kode = input('masukkan kode mainan :')
# input harga
harga = int(input('masukkan harga :'))
# input jumlah beli
jumlah = int(input('masukkan jumlah beli :'))
# total harga
total = harga * jumlah
# cari diskon
diskon = total / 10
# total harga diskon
totalDiskon = total - diskon

print('\n====================================')
print('Nama Pembeli         = ' + nama)
print('Kode Mainan          = ' + kode)
print('Harga                = ' + str(harga))
print('jumlah beli          = ' + str(jumlah))
print('total                = ' + str(total))
print('diskon               = ' + str(diskon))
print('total setelah diskon = ' + str(totalDiskon))
