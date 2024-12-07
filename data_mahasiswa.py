class DataNilaiMahasiswa:

    def __init__(self):
        # Variabel untuk menghitung statistik
        self.jumlah_sangat_memuaskan = 0
        self.jumlah_memuaskan = 0
        self.jumlah_cukup = 0
        self.total_nilai = 0
        self.total_mahasiswa = 0

    def tampilan_judul(self):
        print("Daftar Nilai-MK-Algoritma anggota kelompok kelas KJ002".center(50))

    def input_data(self):
        print("\nMasukkan Data Mahasiswa")
        no = int(input("Masukkan Nomor         : "))
        nim = input("Masukkan Nim           : ")
        nama = input("Masukkan Nama          : ")
        nilai_mk_algoritma = int(input("Masukkan Nilai         : "))

        # Validasi nilai
        if nilai_mk_algoritma < 0 or nilai_mk_algoritma > 100:
            raise ValueError("Inputkan nilai dengan benar")

        return no, nim, nama, nilai_mk_algoritma

    def proses_data(self, no, nim, nama, nilai_mk_algoritma):
        # Menentukan predikat berdasarkan nilai
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

        # Menambahkan total nilai dan jumlah mahasiswa
        self.total_nilai += nilai_mk_algoritma
        self.total_mahasiswa += 1

        # Menampilkan data mahasiswa setelah diproses
        print(f"{no}\t{nim}\t{nama}\t{nilai_mk_algoritma}\t{predikat}")

    def hitung_total_dan_rata_rata(self):
        # Menghitung total mahasiswa dan rata-rata nilai
        rata_rata = self.total_nilai / self.total_mahasiswa if self.total_mahasiswa > 0 else 0
        return rata_rata

    def tampilan_output(self):
        # Tampilan judul
        self.tampilan_judul()

        # Input dan proses data mahasiswa
        lanjut = True
        while lanjut:
            no, nim, nama, nilai_mk_algoritma = self.input_data()
            self.proses_data(no, nim, nama, nilai_mk_algoritma)
            lanjut = input("\nAda data lagi? (y/n): ").lower() == 'y'

        # Menampilkan statistik
        print("\nJumlah dengan predikat:")
        print(f'Sangat Memuaskan : {self.jumlah_sangat_memuaskan}')
        print(f'Memuaskan        : {self.jumlah_memuaskan}')
        print(f'Cukup            : {self.jumlah_cukup}')
        print(f"\nTotal Nilai      : {self.total_nilai}")
        rata_rata = self.hitung_total_dan_rata_rata()
        print(f"Rata-rata Nilai  : {rata_rata:.2f}")


# Menjalankan program
if __name__ == "__main__":
    program = DataNilaiMahasiswa()
    program.tampilan_output()