'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''

harga_awal = int(input("masukan harga awal: " ))
diskon = int(input("masukkan diskon: " ))

harga_diskon = (diskon/100) * harga_awal
harga_akhir = harga_awal - harga_diskon

print (harga_akhir)