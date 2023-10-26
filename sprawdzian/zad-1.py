def dziesietna_na_binarny(liczba):
    if liczba == 0:
        return "0"
    wynik = ""
    while liczba > 0:
        reszta = liczba % 2
        wynik = str(reszta) + wynik
        liczba = liczba // 2
    return wynik

def licz_bloki(liczba_binarna):
    ile_blokow = 0
    cyfra_poprzednia = None
    for cyfra in liczba_binarna:
        if cyfra != cyfra_poprzednia:
            ile_blokow += 1
        cyfra_poprzednia = cyfra
    return ile_blokow

def oblicz_bloki_dla_liczb_z_pliku(nazwa_pliku_wejsciowego, nazwa_pliku_wyjsciowego):
    with open('liczby.txt', 'r') as plik_wejsciowy, open('wynik1.txt', 'w') as plik_wyjsciowy:
        for wiersz in plik_wejsciowy:
            liczba = int(wiersz.strip())
            liczba_binarna = dziesietna_na_binarny(liczba)
            bloki = licz_bloki(liczba_binarna)
            plik_wyjsciowy.write(f' Bloki: {bloki}\n')
            print(f'Liczba: {liczba}, Binarnie: {liczba_binarna}, Bloki: {bloki}')

# Przykład użycia
oblicz_bloki_dla_liczb_z_pliku('liczby.txt', 'wyniki1.txt')
