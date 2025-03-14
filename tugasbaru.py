print("---------------------SELAMAT DATANG---------------------")
print("**********************DAFTAR MENU***********************")
print("________________________________________________________")
print("|[ PAKET A ] Nasi Goreng | Es Teh | Harga Rp  : 50000 | ")
print("|[ PAKET B ] Ayam Bakar  | Es Teh | Harga Rp  : 45000 | ")
print("|[ PAKET C ] Ayam Kecap  | Es Teh | Harga Rp  : 40000 | ")
print("|[ PAKET D ] Ikan Bakar  | Es Teh | Harga Rp  : 30000 | ")
print("|[ PAKET E ] Ayam Goreng | Es Teh | Harga Rp  : 32000 | ")
print("|[ PAKET F ] Ayam Geprek | Es Teh | Harga Rp  : 35000 | ")
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print("MASUKAN DETAIL PEMESANAN")
nama =       input("NAMA                 : ")
no_telepon = input("NO.TELEPON           : ")
alamat = input    ("ALAMAT PENERIMA      : ")
pesanan1 =input   ("PAKET PESANAN        : ")
jumlah1 =int(input("JUMLAH PESANAN       : "))
if pesanan1 == "A":
    detail1 = ("Nasi Goreng + Es Teh = Harga Rp  : 50000 ")
    harga1 = 50000
elif pesanan1== "B":
    detail1 = ("Ayam Bakar + Es Teh = Harga Rp  : 45000")
    harga1 = 45000
elif pesanan1=="C":
    detail1 = ("Ayam Kecap + Es Teh = Harga Rp  : 40000")
    harga1 = 40000
elif pesanan1=="D":
    detail1 = ("Ikan Bakar + Es Teh  = Harga Rp  : 30000")
    harga1 = 30000
elif pesanan1=="E":
    detail1 = ("Ayam Goreng + Es Teh = Harga Rp  : 32000")
    harga1 = 32000
elif pesanan1=="F":
    detail1 = ("Ayam Geprek + Es Teh = Harga Rp  : 35000")
    harga1 = 30000
else :
    print("Pesanan tidak tersedia")

tambahan = input("apakah ada pesanan tambahan (YA/TIDAK)? ")
if tambahan == "YA":
    pesanan2 = input   ("PAKET PESANAN        : ")
    jumlah2 = int(input("JUMLAH PESANAN       : "))
    if pesanan2 == "A":
        detail2 = ("Nasi Goreng + Es Teh = Harga Rp  : 50000 ")
        harga2 = 50000
    elif pesanan2== "B":
        detail2 = ("Ayam Bakar + Es Teh = Harga Rp  : 45000")
        harga2 = 45000
    elif pesanan2=="C":
        detail2 = ("Ayam Kecap + Es Teh = Harga Rp  : 40000")
        harga2 = 40000
    elif pesanan2=="D":
        detail2 = ("Ikan Bakar + Es Teh  = Harga Rp  : 30000")
        harga2 = 30000
    elif pesanan2=="E":
        detail2 = ("Ayam Goreng + Es Teh = Harga Rp  : 32000")
        harga2 = 32000
    elif pesanan2 =="F":
        detail2 = ("Ayam Geprek + Es Teh = Harga Rp  : 35000")
        harga2 = 30000
    else :
        print("Pesanan tidak tersedia")
    
    biaya = jumlah1*harga1 + jumlah2*harga2
    pajak = int(biaya*(10/100))
    total_jumlah = jumlah1+jumlah2

    if biaya < 150000 :
        biaya_pengiriman = 25000
    else: 
        biaya_pengiriman = 0
    
    total = int(biaya+pajak+biaya_pengiriman)
    print("_____________________________________________________________________")
    print("===========================STRUK PEMESANAN===========================")
    print("_____________________________________________________________________")
    print("NAMA                     : " ,nama)
    print("NO TELEPON               : ", no_telepon)
    print("ALAMAT PENGIRIMAN        : " , alamat)
    print("DETAIL PESANAN           :  PAKET",pesanan1,detail1) 
    print("                         :  PAKET",pesanan2,detail2)
    print("JUMLAH                   : " , total_jumlah)
    print("TOTAL HARGA              : " , biaya)
    print("PAJAK(10%)               : " ,pajak)
    print("BIAYA PENGIRIMAN         : " ,biaya_pengiriman )
    print("TOTAL AKHIR              : " , total)
    print("*********************************************************************")

elif tambahan == "TIDAK" :
    print("Silahkan lakukan pemesanan ulang")

else:
    biaya = jumlah1*harga1
    pajak = int(biaya*(10/100))

    if biaya < 150000 :
        biaya_pengiriman = 25000
    elif biaya >= 150000 :
        biaya_pengiriman = 0

    total = int(biaya+pajak+biaya_pengiriman)
    print()
    print()
    print("_____________________________________________________________________")
    print("===========================STRUK PEMESANAN===========================")
    print("_____________________________________________________________________")
    print("NAMA                     : " ,nama)
    print("NO TELEPON               : ", no_telepon)
    print("ALAMAT PENGIRIMAN        : " , alamat)
    print("DETAIL PESANAN           :  PAKET",pesanan1,detail1)
    print("JUMLAH                   : " , jumlah1)
    print("TOTAL HARGA              : " , biaya)
    print("PAJAK(10%)               : " ,pajak)
    print("BIAYA PENGIRIMAN         : " ,biaya_pengiriman )
    print("TOTAL AKHIR              : " , total)
    print("*********************************************************************")