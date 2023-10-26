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
