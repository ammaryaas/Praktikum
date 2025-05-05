import math
import time

def cek_prima(n):
    if n <= 1:
        return False  
    batascek = int(math.sqrt(n)) + 1
    for i in range(2, batascek):  # cek prima
        if n % i == 0:
            return False
    return True

try:
    angka = int(input("Masukkan sebuah angka: "))

    mulai = time.time()
    if cek_prima(angka):
        print(f"{angka} adalah bilangan prima.")
    else:
        print(f"{angka} bukan bilangan prima.")
    selesai = time.time()

    print(f"waktu pengecekan: {selesai - mulai:.6f} detik")
except ValueError:
    print("Masukkan angka yang valid.")
