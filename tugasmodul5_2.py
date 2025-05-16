nomor_mahasiswa =[]
nama_mahasiswa  =[]
nilai_mahasiswa =[]
while True :
    print("[1] Tambah Data")
    print("[2] Hapus Data")
    print("[3] Tampilkan Data")
    print("[4] Keluar")
    print()
    pilihan =int(input("Inputkan Pilihan(1-4) : "))
    if pilihan == 1 :
        no    = int(input("NOMOR MAHASISWA : "))
        nama  = (input   ("NAMA MAHASISWA  : "))
        nilai = int(input("NILAI MAHASISWA : "))
        nomor_mahasiswa.append(no)
        nama_mahasiswa.append(nama)
        nilai_mahasiswa.append(nilai)
        print("Data berhasil ditambahkan")
        print()
    elif pilihan == 2:
        no = int(input("Masukan nomor mahasiswa yang ingin dihapus : "))
        if no in nomor_mahasiswa :
                index=nomor_mahasiswa.index(no)
                nomor_mahasiswa.pop(index)
                nama_mahasiswa.pop(index)
                nilai_mahasiswa.pop(index)
                print("Data berhasil dihapus")
        else :
                print("Nomor mahasiswa tidak ditemukan ")
        print()
    elif pilihan == 3 :
        if len(nomor_mahasiswa) == 0:
            print("Belum ada data yang ditambahkan")
        else:
            gabungan = []
            for i in range(len(nomor_mahasiswa)):
                gabungan.append((nomor_mahasiswa[i], nama_mahasiswa[i], nilai_mahasiswa[i]))
            batas = len(gabungan)
            while batas > 1 :
                for i in range(batas -1) :
                    if gabungan[i][2] < gabungan[i+1][2]:
                        x = gabungan[i]
                        gabungan[i] = gabungan[i+1] 
                        gabungan[i+1] = x
                batas -=1
                print("NOMOR MAHASISWA" + "    " + "NAMA MAHASISWA" + "   " + "NILAI MAHASISWA")
            for i in range (len(gabungan)):  
                print(f"[       {gabungan[i][0]}       ][      {gabungan[i][1]}     ][       {gabungan[i][2]}      ]")
            print()
    elif pilihan == 4 :
        print("Terima Kasih ")
        break
    else :
        print("Pilihan menu tidak valid , Silahkan coba lagi")                 