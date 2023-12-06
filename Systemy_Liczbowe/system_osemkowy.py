def trojkowy_na_dziesietny(trojkowy):
    wynik = 0
    potega = 0
    while trojkowy > 0:
        cyfra = trojkowy % 10
        wynik += cyfra * (3 ** potega)
        potega += 1
        trojkowy //= 10
    return wynik

def dziesietny_na_osemkowy(dziesietny):
    osemkowy = ""
    while dziesietny > 0:
        osemkowy = str(dziesietny % 8) + osemkowy
        dziesietny //= 8
    return osemkowy

# Przykładowe użycie
n = 311212  # Przykładowa liczba w systemie trójkowym
liczba_dziesietna = trojkowy_na_dziesietny(n)
liczba_osemkowa = dziesietny_na_osemkowy(liczba_dziesietna)

print("Liczba trójkowa:", n)
print("Liczba ósemkowa:", liczba_osemkowa)
print(liczba_dziesietna)


########################

def konwertuj_na_osemkowy(n):
    wynik = ""
    while n > 0:
        reszta = n % 8
        wynik = str(reszta) + wynik
        n = n // 8
    return wynik

# Testowanie funkcji
n = 1679
osemkowy = konwertuj_na_osemkowy(n)
print(f"{n} w systemie ósemkowym to {osemkowy}")



def binarny_na_dziesietny(binarny):
    dziesietny = 0
    potega = 0
    while binarny > 0:
        cyfra = binarny % 10
        dziesietny += cyfra * (2 ** potega)
        potega += 1
        binarny //= 10
    return dziesietny

def dziesietny_na_trojkowy(dziesietny):
    trojkowy = ""
    while dziesietny > 0:
        trojkowy = str(dziesietny % 3) + trojkowy
        dziesietny //= 3
    return trojkowy

# Przykładowe użycie
liczba_binarna = 111010  # Przykładowa liczba binarna
liczba_dziesietna = binarny_na_dziesietny(liczba_binarna)
liczba_trojkowa = dziesietny_na_trojkowy(liczba_dziesietna)

print("Liczba dziesiętna:", liczba_dziesietna)
print("Liczba trójkowa:", liczba_trojkowa)
