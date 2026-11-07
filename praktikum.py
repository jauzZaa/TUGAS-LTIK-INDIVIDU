#No 1
for i in range (1, 6):
    harga = 25000
    total = harga * i

print (f"total biaya pembelian: Rp", total)

#No 2 
for i in range (1, 6):
    nilai = float(input(f"masukkan nilai mahasiswa ke-{i}: "))
    total = nilai + i

    rata_rata = total/5 
print (f"rata-rata nilai mahasiswa", rata_rata)

#No 3
total_genap = 0
for i in range(0, 21, 2):
    total_genap += i 

print(f"jumlah seluruh bilangan genap", total_genap)


#No 4 
lulus = 0 
for i in range(1, 6):
    nilai = float(input(f"masukkan nilai mahasiswa ke-{i}: "))

    if (nilai >= min):
        min.append(nilai)
print (f"jumlah mahasiswa yang lulus: ", nilai)