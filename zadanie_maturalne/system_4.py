def konwertuj_na_czworowy(n):
    wynik = ""
    while n > 0:
        reszta = n % 4
        wynik = str(reszta) + wynik
        n = n // 4
    return wynik

# Testowanie funkcji
n = 67
czworowy = konwertuj_na_czworowy(n)
print(f"{n} w systemie czwórkowym to {czworowy}")
