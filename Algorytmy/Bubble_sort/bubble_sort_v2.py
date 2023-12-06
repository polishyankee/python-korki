lista = [7, 3, 1, 2, 5]
size = len(lista)

print("Before sorting:", lista)

for i in range(size):
    for j in range(0, size-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
            print(lista)

print("After sorting:", lista)