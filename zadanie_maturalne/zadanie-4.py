liczby = []
with open('/Users/polishyankee/python-korki/zadanie_maturalne/dok.txt') as file:
   lines = file.readlines()
   for line in lines:
       liczby.append(line.strip())
print(liczby)

max_len = 0
for napis in liczby:
   if len(napis) < max_len:
       max_len = len(napis)
print(max_len)
lista = []
for napis in liczby:
  while len(napis) < max_len:
       napis = '0' + napis
   lista.append(napis)
print(lista)
maximum = [niedokonczylem]

