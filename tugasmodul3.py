print()
print("=============================================")
print("      PERHITUNGAN PROBABILITAS POISSON       ")
print("=============================================")


lamda_t = float(input("Masukan nilai lamda (λ)   : "))
m = int(input        ("Masukan nilai m           : "))
print("=============================================")
print("       HASIL PERHITUNGAN PROBABILITAS        ")
print("=============================================")
e = 2.71828
factorial = 1
for n in range (0,m+1):
    probabilitas = (e**(-lamda_t)*(lamda_t**n))/ factorial
    factorial *= (n+1)
    print((f"(P(N(t)) = {n}) adalah {probabilitas}"))
print("=============================================")