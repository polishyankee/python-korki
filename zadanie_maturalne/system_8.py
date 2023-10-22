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
