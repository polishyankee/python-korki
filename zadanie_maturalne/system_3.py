def konwertuj_na_trojkowy(n):
    wynik = ""
    while n > 0:
        reszta = n % 3
        wynik = str(reszta) + wynik
        n = n // 3
    return wynik

# Testowanie funkcji
n = 67
trojkowy = konwertuj_na_trojkowy(n)
print(f"{n} w systemie trójkowym to {trojkowy}")


