class Dafpay:
    def __init__(self, nama, pin, saldo):
        # private attributes
        self.__nama = nama
        self.__pin = pin
        self.__saldo = saldo

    # getter
    def get_nama(self):
        return self.__nama

    def get_saldo(self, pin):
        if pin == self.__pin:
            return f"Saldo anda: Rp{self.__saldo}"
        else:
            return "PIN salah!"

    # metode validasi
    def tarik_tunai(self, jumlah, pin):
        if pin != self.__pin:
            return "PIN salah!"

        if jumlah > self.__saldo:
            return "Saldo tidak cukup!"

        self.__saldo -= jumlah
        return f"Berhasil tarik Rp{jumlah}. Sisa saldo: Rp{self.__saldo}"


#  object
akun1 = Dafpay("Daffa", "1234", 500000)

#  getter
print("Nama Pemilik:", akun1.get_nama())

print("----- CEK SALDO -----")

#  pin benar
print(akun1.get_saldo("1234"))

#  pin salah
print(akun1.get_saldo("0000"))

print("----- TARIK TUNAI -----")

#  pin benar
print(akun1.tarik_tunai(100000, "1234"))

#  pin salah
print(akun1.tarik_tunai(50000, "9999"))
