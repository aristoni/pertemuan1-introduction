##Case 12

jumlah_int = int(input("Masukkan Besar Integer Yang Di Inginkan : "))
for i in range(jumlah_int):
    for j in range(i):
        print("*", end="")
    print("")
for i in range(jumlah_int):
    for j in range(jumlah_int):
        print("*", end="")
    print("")
    jumlah_int -=1

