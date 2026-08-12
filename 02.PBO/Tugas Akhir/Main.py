
# ============================================================
# FINAL PROJECT OOP
# RPG BATTLE ARENA
# ============================================================


# ============================================================
# CUSTOM EXCEPTION
# ============================================================

class DamageRetriError(Exception):
    """Custom Exception untuk Damage Retribution."""
    def __init__(self, pesan):
        super().__init__(pesan)


# ============================================================
# PARENT CLASS - PLAYER
# ============================================================

class Player:

    # Magic Method
    def __init__(self, nama, hp, damage):
        # Encapsulation menggunakan private attribute
        self.__nama = nama
        self.__hp = hp
        self.__damage = damage

    # Magic Method
    def __str__(self):
        return (
            f"{self.__nama} | "
            f"HP: {self.__hp} | "
            f"Damage: {self.__damage}"
        )

    # =========================
    # GETTER
    # =========================

    def get_nama(self):
        return self.__nama

    def get_hp(self):
        return self.__hp

    def get_damage(self):
        return self.__damage

    # =========================
    # SETTER
    # =========================

    def set_hp(self, hp_baru):
        if hp_baru < 0:
            self.__hp = 0
        else:
            self.__hp = hp_baru

    def set_damage(self, damage_baru):
        if damage_baru > 0:
            self.__damage = damage_baru

    # =========================
    # INSTANCE METHOD
    # =========================

    def attack(self, musuh):
        """Menyerang player lain."""

        if self.__hp <= 0:
            print(f"{self.__nama} sudah kalah dan tidak dapat menyerang.")
            return

        musuh.set_hp(musuh.get_hp() - self.__damage)

        print(
            f"{self.__nama} menyerang "
            f"{musuh.get_nama()} sebesar "
            f"{self.__damage} damage!"
        )

        if musuh.get_hp() <= 0:
            print(f"{musuh.get_nama()} telah dikalahkan!")

    def info(self):
        print(f"Nama   : {self.__nama}")
        print(f"HP     : {self.__hp}")
        print(f"Damage : {self.__damage}")

    # =========================
    # STATIC METHOD
    # =========================

    @staticmethod
    def validasi_damage(damage):
        """
        Static Method untuk memvalidasi nilai damage.
        Tidak membutuhkan object/self.
        """

        if damage <= 0:
            return False

        return True

    # =========================
    # DAMAGE RETRIBUTION
    # =========================

    def damage_retribution(self, jumlah):

        if jumlah <= 0:
            raise DamageRetriError(
                "Damage retribution harus lebih dari 0!"
            )

        if jumlah > self.__damage:
            raise DamageRetriError(
                f"Damage retribution gagal! "
                f"Damage yang dimiliki hanya {self.__damage}"
            )

        self.__damage -= jumlah

        print(
            f"{self.__nama} menggunakan Damage Retribution "
            f"sebesar {jumlah}."
        )

        print(f"Sisa Damage: {self.__damage}")


# ============================================================
# INHERITANCE - DEFENDER
# ============================================================

class Defender(Player):

    def __init__(self, nama, hp, damage):
        super().__init__(nama, hp, damage)

    def jenis_defender(self):
        print(f"{self.get_nama()} adalah Defender.")

    def gunakan_perisai(self):
        print(
            f"{self.get_nama()} menggunakan perisai "
            f"untuk bertahan!"
        )


# ============================================================
# INHERITANCE - ATTACKER
# ============================================================

class Attacker(Player):

    def __init__(self, nama, hp, damage):
        super().__init__(nama, hp, damage)

    def jenis_attacker(self):
        print(f"{self.get_nama()} adalah Attacker.")

    def gunakan_pedang(self):
        print(
            f"{self.get_nama()} menggunakan pedang "
            f"untuk menyerang!"
        )


# ============================================================
# MULTIPLE INHERITANCE
# ============================================================

class HybridPlayer(Defender, Attacker):

    def __init__(self, nama, hp, damage):
        super().__init__(nama, hp, damage)

    def info_role(self):
        print(
            f"{self.get_nama()} adalah Hybrid Player "
            f"(Defender + Attacker)."
        )


# ============================================================
# PARENT CLASS ALAT ELIMINASI
# ============================================================

class AlatEliminasi:

    def proses_eliminasi(self, player):
        print(
            f"{player.get_nama()} menggunakan alat eliminasi."
        )


# ============================================================
# POLYMORPHISM - PEDANG
# ============================================================

class Pedang(AlatEliminasi):

    # Method Overriding
    def proses_eliminasi(self, player):
        print(
            f"{player.get_nama()} menyerang menggunakan PEDANG!"
        )


