"""Utilizînd ciclul FOR elaboraţi un program care afişează primele 10 numere naturale 
şi păstrarea lor în ordine descrescătoare."""
for nr in reversed(range(1, 11)):
    print(nr, end=",")