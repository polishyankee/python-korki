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



# liczby = []
# with open('liczby3.txt')as file:
#     lines = file.readlines()
#     for line in lines:
#         liczby.append(line.strip())
# print(liczby)

# def dziesiatkowy_na_trojkowy(liczby):
#     if liczby == 0:
#         return '0'
#     liczby_trojkowe = ''
#     while liczby != 0:
#         reszta = liczby % 3
#         liczby = liczby // 3
        
#         if reszta == 2:
#             reszta = -1
#             liczby += 1
        
#         if reszta == -1:
#             liczby_trojkowe = '-' + liczby_trojkowe
#         elif reszta == 1:
#             liczby_trojkowe = '+' + liczby_trojkowe
#         else:
#             liczby_trojkowe = '0' + liczby_trojkowe
#     return liczby_trojkowe
# # print(dziesiatkowy_na_trojkowy(liczby))



def wczytaj_liczby(nazwa_pliku):
    liczby = []
    with open(nazwa_pliku) as file:
        for line in file:
            liczby.append(line.strip())
    return liczby

def dziesiatkowy_na_trojkowy(liczba):
    if liczba == 0:
        return '0'
    liczba_trojkowa = ''
    while liczba != 0:
        reszta = liczba % 3
        liczba = liczba // 3
        
        if reszta == 2:
            reszta = -1
            liczba += 1
        
        if reszta == -1:
            liczba_trojkowa = '-' + liczba_trojkowa
        elif reszta == 1:
            liczba_trojkowa = '+' + liczba_trojkowa
        else:
            liczba_trojkowa = '0' + liczba_trojkowa
    return liczba_trojkowa

liczby = wczytaj_liczby('liczby4.txt')
liczby_trojkowe = [dziesiatkowy_na_trojkowy(liczba) for liczba in liczby]
print(liczby_trojkowe)

src="{{ asset('storage/'.$category->main_image) }}"