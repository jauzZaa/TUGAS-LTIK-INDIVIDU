#hasna jauza salsabila | 2601734 | 1C
#pengulangan

#contoh program print dengan for
jumlah_perulangan = 5

for index in range(jumlah_perulangan):
    print(f"Print ke-{index}")

for i in range(1, 5):
    print(i)

# perulangan for dari suatu string
for i in "Hasna":
    print(f"Huruf:{i}")

#perulangan for untuk suatu list
buah = ["apel", "belimbing", "mangga", "kiwi"]
for i in buah:
    print(f"Buah:  {i}")

#perulangan for untuk suatu list dengan range
buah = ["apel", "belimbing", "mangga", "alpukat"]
for i in range (len(buah)):
    print(f"Buah:  {buah[i]}")

#studi kasus
for i in range(2, 11, 2):
    print(f"Nilai ke-{i}")

for i in range(10, 1, -1):
    print(f"Nilai ke-{i}")

#looping while
angka = 0
while(angka < 8):
    print(f"angka sekarang: {angka}")
    angka += 1

#fungsi break (untuk memhentikan suatu looping)
angka = [1, 2, 3, 4, 5]
for i in angka:
    print(i)
    if i == 3:
        break

#fungsi continue (untuk menghentikan sementara)
angka = [1, 2, 3, 4, 5]
for i in angka:
    print(i)
    if i == 3:
        continue
    print(i)

    # #fungsi range
    # for i in range[10, 0, -1]

    #fungsi nested

    #if else di loop
    
