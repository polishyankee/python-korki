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
