wiadomosc = 'Matura'
klucz = 'trauma'
szerokosc = 5

def szyfruj(wiadomosc, klucz):
  tabela = utworzTabeleSzyfrujaca(len(klucz), wiadomosc)
  kluczSequence = sekwencjaKlucza(klucz)

  szyfrogram = "";
  for num in range(len(kluczSequence)):
    pos = kluczSequence.index(num+1)
    for row in range(len(tabela)):
      if len(tabela[row]) > pos:
        szyfrogram += tabela[row][pos]
  return szyfrogram

def utworzTabeleSzyfrujaca(szerokosc, wiadomosc):
  r = 0
  c = 0
  tabela = [[]]
  for pos, ch in enumerate(wiadomosc):
    tabela[r].append(ch)
    c += 1
    if c >= szerokosc:
      c = 0
      r += 1
      tabela.append([])

  return tabela


def sekwencjaKlucza(klucz):
  sekwencja = []
  for pos, ch in enumerate(klucz):
    poprzednieLitery = klucz[:pos]
    nowyNumer = 1
    for prevPos, prevCh in enumerate(poprzednieLitery):
      if prevCh > ch:
        sekwencja[prevPos] += 1
      else:
        nowyNumer += 1
    sekwencja.append(nowyNumer)
  return sekwencja


print(szyfruj(wiadomosc, klucz))