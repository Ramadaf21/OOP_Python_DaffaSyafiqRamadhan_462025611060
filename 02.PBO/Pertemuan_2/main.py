class Buff:
    def __init__(self, nama, jenis, Peningkatan):
        self.nama = nama
        self.jenis = jenis
        self.Peningkatan = Peningkatan

Buff1=Buff("Kadal","Hijau","Penambahan 10 Hybrid Damage")
Buff2=Buff("Ular Cobra","Biru","Pengurangan 30% Mana")
Buff3=Buff("Kuda Poni","Merah","Penambahan 30 Hybrid Defense")

print("Buff 1 :",Buff1.nama,Buff1.jenis,Buff1.Peningkatan)
print("Buff 2 :",Buff2.nama,Buff2.jenis,Buff2.Peningkatan)
print("Buff 3 :",Buff3.nama,Buff3.jenis,Buff3.Peningkatan)