# def konwertuj_na_czworowy(n):
#     wynik = ""
#     while n > 0:
#         reszta = n % 4
#         wynik = str(reszta) + wynik
#         n = n // 4
#     return wynik

# # Testowanie funkcji
# n = 85
# czworowy = konwertuj_na_czworowy(n)
# print(f"{n} w systemie czwórkowym to {czworowy}")

def konwertuj_na_czworowy(n):
    wynik = ""
    while n > 0:
        reszta = n % 4
        wynik = str(reszta) + wynik
        n = n // 4
    return wynik

def wczytaj_liczby_z_pliku(file_path):
    liczby = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            liczba = int(line.strip())
            czworowy = konwertuj_na_czworowy(liczba)
            liczby.append(czworowy)

    return liczby

# Tutaj podaj ścieżkę do swojego pliku z liczbami
file_path = 'zadanie_maturalne/liczby.txt'

# Wczytanie i konwersja liczb z pliku
liczby_w_czworowym = wczytaj_liczby_z_pliku(file_path)
print(liczby_w_czworowym)

