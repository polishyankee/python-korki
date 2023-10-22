def konwertuj_na_szesnastkowy(n):
    cyfry_hex = "0123456789ABCDEF"
    wynik = ""
    while n > 0:
        reszta = n % 16
        wynik = cyfry_hex[reszta] + wynik
        n = n // 16
    return wynik

# Testowanie funkcji
n = 1679
szesnastkowy = konwertuj_na_szesnastkowy(n)
print(f"{n} w systemie szesnastkowym to {szesnastkowy}")

