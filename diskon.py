#Case 11

harga = int(input("Masukan Total Harga Barang : "))
diskon = 0

if harga> 75000:
    diskon= harga * 0,5
    if diskon>50000:
        diskon = 50000

if harga > 30000 and harga<=75000:
    diskon = harga * 0,3
    if diskon>30000:
        diskon = 30000
if harga<30000:
    diskon=0
Pembayaran = harga - diskon
print(f"Diskon Yang didapatkan : {diskon} Rp")
print(f"Total Pembayaran : {Pembayaran} Rp")
