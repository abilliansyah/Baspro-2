def hitung_gaji(status, golongan):
    gaji_tetap = 1_000_000
    gaji_honor = 750_000
    bonus = {"A": 200_000, "B": 400_000, "C": 550_000}
    bonus_honor = {"A": 150_000, "B": 275_000, "C": 480_000}

    if status == "Tetap":
        gaji = gaji_tetap
        bonus_golongan = bonus.get(golongan, 0)
    else:  
        gaji = gaji_honor
        bonus_golongan = bonus_honor.get(golongan, 0)

    total_gaji = gaji + bonus_golongan
    return gaji, bonus_golongan, total_gaji

nama = input("Masukkan Nama Pegawai: ").strip()
nik = input("Masukkan NIK Pegawai: ").strip()

while not nik.isdigit():
    print("NIK harus berupa angka! Silakan masukkan kembali.")
    nik = input("Masukkan NIK Pegawai: ").strip()
nik = int(nik)

while True:
    status = input("Pegawai Tetap/Honor: ").strip().capitalize()
    if status in ["Tetap", "Honor"]:
        break
    print("Status harus 'Tetap' atau 'Honor'!")

while True:
    golongan = input("Pilih Golongan A/B/C: ").strip().upper()
    if golongan in ["A", "B", "C"]:
        break
    print("Golongan harus 'A', 'B', atau 'C'!")

gaji, bonus, total_gaji = hitung_gaji(status, golongan)

print("\n=== DATA PEGAWAI ===")
print(f"Nama Pegawai   : {nama}")
print(f"NIK Pegawai    : {nik}")
print(f"Status Pegawai : {status}")
print(f"Golongan       : {golongan}")
print(f"Gaji Pokok     : Rp{gaji:,}")
print(f"Bonus          : Rp{bonus:,}")
print(f"Total Gaji     : Rp{total_gaji:,}")
