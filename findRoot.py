import math

# Panduan dalam menggunakan operator
print("=====Panduan penggunaan operator=====")
print("| Operator tambah : +               |")
print("| Operator kurang : -               |")
print("| Operator kali : *                 |")
print("| Operator bagi : /                 |")
print("| Operator pangkat : **             |")
print("| Operator akar : math.sqrt(x)      |")
print("| Operator EXP : math.exp(x)        |")
print("=====================================")

# Membuat fungsi F(x) berdasarkan persamaan yang dimasukkan oleh pengguna
def F(x_value):
    return eval(F_x_str.replace('x', str(x_value)))

# Membuat fungsi G(x) berdasarkan persamaan yang dimasukkan oleh pengguna
def g(x_value):
    return eval(G_x_str.replace('x', str(x_value)))

# Mendefinisikan persamaan F(x)
F_x_str = input("Masukkan persamaan F(x): ")

# Mendefinisikan persamaan G(x)
G_x_str = input("Masukkan persamaan G(x): ")

xiAwal = float(input("Masukkan pendekatan awal (x0): "))
e = float(input("Masukkan toleransi error (e): "))
N = int(input("Masukkan jumlah maksimum iterasi (N): "))

# Menampilkan header tabel
print("\n")
print("=" * 83)  # Garis atas tabel
print(f"{'|':<3}{'Iterasi':<10}{'|':<3}{'xi':<20}{'|':<3}{'g(xi)':<20}{'|':<3}{'f(xi)':<20}{'|':<1}")
print("=" * 83)  # Garis bawah tabel

for iterasi in range(1, N + 2):
    F_xi = F(xiAwal)
    g_xi = g(xiAwal)

    # Menampilkan nilai xi, g(xi), dan f(xi) dalam bentuk tabel dengan garis pemisah kolom
    print(f"{'|':<3}{iterasi:<10}{'|':<3}{xiAwal:<20.6f}{'|':<3}{g_xi:<20.6f}{'|':<3}{F_xi:<20.6f}{'|':<1}")
    print("-" * 83)  # Garis pemisah setiap baris

    # Jika nilai F(xi) sudah lebih kecil dari toleransi error (e),
    # maka akar yang ditemukan adalah xi
    if abs(F_xi) < e:
        xiAwal = round(xiAwal, 3)  # Bulatkan nilai xi menjadi 3 angka di belakang koma
        print(f"\nNilai x didapatkan pada saat iterasi ke - {iterasi}, dengan nilai x = {xiAwal:.2f}\n")
        break

    xiAwal = g_xi

else:
    xiAwal = round(xiAwal, 3)  # Bulatkan nilai xi menjadi 3 angka di belakang koma
    print(f"\nMaksimum jumlah iterasi telah tercapai. Nilai x = {xiAwal:.2f}\n")

