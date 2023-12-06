# def liczba_blokow(n):
#     liczba_blokow = 0
#     while n > 0:
#         if n % 2:
#             liczba_blokow += 1
#         n = n // 2
#     return liczba_blokow
# # Testowanie funkcji
# n = 245
# b = liczba_blokow(n)
# print(f"Dla liczby {n} wynikiem jest {b}, ponieważ {n} w zapisie binarnym to {bin(n)[2:]}")

#--------------------------------

# def liczba_blokow(n):
#     liczba_blokow = 0
#     while n > 0:
#         if n % 2 == 1:
#             liczba_blokow += 1
#         n = n // 2
#     return liczba_blokow

# # Testowanie funkcji
# liczba1 = 67
# liczba2 = 245

# wynik1 = liczba_blokow(liczba1)
# wynik2 = liczba_blokow(liczba2)

# print(f"Dla liczby {liczba1} wynikiem jest {wynik1}, ponieważ {liczba1} w zapisie binarnym to {bin(liczba1)[2:]}")
# print(f"Dla liczby {liczba2} wynikiem jest {wynik2}, ponieważ {liczba2} w zapisie binarnym to {bin(liczba2)[2:]}")

#--------------------------------

# def liczba_blokow(n):
#     if n == 0:
#         return 1  # Specjalny przypadek, dla zera mamy jeden blok z jedynką
#     liczba_blokow = 0
#     while n > 0:
#         if n % 2 == 1:
#             liczba_blokow += 1
#         n = n // 2
#     return liczba_blokow

# # Testowanie funkcji
# liczba1 = 67
# liczba2 = 245

# wynik1 = liczba_blokow(liczba1)
# wynik2 = liczba_blokow(liczba2)

# print(f"Dla liczby {liczba1} wynikiem jest {wynik1}, ponieważ {liczba1} w zapisie binarnym to {bin(liczba1)[2:]}")
# print(f"Dla liczby {liczba2} wynikiem jest {wynik2}, ponieważ {liczba2} w zapisie binarnym to {bin(liczba2)[2:]}")

#--------------------------------

# def bloczek(liczba):
#     if liczba == 0:
#         return 1
    
#     ile_blokow = 0
#     cyfra_p = None
    
#     while liczba != 0:
#         cyfra = liczba % 2
#         if cyfra != cyfra_p:
#             ile_blokow += 1
#         cyfra_p = cyfra
#         liczba = liczba // 2
#     return ile_blokow

# # Testy
# print(bloczek(67))  # Wynik: 3
# print(bloczek(245)) # Wynik: 5

#--------------------------------

# def dziesietna_na_binarny(liczba):
#     if liczba == 0:
#         return "0"
#     wynik = ""
#     while liczba > 0:
#         reszta = liczba % 2
#         wynik = str(reszta) + wynik
#         liczba = liczba // 2
#     return wynik

# def licz_bloki(liczba_binarna):
#     ile_blokow = 0
#     cyfra_poprzednia = None
#     for cyfra in liczba_binarna:
#         if cyfra != cyfra_poprzednia:
#             ile_blokow += 1
#         cyfra_poprzednia = cyfra
#     return ile_blokow

# def oblicz_bloki_dla_liczb_z_pliku(nazwa_pliku_wejsciowego, nazwa_pliku_wyjsciowego):
#     with open('liczby.txt', 'r') as plik_wejsciowy, open('wynik1.txt', 'w') as plik_wyjsciowy:
#         for wiersz in plik_wejsciowy:
#             liczba = int(wiersz.strip())
#             liczba_binarna = dziesietna_na_binarny(liczba)
#             bloki = licz_bloki(liczba_binarna)
#             plik_wyjsciowy.write(f' Bloki: {bloki}\n')
#             print(f'Liczba: {liczba}, Binarnie: {liczba_binarna}, Bloki: {bloki}')

# # Przykład użycia
# oblicz_bloki_dla_liczb_z_pliku('liczby.txt', 'wyniki1.txt')

#--------------------------

# def bin_na_int(binarny):
#     dziesietny = 0
#     potega = 1
#     dlugosc = len(binarny)
#     for i in range(dlugosc - 1, -1, -1):
#         if binarny[i] == '1':
#             dziesietny += potega
#         potega *= 2
#     return dziesietny

# def znajdz_maksimum_i_minimum(nazwa_pliku):
#     maksimum = 0
#     minimum = float('inf')

#     with open(nazwa_pliku, 'r') as plik:
#         for wiersz in plik:
#             liczba = bin_na_int(wiersz.strip())
#             if liczba > maksimum:
#                 maksimum = liczba
#             if liczba < minimum:
#                 minimum = liczba
    
#     # Konwersja maksimum i minimum z powrotem na zapis binarny
#     maksimum_bin = bin(maksimum)[2:]
#     minimum_bin = bin(minimum)[2:]
    
#     return maksimum_bin, minimum_bin

# # Przykład użycia
# maksimum, minimum = znajdz_maksimum_i_minimum('bin.txt')
# print(f'Maksimum: {maksimum}')
# print(f'Minimum: {minimum}')

# with open('wyniki2.txt', 'w') as plik_wynikowy:
#     plik_wynikowy.write(f'Maksimum: {maksimum}\n')
#     plik_wynikowy.write(f'Minimum: {minimum}\n')

#--------------------------


# wynik = ""
# liczba = 456
# while liczba > 0:
#     reszta = liczba % 2
#     wynik = str(reszta) + wynik
#     liczba = liczba // 2
# print(wynik)
# print(hex(int(wynik)), oct(int(wynik))) # tu jest zmiana int na 16 i 8 

wynik = []
liczby = [4, 56, 710, 110, 404]

for liczba in liczby:
    binarna = []
    while liczba > 0:
        reszta = liczba % 2
        binarna.insert(0, reszta)
        liczba = liczba // 2
    wynik.append(binarna)

print(wynik)


