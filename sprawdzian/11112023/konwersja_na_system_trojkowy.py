# def konwersja_na_trojkowy(liczby):
#     liczby_trojkowe = []

#     for liczba in liczby:
#             wynik = ''
#             while liczba > 0:
#                 wynik = str(liczba % 3) + wynik
#                 liczba //= 3
#             liczby_trojkowe.append(wynik)

#     return liczby_trojkowe

# # Example usage
# liczby_dziesiętne = [5, 10, 15, 20]
# liczby_trojkowe = konwersja_na_trojkowy(liczby_dziesiętne)

# print(f"{liczby_dziesiętne}w systemie trojkowym to {liczby_trojkowe}")



def konwertuj_na_trojkowy(n):
    liczby_troj = []
    for i in n:
        wynik = ''
        while i > 0:
            reszta = i % 3
            wynik = str(reszta) + wynik
            i //= 3
        liczby_troj.append(wynik)
    return liczby_troj

lista = [94,23,12,67,14,456]
system_troj = konwertuj_na_trojkowy(lista)
print(system_troj)