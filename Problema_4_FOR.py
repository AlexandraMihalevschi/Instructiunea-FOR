"""Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele impare, 
pentru intervalul de la a la b (a și b se citesc de la tastatură)."""
a=int(input("Dati numarul a: "))
b=int(input("Dati numarul b: "))
for n in range (a, b+1, 1):
    if n%2!=0:
        print(n, end=",")