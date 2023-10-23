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

przetwarzaj_plik('liczby3.txt', 'wyniki5.txt')
