class Creep:
    def __init__(self, nama, hp):
        self.nama = nama
        self.hp = hp

    # tampil saat di-print
    def __str__(self):
        return f"{self.nama} memiliki hp {self.hp}"

    # == (sama)
    def __eq__(self, other):
        return self.hp == other.hp

    # < (lebih kecil)
    def __lt__(self, other):
        return self.hp < other.hp

    # > (lebih besar)
    def __gt__(self, other):
        return self.hp > other.hp


# ✅ 3 object
c1 = Creep("Kadal", 90)
c2 = Creep("Ular Cobra", 175)
c3 = Creep("Kuda Poni", 170)

# ✅ test __str__
print(c1)
print(c2)
print(c3)

print("----- Perbandingan -----")

# ✅ test perbandingan
print("Apakah c1 > c2?", c1 >c2)
print("Apakah c2 < c3?", c2 < c3)
print("Apakah c1 == c3?", c1 == c3)