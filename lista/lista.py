#lista.remove(5)

# lista = [9, 8, 1, 23, 4]
# lista_p = []
# j = len(lista) # len tj. length wypisanie ilości elementów listy 
# for m in range(j):
#     min = max(lista)
#     lista.remove(min)
#     lista_p.append(min)
# print(lista_p)
# #print(j)


# Inicjalizacja zmiennych:
# lista = [9, 8, 1, 23, 4] - To jest lista liczb, którą będziemy sortować.
# lista_p = [] - To jest pusta lista, do której będziemy dodawać liczby w kolejności rosnącej.
# j = len(lista) - To jest długość listy, czyli liczba elementów w liście (w tym przypadku 5).
# Pętla główna:
# for m in range(j): - Pętla ta iteruje od 0 do długości listy - 1 (od 0 do 4 włącznie), ponieważ range(j) generuje liczby od 0 do j - 1.
# maks = min(lista) - Znajduje najmniejszą wartość w liście.
# lista.remove(maks) - Usuwa najmniejszą wartość z listy. Jeśli w liście są duplikaty tej wartości, usunie tylko pierwsze wystąpienie.
# lista_p.append(maks) - Dodaje najmniejszą wartość do listy lista_p, która przechowuje posortowane liczby.
# Wynik:
# Po wykonaniu pętli, lista_p zawiera oryginalne liczby z listy lista, ale posortowane w kolejności rosnącej.

#  -----------------------------------------------

lista = [8, 98, 12, 5]
def sortowanie_przez_wybor(dane):
    dane_posortowane = []
    while dane != []:
        liczba = max(dane)
        dane.remove(liczba)
        dane_posortowane.insert(0, liczba)
    return dane_posortowane
print(sortowanie_przez_wybor(lista))


lista = [90, 12, 2, 532, 63, 0]
def sortowanie_przez_wybory(dane):
    for i in range(len(dane)-1): # 5
        for j in range ( i + 1, len(dane)):
            if dane[j] < dane[i]:
                dane[i], dane[j] = dane[j],dane[i]
    return dane
print(sortowanie_przez_wybory(lista))
