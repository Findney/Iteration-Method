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

# Mendefinisikan fungsi metode iterasi
def metode_iterasi(F, g, x0, e, N):
    xi = x0
    iterasi = 1
    
    # Menampilkan header tabel
    print("\n")
    print(f"{'Iterasi':<10}{'xi':<20}{'g(xi)':<20}{'f(xi)':<20}")
    
    # Loop iterasi akan berjalan hingga mencapai jumlah maksimum iterasi (N)
    # atau ketika nilai fungsi F(xi) lebih kecil dari toleransi error (e)
    while iterasi <= N or F(xi) >= e:
        F_xi = F(xi)
        
        # Menampilkan nilai xi, g(xi), dan f(xi) dalam bentuk tabel
        print(f"{iterasi:<10}{xi:<20}{g(xi):<20}{F_xi:<20}")

        # Jika nilai F(xi) sudah lebih kecil dari toleransi error (e),
        # maka akar yang ditemukan adalah xi
        if F_xi < e:
                xi = round(xi, 3)  # Bulatkan nilai xi menjadi 5 angka di belakang koma
                print(f"\nNilai x didapatkan pada saat iterasi ke - {iterasi}, dengan nilai x = {xi}\n")
                return xi
        
        # Jika sudah mencapai jumlah maksimum iterasi (N),
        # maka akar yang ditemukan adalah xi
        if iterasi == N:
            xi = round(xi, 3)  # Bulatkan nilai xi menjadi 5 angka di belakang koma
            print(f"\nMaksimum jumlah iterasi telah tercapai. Nilai x = {xi}.\n")
            return xi
        
        # Lakukan iterasi baru dengan g(xi)
        xi = g(xi)

        iterasi += 1

    return xi

try: 
    # Meminta input dari pengguna
    x0 = float(input("Masukkan pendekatan awal (x0): "))
    e = float(input("Masukkan toleransi error (e): "))
    N = int(input("Masukkan jumlah maksimum iterasi (N): "))
except ValueError:
    print("Inputan tidak valid! Mohon periksa kembali inputan Anda")

# Panggil fungsi metode_iterasi untuk mencari akar
hasil_akar = metode_iterasi(F, g, x0, e, N)
