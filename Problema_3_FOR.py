"""Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele pare, 
pentru intervalul de la 1 la n (n-este citit de la tastatură)."""
n=int(input("Dati numarul: "))
for n in range (1, n+1, 1):
    if n%2==0:
        print(n, end=",")
