# def liczba_blokow(n):
#     liczba_blokow = 0
#     while n > 0:
#         if n % 2 == 1:
#             liczba_blokow += 1
#         n = n // 2
#     return liczba_blokow

# # Testowanie funkcji
# n = 245
# b = liczba_blokow(n)
# print(f"Dla liczby {n} wynikiem jest {b}, ponieważ {n} w zapisie binarnym to {bin(n)[2:]}")

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

def bloki(liczba):
    if liczba == 0:
        return 1
    
    ile_blokow = 0
    cyfra_p = None
    
    while liczba != 0:
        cyfra = liczba % 2
        if cyfra != cyfra_p:
            ile_blokow += 1
        cyfra_p = cyfra
        liczba = liczba // 2
    
    return ile_blokow

# Testy
print(bloki(67))  # Wynik: 3
print(bloki(245)) # Wynik: 5


