class DataNilaiMahasiswa:

    def __init__(self):
        self.data_mahasiswa = [] #Menggunakan Array untuk menyimpan data
        self.jumlah_sangat_memuaskan = 0
        self.jumlah_memuaskan = 0
        self.jumlah_cukup = 0
        self.total_nilai = 0
        self.total_mahasiswa = 0

    def tampilan_judul(self):
        print("Daftar Nilai-MK-Algoritma anggota kelompok kelas KJ002".center(80))
        print("+".center(80, "+"))

    def input_data(self):
        print("\nMasukkan Data Mahasiswa")
        no = int(input("Masukkan Nomor         : "))
        nim = int(input("Masukkan Nim           : "))
        nama = input("Masukkan Nama          : ")
        nilai_mk_algoritma = int(input("Masukkan Nilai         : "))

        if nilai_mk_algoritma < 0 or nilai_mk_algoritma > 100:
            raise ValueError("Inputkan nilai antara 0-100")

        return no, nim, nama, nilai_mk_algoritma

    def proses_data(self, no, nim, nama, nilai_mk_algoritma):
        if nilai_mk_algoritma >= 88:
            predikat = "Sangat Memuaskan"
            self.jumlah_sangat_memuaskan += 1
        elif nilai_mk_algoritma >= 77:
            predikat = "Memuaskan"
            self.jumlah_memuaskan += 1
        elif nilai_mk_algoritma >= 60:
            predikat = "Cukup"
            self.jumlah_cukup += 1
        else:
            predikat = "Tidak Lulus"

        self.total_nilai += nilai_mk_algoritma
        self.total_mahasiswa += 1

        # Simpan data ke list
        self.data_mahasiswa.append((no, nim, nama, nilai_mk_algoritma, predikat))

    def hitung_total_dan_rata_rata(self):
        if self.total_mahasiswa > 0:
            return self.total_nilai / self.total_mahasiswa
        return 0

    def tampilan_output(self):
        while True:
            data = self.input_data()
            self.proses_data(*data)
            lanjut = input("\nAda data lagi? (y/n): ").lower()
            if lanjut != 'y':
                break

        self.tampilan_judul()
        print("No\tNIM\t\tNama\t\tNilaiAlgoritma\tPredikat")
        print("+" * 80)
        for mahasiswa in self.data_mahasiswa:
            print(f"{mahasiswa[0]}\t{mahasiswa[1]}\t\t{mahasiswa[2]}\t\t{mahasiswa[3]}\t{mahasiswa[4]}")

        print("\nJumlah dengan predikat:")
        print(f"Sangat Memuaskan : {self.jumlah_sangat_memuaskan}")
        print(f"Memuaskan        : {self.jumlah_memuaskan}")
        print(f"Cukup            : {self.jumlah_cukup}")
        print(f"\nTotal Nilai      : {self.total_nilai}")
        rata_rata = self.hitung_total_dan_rata_rata()
        print(f"Rata-rata Nilai  : {rata_rata}")



program = DataNilaiMahasiswa()
program.tampilan_output()
