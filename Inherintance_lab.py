
class Player:
    def __init__(self, name, Role, Tingkat):
        self.name = name
        self.Role = Role
        self.Tingkat = Tingkat

    def info(self):
        print(f"Player {self.name} adalah {self.Role} dengan tingkat {self.Tingkat}.")
    def Perisai(self):
        print("Player menggunakan perisai.")
    def Pedang(self):
        print("Player menggunakan pedang.")
    
class Defender(Player):
    def jenis_defender(self):
        print("Ini adalah defender.")
    def dari_parent(self):
        super().Perisai()
    def cek_diamond_problem(self):
        print("Cek diamond problem di kelas Defender.")
        
class Attacker(Player):
    def jenis_attacker(self):
        print("Ini adalah attacker.")
    def dari_parent(self):
        super().Pedang()
    def cek_diamond_problem(self):
        print("Cek diamond problem di kelas Attacker.")
            
class DefenderAttacker(Defender, Attacker):
    def info_neutral(self):
        print("Ini adalah neutral.")

Name1 = "Andi"
Name2 = "Budi"
Name3 = "Cici"

DefenderAttacker1 = DefenderAttacker("Andi", "Defender", "Tinggi")
DefenderAttacker1.info()
DefenderAttacker1.jenis_defender()
DefenderAttacker1.jenis_attacker()
DefenderAttacker1.cek_diamond_problem()

Attacker1 = Attacker(Name2, "Offense", "Sedang")
Attacker1.info()
Attacker1.jenis_attacker()
Attacker1.cek_diamond_problem()
Attacker1.dari_parent()
Attacker1.Pedang()


Defender1 = Defender(Name3, "Tank", "Rendah")
Defender1.info()
Defender1.jenis_defender()
Defender1.cek_diamond_problem()
Defender1.dari_parent()
Defender1.Perisai()
