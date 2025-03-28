print("===========================RESERVASI TIKET KONSER===============================")
print("================================================================================")
print("|[       KATEGORI        ][         HARGA        ][         KETERANGAN        ]|")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("|[        VVIP           ][     Rp 2.000.000     ][        kursi : 1-30       ]|")
print("|[        VIP            ][     Rp 1.500.000     ][        kursi : 31-60      ]|")
print("|[        Reguler        ][     Rp 1.000.000     ][        kursi : 61-90      ]|")
print("|[        Ekonomi        ][     Rp 500.000       ][        kursi : 91 - 150   ]|")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("===========================TAMPILAN LAYOUT KURSI================================")
for i in range (1,100):
    print(f"[ {i : 3}  ]",end = "")
    if i%10 == 0 :
        print()
for i in range (100,151):
    print(f"[ {i : 1} ]",end = "")
    print
    if i%10 == 0 :
        print()
print()
print("================================================================================")
tiket= int(input("SILAHKAN MASUKAN JUMLAH TIKET YANG INGIN DIPESAN : "))
VVIP=0
VIP=0
Reguler=0
Ekonomi=0
kursi_terisi=" "
for i in range(1,tiket+1):
    print(f"Pemesanan ke - {i}")
    nama=      (input("MASUKAN NAMA ANDA                      : "))
    notelepon =(input("MASUKAN NO TELEPON                     : "))
    kursi= int (input("MASUKAN NO KURSI                       : "))
    pasword =  (input("MASUKAN PASWORD UNTUK MENGAKSES KONSER : "))
    if 1<=kursi<=30 :
        kategori = ("VVIP")
        harga_tiket = 2000000
        VVIP+=1
    elif 30 < kursi <= 60 :
        kategori = ("VIP")
        harga_tiket = 1500000
        VIP+=1
    elif 60 < kursi <=90 :
        kategori = ("Reguler")
        harga_tiket = 1000000
        Reguler +=1
    elif 90 < kursi <=150 :
        kategori = ("Ekonomi")
        harga_tiket = 500000
        Ekonomi +=1
    else :
        ("No kursi yang anda masukan tidak ditemukan")
    print()
    print("==================Struk Pemesanan Tiket=================")
    print("--------------------------------------------------------")
    print(f"NAMA                       : {nama}                  ")
    print(f"NO TELEPON                 : {notelepon}             ")
    print(f"NOMOR KURSI                : {kursi}                 ")
    print(f"KATEGORI                   : {kategori}              ")
    print(f"HARGA                      : {harga_tiket}           ")
    print(f"PASWORD                    : {pasword}               ")
    print("********************************************************")
    print()
    kursi_terisi+= str(kursi)+","

print("Sisa kursi perkategori : ")
sisaVVIP = 30 - VVIP
sisaVIP = 30 - VIP
sisaregular= 30 - Reguler 
sisaekonomi = 60 - Ekonomi
print(f"VVIP              :{sisaVVIP} ")
print(f"VIP               :{sisaVIP}")
print(f"Reguler           :{sisaregular}")
print(f"Ekonomi           :{sisaekonomi}")
print()
print(" TAMPILAN LAYOUT KURSI")
for j in range(1,100):
    if f",{j}," in kursi_terisi :
        print("[  0   ]",end="")
    else :
        print(f"[ {j : 3}  ]",end = "")
    if j%10 == 0 :
            print()
    
for j in range (100,151):
    if f" {j}" in kursi_terisi :
        print("[  0   ]",end="")
    else :
        print(f"[ {j : 1} ]",end = "")
    if j%10 == 0 :
        print()
    


    

