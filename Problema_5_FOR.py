"""Utilizînd ciclul FOR elaboraţi un program care să calculeze suma numerelor de la 1 la n, 
care se împart la 3 şi 5 pentru oricare n întrodus de la tastatură."""
n=int(input("Dati numarul: "))
s=0
for n in range (1, n+1, 1):
    if (n%3==0)and(n%5==0):
        s+=n
print("Suma este egala cu", s)
