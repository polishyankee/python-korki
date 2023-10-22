liczby = []
with open('/Users/polishyankee/python-korki/zadanie_maturalne/dok.txt') as file:
   lines = file.readlines()
   for line in lines:
       liczby.append(line.strip())
print(liczby)
min_len = len(liczby[0])
max_len = len(liczby[0])

for napis in liczby:
   if len(napis) > (max_len):
       max_len = len(napis)
   elif len(napis) < min_len:
       min_len = len(napis)
print(min_len)
print(max_len)

kan_max = []
kan_min = []
for napis in liczby:
   if len(napis) == max_len:
       kan_max.append(napis)
   elif len(napis) == min_len:
       kan_min.append(napis)
print(kan_max)
print(kan_min)

najwieksza = kan_max[0]
najmniejsza = kan_min[0]
for napis in kan_max:
   if napis > najwieksza:
       najwieksza = napis
for napis in kan_min:
   if napis < najmniejsza:
       najmniejsza = napis
print(najwieksza)
print(najmniejsza)