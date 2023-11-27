##Case 8

##Case 6

Me = 'Hallo Gaes.. Nama saya Deni, usia saya sekarang beranjak ke 22 Tahun'
print(f"Panjang Tulisan : {len(Me)}")
print("\n")

print(f"Split Berdasarkan Space : {Me.split(' ')}")
print(f"Split Berdasarkan Koma : {Me.split(',')}")
print("\n")

print(f"Panjang Tulisan Berdasarkan Split Menggunakan Space : {len(Me.split(' '))}")
print(f"Panjang Tulisan Berdasarkan Split Menggunakan Koma : {len(Me.split(','))}")
print("\n")

print(Me.split(' ')[0])
print(f"Tipe Data : {type(Me.split(' ')[0])}")
print(Me.split(' ')[2:5])
print(f"Tipe Data : {type(Me.split(' ')[2:5])}")
print("\n")

print(Me.split(',')[1])
print(f"Tipe Data : {type(Me.split(','))}")
print("\n")

##Case 7

Me = 'Hallo Gaes.. Nama saya Deni, usia saya sekarang beranjak ke 22 Tahun'
Saya = Me.split(' ')
print(Saya)
print(f" Index -10 : {Saya[10]}")
print("\n")

print(f"Tipe Data Sebelum DiKonvert : {type(Saya[10])}")
Saya[10] = int(Saya[10])
print(f"Tipe Data Sesudah DiKonvert : {type(Saya[10])}")