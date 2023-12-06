# Przegląd podstawowych algorytmów


## Bubblesort (sortowanie bąbelkowe)

Sortowanie bąbelkowe jest to jeden z najprostszych algorytmów sortowania. Warty poznania, jednak ze względu na dużą złożoność nie wykorzystywany w kodzie produkcyjnym. Sortowanie to polega na przejściu po tablicy poprzez porównywanie dwóch kolejnych elementów i za każdym razem sprawdzanie czy elementy są w poprawnej kolejności. Jeżeli elementy nie będą w dobrej kolejności zostaną zamienione. Operację tę wykonuje się dotąd, aż cały zbiór nie będzie posortowany.

```
lista = [7, 3, 1, 2, 5]
size = len(lista)

print("Before sorting:", lista)

for i in range(size):
    for j in range(0, size-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
            print(lista)

print("After sorting:", lista)
```

**Wyjaśnienie:**
Bubble Sort to prosty algorytm sortowania, który wielokrotnie przechodzi przez listę, porównując sąsiednie elementy i zamieniając je miejscami, jeśli są w złej kolejności. Proces ten powtarza się aż do momentu, kiedy nie będzie potrzeby żadnej zamiany, co oznacza, że lista jest posortowana.

### 2. Quicksort

**Kod:**

```python
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)

# Przykład użycia
arr = [10, 7, 8, 9, 1, 5]
quicksort(arr, 0, len(arr)-1)
print("Posortowana tablica:", arr)
```

**Wyjaśnienie:**
Quicksort to szybki algorytm sortowania, który korzysta z techniki 'dzieli i rządź'. Wybiera element zwany pivot i umieszcza elementy mniejsze od pivotu po jego lewej stronie, a większe po prawej. Proces ten jest powtarzany rekursywnie dla mniejszych list.

### 3. Insertion Sort

**Kod:**

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Przykład użycia
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Posortowana tablica:", arr)
```

**Wyjaśnienie:**
Insertion Sort to prosty algorytm sortowania, który buduje posortowaną listę jeden element na raz, biorąc każdy kolejny element i umieszczając go we właściwym miejscu względem już posortowanej części listy.

### 4. Selection Sort

**Kod:**

```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Przykład użycia
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Posortowana tablica:", arr)
```

**Wyjaśnienie:**
Selection Sort to algorytm sortowania, który na każdym kroku wyszukuje najmniejszy (lub największy, w zależności od porządku sortowania) element z nieposortowanej części listy i zamienia go z pierwszym elementem tej części. Proces ten jest powtarzany aż do posortowania całej listy. 

Te algorytmy to klasyki w nauce programowania i są świetnym punktem wyjścia do zrozumienia podstawowych koncepcji algorytmów sortowania.