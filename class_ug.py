class Mahasiswa:
    def __init__(self,nama,nim,prodi):
        self._nama=nama
        self._nim=nim
        self._prodi=prodi

    def get_nama(self):
        return self._nama
    def get_nim(self):
        return self._nim
    def get_nama(self):
        return self._prodi
    
    def printinformasi(self):
        info_maha=f"===INFORMASI MAHASISWA===\nName: {self._nama}\nNim: {self._nim}\nProdi: {self._prodi}"
        return info_maha
    
    def hitungips():
        nilaiAngka = {
            "A": 4,
            "A-": 3.7,
            "B+": 3.3,
            "B":3,
            "B-": 2.7,
            "C+": 2.3,
            "C": 2,
            "D": 1,
            "E": 0
        }
        print('=== SELAMAT DATANG DI PROGRAM MENGHITUNG IPS ===')
        jumlah_matkul=int(input('Masukan jumlah matkul: '))
        total_ips=0
        total_sks=0
        for i in range(1,jumlah_matkul+1):
            input(f'Matkul-{i}: ')
            nilai_huruf=input('Masukan nilai: ')
            nilai_temp=0
            for key in nilaiAngka:
                if nilai_huruf==key:
                    nilai_temp=nilaiAngka[key]
            sks=int(input('Masukan sks: '))
            total_sks+=sks
            total_ips+=nilai_temp*sks
        total_ips=total_ips/total_sks
        hasil=f'selamat, jumlah ips Anda adalah: {total_ips:.2f}'
        return hasil



