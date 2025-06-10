import os
import json

FILE_NAME = "data_keuangan.txt"

if os.path.exists(FILE_NAME):
    file = open(FILE_NAME, "r")
    data = json.load(file)
    file.close()
else:
    data = []

pilihan = ""
while pilihan != "4":
    print("=== Menu Keuangan Pribadi ===")
    print("1. Tambah data keuangan")
    print("2. Hapus data keuangan")
    print("3. Tampilkan semua data")
    print("4. Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
        keterangan = input("Masukkan keterangan: ")
        jumlah = int(input("Masukkan jumlah uang: "))
        tipe = input("Tipe (pemasukan/pengeluaran): ")

        item = {
            "tanggal": tanggal,
            "keterangan": keterangan,
            "jumlah": jumlah,
            "tipe": tipe
        }

        data.append(item)

        file = open(FILE_NAME, "w")
        json.dump(data, file, indent=4)
        file.close()

        print("Data berhasil ditambahkan!")

    elif pilihan == "2":
        if len(data) == 0:
            print("Belum ada data untuk dihapus.")
        else:
            print("\nData Keuangan:")
            i = 0
            while i < len(data):
                item = data[i]
                print(str(i + 1) + ". " + item["tanggal"] + " | " + item["keterangan"] + " | Rp" + str(item["jumlah"]) + " | " + item["tipe"])
                i += 1

            hapus = int(input("Masukkan nomor data yang ingin dihapus: ")) - 1
            if hapus >= 0 and hapus < len(data):
                del data[hapus]
                file = open(FILE_NAME, "w")
                json.dump(data, file, indent=4)
                file.close()
                print("Data berhasil dihapus!")
            else:
                print("Nomor tidak valid.")

    elif pilihan == "3":
        if len(data) == 0:
            print("Belum ada data untuk ditampilkan.")
        else:
            print("\nData Keuangan:")
            i = 0
            while i < len(data):
                item = data[i]
                print(str(i + 1) + ". " + item["tanggal"] + " | " + item["keterangan"] + " | Rp" + str(item["jumlah"]) + " | " + item["tipe"])
                i += 1

    elif pilihan == "4":
        print("Terima kasih. Program selesai.")

    else:
        print("Pilihan tidak valid. Silakan pilih kembali menu 1-4.")