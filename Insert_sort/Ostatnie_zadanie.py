def insertion_sort(lista):
    n = len(lista)
    for j in range(n - 1, 0, -1):
        x = lista[j]  # Element do wstawienia
        i = j + 1  # Indeks miejsca, gdzie x zostanie wstawiony

        while i < n and x < lista[i]:
            lista[i - 1] = lista[i]  # Przesuń większe elementy w prawo
            i += 1

        lista[i - 1] = x  # Wstaw x na właściwe miejsce

    return lista

# Przykład użycia
lista = [12, 4, 3, 10, 5, 11]
posortowana_lista = insertion_sort(lista)
print("Posortowana lista:", posortowana_lista)
