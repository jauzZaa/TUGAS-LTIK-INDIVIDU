#hasna jauza salsabila | 2601734 | 1C
n = int(input("masukkan jumlah bilangan: "))
bilangan = []

for i in range(n):
    angka = int(input(f"bilangan ke - {i+1} : "))
    bilangan.append(angka)

for angka in bilangan:
    if angka % 2 == 0:
        print(f"bilangan {angka} adalah genap")
    else:
        print(f"bilangan {angka} adalah ganjil")