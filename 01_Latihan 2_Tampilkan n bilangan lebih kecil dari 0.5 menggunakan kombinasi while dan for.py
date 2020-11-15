#01_Latihan 2_Tampilkan n bilangan lebih kecil dari 0.5 menggunakan kombinasi while dan for
print()
import random
n=int(input('Masukkan jumlah n '))
for i in range(n):
    while 1:
        n=random.random()
        if n < 0.5:
            break
    print(n)