# ============================================================
# POLYMORPHISM - PANAH
# ============================================================

class Panah(AlatEliminasi):

    # Method Overriding
    def proses_eliminasi(self, player):
        print(
            f"{player.get_nama()} menyerang menggunakan PANAH!"
        )


# ============================================================
# POLYMORPHISM - SIHIR
# ============================================================

class Sihir:

    # Tidak mewarisi AlatEliminasi
    # Tetapi mempunyai method dengan nama yang sama

    def proses_eliminasi(self, player):
        print(
            f"{player.get_nama()} menyerang menggunakan SIHIR!"
        )


# ============================================================
# DUCK TYPING
# ============================================================

def jalankan_eliminasi(alat, player):
    """
    Duck Typing.

    Fungsi tidak peduli alat berasal dari class apa.
    Yang penting objek tersebut memiliki
    method proses_eliminasi().
    """

    alat.proses_eliminasi(player)


# ============================================================
# FUNGSI MEMBUAT PLAYER
# ============================================================

def pilih_player():

    print("\n=== PILIH ROLE PLAYER ===")
    print("1. Defender")
    print("2. Attacker")
    print("3. Hybrid")

    pilihan = input("Pilih role: ")

    nama = input("Masukkan nama player: ")

    hp = 100
    damage = 20

    if pilihan == "1":

        player = Defender(
            nama,
            hp,
            damage
        )

    elif pilihan == "2":

        player = Attacker(
            nama,
            hp,
            damage
        )

    elif pilihan == "3":

        player = HybridPlayer(
            nama,
            hp,
            damage
        )

    else:
        print("Pilihan role tidak valid.")

        player = Player(
            nama,
            hp,
            damage
        )

    return player


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("=" * 50)
    print("       RPG BATTLE ARENA")
    print("       FINAL PROJECT OOP")
    print("=" * 50)

    # Membuat player
    player = pilih_player()

    # Membuat musuh
    musuh = Player(
        "Goblin",
        100,
        15
    )

    while True:

        print("\n" + "=" * 50)
        print("MENU UTAMA")
        print("=" * 50)

        print("1. Lihat Status")
        print("2. Serang Musuh")
        print("3. Damage Retribution")
        print("4. Gunakan Alat Eliminasi")
        print("5. Validasi Damage")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        # ================================================
        # STATUS
        # ================================================

        if pilihan == "1":

            print("\n=== STATUS PLAYER ===")
            print(player)

            print("\n=== STATUS MUSUH ===")
            print(musuh)

        # ================================================
        # ATTACK
        # ================================================

        elif pilihan == "2":

            if musuh.get_hp() <= 0:

                print(
                    f"{musuh.get_nama()} sudah kalah!"
                )

            else:

                player.attack(musuh)

        # ================================================
        # DAMAGE RETRIBUTION
        # ================================================

        elif pilihan == "3":

            try:

                jumlah = int(
                    input(
                        "Masukkan jumlah Damage Retribution: "
                    )
                )

                player.damage_retribution(jumlah)

            except DamageRetriError as e:

                print("Custom Error:", e)

            except ValueError:

                print(
                    "Error: Input harus berupa angka!"
                )

            finally:

                print(
                    "Proses Damage Retribution selesai."
                )

        # ================================================
        # ALAT ELIMINASI
        # ================================================

        elif pilihan == "4":

            print("\n=== PILIH ALAT ELIMINASI ===")

            print("1. Pedang")
            print("2. Panah")
            print("3. Sihir")

            alat_pilihan = input(
                "Pilih alat: "
            )

            if alat_pilihan == "1":

                alat = Pedang()

            elif alat_pilihan == "2":

                alat = Panah()

            elif alat_pilihan == "3":

                alat = Sihir()

            else:

                print("Pilihan tidak valid.")
                continue

            # Polymorphism + Duck Typing
            jalankan_eliminasi(
                alat,
                player
            )

        # ================================================
        # STATIC METHOD
        # ================================================

        elif pilihan == "5":

            try:

                damage = int(
                    input(
                        "Masukkan nilai damage: "
                    )
                )

                if Player.validasi_damage(damage):

                    print(
                        "Damage valid!"
                    )

                else:

                    print(
                        "Damage tidak valid!"
                    )

            except ValueError:

                print(
                    "Input harus berupa angka!"
                )

        # ================================================
        # EXIT
        # ================================================

        elif pilihan == "6":

            print(
                "\nTerima kasih telah bermain!"
            )

            break

        else:

            print(
                "Pilihan menu tidak tersedia."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
