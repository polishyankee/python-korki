lista = []
with open('/Users/polishyankee/python-korki/zadanie_maturalne/dok.txt') as file:
    liczby  = file.readlines()
    for liczba in liczby:
        lista.append(int(liczba))
print(lista)
binarne = []
for i in range(len(lista)):
    binarna = ''
    while lista[i] != 0:
        reszta = lista[i] % 2
        lista[i] = lista[i] // 2
        binarna = str(reszta)+binarna
    binarne.append(binarna)
    print(binarne)

for i in binarne:
    licznik = 1
    for j in range(0,len(i)-1):
        if i[j] != i[j+1]:
            licznik = licznik + 1
    print(licznik)

# print(15 % 2)
# print (1 // 2)


