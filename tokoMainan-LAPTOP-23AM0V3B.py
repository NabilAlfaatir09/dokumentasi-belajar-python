print("             TOKO MAINAN ANAK")
print('\n       ****************************')
nama = input('masukkan nama pembeli :')
kode = input('masukkan kode mainan :')
harga = int(input('masukkan harga :'))
jumlah = int(input('masukkan jumlah beli :'))
total = harga * jumlah
diskon = total / 10
totalDiskon = total - diskon

print('\n====================================')
print('Nama Pembeli         = ' + nama)
print('Kode Mainan          = ' + kode)
print('Harga                = ' + str(harga))
print('jumlah beli          = ' + str(jumlah))
print('total                = ' + str(total))
print('diskon               = ' + str(diskon))
print('total setelah diskon = ' + str(totalDiskon))
