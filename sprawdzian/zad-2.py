def bin_na_int(binarny):
    dziesietny = 0
    potega = 1
    dlugosc = len(binarny)
    for i in range(dlugosc - 1, -1, -1):
        if binarny[i] == '1':
            dziesietny += potega
        potega *= 2
    return dziesietny

def znajdz_maksimum_i_minimum(nazwa_pliku):
    maksimum = 0
    minimum = float('inf')

    with open(nazwa_pliku, 'r') as plik:
        for wiersz in plik:
            liczba = bin_na_int(wiersz.strip())
            if liczba > maksimum:
                maksimum = liczba
            if liczba < minimum:
                minimum = liczba
    
    # Konwersja maksimum i minimum z powrotem na zapis binarny
    maksimum_bin = bin(maksimum)[2:]
    minimum_bin = bin(minimum)[2:]
    
    return maksimum_bin, minimum_bin

# Przykład użycia
maksimum, minimum = znajdz_maksimum_i_minimum('bin.txt')
print(f'Maksimum: {maksimum}')
print(f'Minimum: {minimum}')

with open('wyniki2.txt', 'w') as plik_wynikowy:
    plik_wynikowy.write(f'Maksimum: {maksimum}\n')
    plik_wynikowy.write(f'Minimum: {minimum}\n')