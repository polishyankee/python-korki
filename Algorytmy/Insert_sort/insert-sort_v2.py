lista = [12, 4, 3, 10, 5, 11]
n = len(lista)

j = 0 # Wybieramy konkretną wartość j

x = lista[j]
p = j
k = n
licznik_p = 0
licznik_k = 0

while k - p > 1:
    i = (p + k) // 2
    if x <= lista[i]:
        k = i
        licznik_k += 1
    else:
        p = i
        licznik_p += 1

for i in range(j, k - 1, -1):
    lista[i + 1] = lista[i]
lista[p] = x

print("Licznik_k:", licznik_k)
print("Licznik_p:", licznik_p)
print("Posortowana lista:", lista)
