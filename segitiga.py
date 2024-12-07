class segitiga:

    def __init__(self,baris,kolom):
        self.jumlah_baris = baris
        self.jumlah_kolom = kolom
    
    def segitiga_angka_siku(self):
        for i in range(1, self.jumlah_baris + 1):
            for j in range(1, min(i, self.jumlah_kolom) + 1):
                print(j, end=" ")
            print()
    
    def segitiga_bintang_sama_sisi(self):
        for i in range(1, self.jumlah_baris + 1):
            bintang = min(i, self.jumlah_kolom)
            print(" " * (self.jumlah_baris - i) + "* " * bintang)
    
    def segitiga_angka_atas(self):
        for i in range(self.jumlah_baris, 0, -1):
            for j in range(1, min(i, self.jumlah_kolom) + 1):
                print(j, end=" ")
            print()


input_baris = int(input("Jumlah Baris : "))
input_kolom = int(input("Jumlah Kolom : "))

Segitiga = segitiga(input_baris,input_kolom)

print("\n")
print("Segitiga Angka (Siku-siku)")
Segitiga.segitiga_angka_siku()

print("\n")
print("Segitiga Angka (Atas)")
Segitiga.segitiga_angka_atas()

print("\n")
print("Segitiga Bintang (Sama sisi)")
Segitiga.segitiga_bintang_sama_sisi()

