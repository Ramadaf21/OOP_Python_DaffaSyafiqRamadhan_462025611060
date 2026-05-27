class Creep:
    # attributes default
    nama = ""
    jenis = ""
    peningkatan = ""
    map = ""

    # Instance method
    def tampilkan(self):
        print("Creep", self.nama, "jenis", self.jenis)

    def buff(self):
        print("Creep", self.nama, "memberi buff", self.peningkatan)

    def lokasi(self):
        print("Creep", self.nama, "terletak di", self.map)

    # Static method
    @staticmethod
    def info():
        print("Creep adalah monster yang memberi buff")


# ✅ Object (dibuat kosong dulu)
c1 = Creep()
c2 = Creep()

# isi manual
c1.nama = "Kadal"
c1.jenis = "Hijau"
c1.peningkatan = "+10 Attack"
c1.map = "Elf Forest"

c2.nama = "Serigala"
c2.jenis = "Abu"
c2.peningkatan = "+5 Speed"
c2.map = "Dark Woods"

# ✅ Pemanggilan
Creep.info()

c1.tampilkan()
c1.buff()
c1.lokasi()

c2.tampilkan()
c2.buff()
c2.lokasi()