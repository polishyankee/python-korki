napis1 = 'matura'
napis2 = 'trauma'

def sortowanie(napis):
     napis = list(napis)
     for i in range(len(napis)):
         for j in range(len(napis)):
             if napis[i] < napis[j]:
                 napis[i],napis[j] = napis[j], napis[i]
     return napis
print(sortowanie(napis1))
print(sortowanie(napis2))
 
napis1_p = sortowanie(napis1)
napis2_p = sortowanie(napis2)

if len(napis1) != len(napis2):
     print('Błąd, różna długość')
if napis1_p == napis2_p:
     print('To jest anagram')
else:
     print('To nie jest anagram')

