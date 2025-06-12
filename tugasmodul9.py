import time
import os
from termcolor import colored

tinggi_bendera = 12
lebar_bendera = 50
lebar_tiang = 5
tambahan_tiang = 10  
gelombang = [0, 1, 2, 1, 0, -1, -2, -1]  


while True:
    for shift in range(len(gelombang)):
        os.system('cls' if os.name == 'nt' else 'clear')  

        
        for baris in range(tinggi_bendera):
            for kolom in range(lebar_tiang + lebar_bendera):
                if kolom < lebar_tiang:
                    print("|", end="") 
                else:
                   
                    geser = gelombang[(baris + shift) % len(gelombang)]
                    if kolom - lebar_tiang + geser < lebar_bendera and kolom - lebar_tiang + geser >= 0:
                        if baris < tinggi_bendera // 2:
                            print(colored(" ","red","on_red"), end="")  
                        else:
                            print(colored(" ","white","on_white"), end="")  
                    else:
                        print(" ", end="") 
            print()

       
        for _ in range(tambahan_tiang):
            print("|" * lebar_tiang)

        time.sleep(0.15)
        
