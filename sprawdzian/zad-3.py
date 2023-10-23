def dziesietna_na_szesnastkowy(liczba, slownik):
    if liczba == 0:
        return "0"
    wynik = ""
    while liczba > 0:
        reszta = liczba % 16
        if reszta > 9:
            wynik = slownik[reszta] + wynik
        else:
            wynik = str(reszta) + wynik
        liczba = liczba // 16
    return wynik

def zlicz_cyfry_szesnastkowe(nazwa_pliku_wejsciowego, slownik, slownik_cyfr):
    with open(nazwa_pliku_wejsciowego, 'r') as plik:
        liczby = [int(line.strip()) for line in plik.readlines()]
        
    for liczba in liczby:
        reprezentacja_szesnastkowa = dziesietna_na_szesnastkowy(liczba, slownik)
        for cyfra in reprezentacja_szesnastkowa:
            slownik_cyfr[cyfra] += 1
            
    return slownik_cyfr

def zapisz_do_pliku(nazwa_pliku_wyjsciowego, dane):
    with open(nazwa_pliku_wyjsciowego, 'w') as plik:
        for cyfra, ilosc in dane.items():
            plik.write(f'{cyfra}:{ilosc}\n')

slownik = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
slownik_cyfr = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}

# Zliczanie cyfr szesnastkowych
zliczenia = zlicz_cyfry_szesnastkowe('/Users/polishyankee/python-korki/zadanie_maturalne/liczby.txt', slownik, slownik_cyfr)

# Zapisanie wyniku do pliku
zapisz_do_pliku('wynik3.txt', zliczenia)
