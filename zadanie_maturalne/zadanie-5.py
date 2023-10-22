lista = []
with open('/Users/polishyankee/python-korki/zadanie_maturalne/liczby.txt') as file:
   lines = file.readlines()
   for line in lines:
       lista.append(line.strip())
print(lista)
slownik = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
slownik_cyfr = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,}

def konwert_liczb(liczba_funkcji,sl,sl_c):
   wynik = ''
   system = 16
   while liczba_funkcji > 0:
      reszta = liczba_funkcji % system
      if reszta < 10:
           wynik = str(reszta) + wynik
           sl_c[str(reszta)] += 1
      else:
           wynik = sl[reszta] + wynik
           sl_c[str(sl[reszta])] += 1
      liczba_funkcji //= system
   return wynik
for liczba in lista:
   konwert_liczb(int(liczba),slownik,slownik_cyfr)
print(slownik_cyfr)