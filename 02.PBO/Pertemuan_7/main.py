# Parent Class
class AlatEliminasi:
    def proses_eliminasi(self):
        print("Memproses eliminasi...")


# Child Class 1
class Pedang(AlatEliminasi):
    def proses_eliminasi(self):
        print("Eliminasi berhasil menggunakan Pedang.")


# Child Class 2
class Panah(AlatEliminasi):
    def proses_eliminasi(self):
        print("Eliminasi berhasil menggunakan Panah.")


# Fungsi Duck Typing
def jalankan_transaksi(objek):
    objek.proses_eliminasi()


# Program Utama
print("=== Demonstrasi Method Overriding ===")
Jarak_Dekat = Pedang()
Jarak_Jauh = Panah()

Jarak_Dekat.proses_eliminasi()
Jarak_Jauh.proses_eliminasi()

print("\n=== Demonstrasi Duck Typing ===")
jalankan_transaksi(Jarak_Dekat)
jalankan_transaksi(Jarak_Jauh)


# Kelas lain yang tidak mewarisi AlatEliminasi
class Sihir:
    def proses_eliminasi(self):
        print("Eliminasi berhasil menggunakan Sihir.")


sihir = Sihir()

print("\n=== Duck Typing dengan Kelas Berbeda ===")
jalankan_transaksi(sihir)