wynik = ""
liczba = 376
while liczba > 0:
    reszta = liczba % 2
    wynik = str(reszta) + wynik
    liczba = liczba // 2
print(wynik)
print(hex(int(wynik)), oct(int(wynik))) # tu jest zmiana int na 16 i 8 

