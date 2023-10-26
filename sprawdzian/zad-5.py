def trojkowy_zrownowazonym_na_dziesietny(liczba_trojkowa):
    wartosc = 0
    potega = 1
    for cyfra in reversed(liczba_trojkowa):
        if cyfra == '+':
            wartosc += potega
        elif cyfra == '-':
            wartosc -= potega
        potega *= 3
    return wartosc

def dziesietny_na_trojkowy_zrownowazonym(liczba_dziesietna):
    if liczba_dziesietna == 0:
        return '0'
    liczba_trojkowa = ''
    while liczba_dziesietna != 0:
        reszta = liczba_dziesietna % 3
        liczba_dziesietna = liczba_dziesietna // 3
        
        if reszta == 2:
            reszta = -1
            liczba_dziesietna += 1
        
        if reszta == -1:
            liczba_trojkowa = '-' + liczba_trojkowa
        elif reszta == 1:
            liczba_trojkowa = '+' + liczba_trojkowa
        else:
            liczba_trojkowa = '0' + liczba_trojkowa
    return liczba_trojkowa    

def przetwarzaj_plik(nazwa_pliku_wejsciowego, nazwa_pliku_wyjsciowego):
    wyniki = []
    with open(nazwa_pliku_wejsciowego, 'r') as plik:
        for linia in plik:
            liczba_trojkowa = linia.strip()
            liczba_dziesietna = trojkowy_zrownowazonym_na_dziesietny(liczba_trojkowa)
            wyniki.append(liczba_dziesietna)
    
    with open(nazwa_pliku_wyjsciowego, 'w') as plik:
        for wynik in wyniki:
            plik.write(str(wynik) + '\n')
            print(str(wynik) + '\n')

przetwarzaj_plik('liczby3.txt', 'wyniki5.txt')

# print(trojkowy_zrownowazonym_na_dziesietny('+++-+'))

def przetwarzaj_plik_jeden(nazwa_pliku_wejsciowego, nazwa_pliku_wyjsciowego):
    wyniki = []
    with open(nazwa_pliku_wejsciowego, 'r') as plik:
        for linia in plik:
            liczba_dziesietna = int(linia.strip())
            liczba_trojkowa = dziesietny_na_trojkowy_zrownowazonym(liczba_dziesietna)
            wyniki.append(liczba_trojkowa)
    
    with open(nazwa_pliku_wyjsciowego, 'w') as plik:
        for wynik in wyniki:
            plik.write(wynik + '\n')
            print(wynik + '\n')

przetwarzaj_plik_jeden('liczby4.txt', 'wyniki5.txt')

