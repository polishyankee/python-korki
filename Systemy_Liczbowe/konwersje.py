
n = 311212
def konwertuj_na_dziesiatkowy(n):
    wynik = 0
    potega = 0
    while n > 0:
        cyfra = n % 10
        wynik += cyfra * (3 ** potega)
        potega += 1
        n //= 10
    return wynik
def konwertuj_na_osemkowy(wynik):
    osemkowy = ''
    while wynik > 0:
        osemkowy += str(wynik % 8),osemkowy
        wynik //= 8
    return osemkowy



print(konwertuj_na_dziesiatkowy(n))
print(konwertuj_na_osemkowy(wynik))




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


# Funkcja do konwersji liczby z jednego systemu liczbowego na drugi
def konwertuj_liczbe(liczba, podstawa_wejsciowa, podstawa_wyjsciowa):
    liczba_dziesietna = int(liczba, podstawa_wejsciowa)
    liczba_wyjsciowa = ""
    
    while liczba_dziesietna > 0:
        reszta = liczba_dziesietna % podstawa_wyjsciowa
        if reszta < 10:
            liczba_wyjsciowa = str(reszta) + liczba_wyjsciowa
        else:
            liczba_wyjsciowa = chr(ord('A') + reszta - 10) + liczba_wyjsciowa
        liczba_dziesietna //= podstawa_wyjsciowa
    
    return liczba_wyjsciowa

# Otwórz plik dane.txt i odczytaj dane
with open("dane.txt", "r") as plik:
    linie = plik.readlines()

# Przetwórz każdą linię i wykonaj konwersję
wyniki = []
for linia in linie:
    # Podziel linię na liczby i podstawy
    liczba, podstawa_wejsciowa, podstawa_wyjsciowa = map(int, linia.split())
    # Wywołaj funkcję konwertującą
    wynik = konwertuj_liczbe(str(liczba), podstawa_wejsciowa, podstawa_wyjsciowa)
    wyniki.append(wynik)

# Zapisz wyniki do pliku wynik.txt
with open("wynik.txt", "w") as plik_wynikowy:
    for wynik in wyniki:
        plik_wynikowy.write(wynik + "\n")
