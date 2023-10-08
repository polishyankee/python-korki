lista = [12,4,3,10,5,11]
n = len(lista)


for j in range (n-1,-1,-1):
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
    for i in range (j, k - 1,1):
        lista[i] = lista[i + 1]
    lista[p] = x 
    print(licznik_k, licznik_p)
print(lista)

