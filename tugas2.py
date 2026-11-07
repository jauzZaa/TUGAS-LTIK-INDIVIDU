#hasna jauza salsabila | 2601734 | 1C
n = int(input("masukkan jumlah hewan yang akan diinput : "))
hewan = []

for i in range(n):
    nama = input(f"hewan ke-{i+1} : ")
    hewan.append(nama)

for i in range(len(hewan)):
    print(f"hewan ke-{i+1} adalah {hewan[i]}")
