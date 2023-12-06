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
            print(f'{cyfra}:{ilosc}\n')

slownik = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
slownik_cyfr = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}

# Zliczanie cyfr szesnastkowych
zliczenia = zlicz_cyfry_szesnastkowe('liczby.txt', slownik, slownik_cyfr)

# Zapisanie wyniku do pliku
zapisz_do_pliku('wynik3.txt', zliczenia)






dane = []
with open('C:/Users/Uczeń.STANOWISKO-12/Desktop/Dane/liczby.txt') as file:
    lines = file.readlines()
    for line in lines:
        dane.append(line.strip())
slownik = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
slownik_cyfr = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,}
for i in range(len(dane)):
    wynik = ''
    liczba = dane[0]
    while liczba > 0: # w tym miejscu wywala błąd rozumiem go ale niewiem jak go poprawic
        reszta = liczba % 16
        liczba = liczba // 16
        if reszta > 9:
            wynik = slownik[reszta] + wynik
        else:
            wynik = str(reszta) + wynik
    for znak in wynik:
        slownik_cyfr[znak] += 1
    print(slownik_cyfr)


def konwertuj_na_szesnastkowy(n):
    cyfry_hex = "0123456789ABCDEF"
    wynik = ""
    while n > 0:
        reszta = n % 16
        wynik = cyfry_hex[reszta] + wynik
        n = n // 16
    return wynik

# Testowanie funkcji
n = 1679
szesnastkowy = konwertuj_na_szesnastkowy(n)
print(f"{n} w systemie szesnastkowym to {szesnastkowy}")

