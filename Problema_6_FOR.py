"""Să se calculeze sumele: 	s1=1+2+3+…+n
s2=1*2+2*3+3*4+…+(n-1)*n
s3=1+1*2+1*2*3+…+1*2*3*…*n
s4=12+22+32+…+n2
s5=1/2+2/3+3/4+…+n/(n+1)
s6=1+2+22+23+24+…+2n
Notă: Pentru fiecare sumă n – se va citi de la tastatură."""
n=int(input("Dati numarul: "))
s1=0
s2=0
s4=0
s5=0
s6=0
s3=0
fact=1
"""s2=0
s3=0
s4=0
s5=0
s6=0"""
for n in range (1,n+1):
    s1+=n
for n in range (1,n+1):
    s2+=(n-1)*n
for n in range (1,n+1):
    fact= fact * n
    s3=s3+fact
for n in range (1,n+1):
    s4+=(2*n)+10
for n in range (1,n+1):
    s5+=n/(n+1)
for n in range (1,n+1):
    s6+=2*n
print("Sumele sunt:", s1, s2, s3, s4, round(s5, 2), s6, end="            ")
