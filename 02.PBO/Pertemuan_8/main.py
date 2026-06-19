# Custom Exception
class damageretriMinimalError(Exception):
    def __init__(self, pesan):
        super().__init__(pesan)


# Class Utama
class Damageretributionplayer:
    def __init__(self, nama, damage):
        self.nama = nama
        self.Damage = damage

    def mencet_retri(self, jumlah):
        if jumlah > self.Damage:
            raise damageretriMinimalError(
                f"Damage retribution gagal! Damage Anda hanya {self.Damage}"
            )

        self.Damage -= jumlah
        print(f"Damage retribution berhasil sebesar {jumlah}")
        print(f"Sisa damage: {self.Damage}")


# Program Utama
player = Damageretributionplayer("Daffa", 5000)

try:
    jumlah_tarik = int(input("Masukkan jumlah damage retribution: "))
    player.mencet_retri(jumlah_tarik)

except damageretriMinimalError as e:
    print("Error:", e)

except ValueError:
    print("Input harus berupa angka!")

finally:
    print("Proses pemeriksaan damage retribution telah selesai.")