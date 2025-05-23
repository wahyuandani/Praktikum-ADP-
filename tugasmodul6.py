while True :
    print("[1] Masuk kedalam program perhitungan")
    print("[2] Keluar")
    pilihan = (int(input(" Masukkan plihan program (1-2): ")))
    if pilihan == 1 :
        n = int(input("Masukkan jumlah titik : "))
        titik=[]
        for i in range(n) :
            x = int(input(f"Masukkan x untuk titik ke-{i+1} : "))
            y = int(input(f"Masukkan y untuk titik ke-{i+1} : "))
            titik.append([x,y])
        print("Kumpulan titik dalam array 2 dimensi")
        for i in range (n):
            print(f"0{i+1} = ({titik[i][0]},{titik[i][1]})")
        print()
        for i in range(n - 1):
            for j in range (i+1, n) :
                x_1 = titik[i][0]
                y_1 = titik[i][1]
                x_2 = titik[j][0]
                y_2 = titik[j][1]
                jarak = ((x_2-x_1)**2 + (y_2-y_1)**2)**0.5
                print(f"jarak dari 0{i+1} ke 0{j+1}-> Jarak = {jarak}")
    elif pilihan == 2 :
        print("Terima Kasih")
        break
    else :
        (" Program yang anda pilih tidak tersedia,Silahkan masukan kembali")