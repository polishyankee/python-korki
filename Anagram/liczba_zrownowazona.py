liczba1 = '1011010'
liczba2 = '1011010'
napisy_lol = '101010101010'
# def funkcja(liczba):
#     licznik_0 = 0 
#     licznik_1 = 0 
#     wynik = ''
#     for znak in liczba: 
#         if znak == '1' :
#             licznik_1 += 1
#         if znak == '0' :
#             licznik_0 += 1
#     roznica = licznik_1 - licznik_0
#     if roznica == 0 :
#         wynik = 'Liczba jest zrownowazona'
#     elif roznica == 1 or roznica == -1 :
#         wynik = 'Liczba jest prawie zrownowazona'
#     else :
# #    if roznica  1 or roznica  -1
#         wynik = 'Liczba jest niezrownowazona'
#     return wynik

# led = funkcja(liczba)

# print(funkcja(liczba))
# print(funkcja(liczba2))
# print(led)

def sortowanie(liczba): #to jest moj 
    liczba = list(str(liczba))
    for i in range(len(liczba)):
        for j in range(len(liczba)):
            if liczba[i] < liczba[j]:
                liczba[i],liczba[j] = liczba[j], liczba[i]
    return liczba

print(sortowanie(liczba1))
print(sortowanie(liczba2))


# def sortowanie1(liczba2):
#     liczba2 = list(str(liczba2))
#     for i in range(len(liczba2)):
#         for j in range(len(liczba2)):
#             if liczba2[i] < liczba2[j]:
#                 liczba2[i],liczba2[j] = liczba2[j], liczba2[i]
#     return liczba2
# print(sortowanie1(liczba2))

if len(liczba1) != len(liczba2):
     print('Błąd, różna długość')
if liczba1 == liczba2:
     print('To jest anagram')
else:
     print('To nie jest anagram')
