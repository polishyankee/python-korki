def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Zmienna, która optymalizuje algorytm - gdy nie nastąpi żadna zamiana, to lista jest już posortowana
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Zamiana elementów
                swapped = True
        if not swapped:
            break  # Jeśli nie było zamiany w danej iteracji, lista jest już posortowana
    return arr

# Przykład użycia:
lista_do_posortowania = [64, 34, 25, 12, 22, 11, 90]
posortowana_lista = bubble_sort(lista_do_posortowania)
print("Posortowana lista:", posortowana_lista)
