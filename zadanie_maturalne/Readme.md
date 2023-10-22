```

def bloki(liczba):
    # Jeśli liczba jest równa 0, to zwracamy 1, ponieważ w zapisie binarnym jest to jeden blok '0'.
    if liczba == 0:
        return 1

    # Inicjalizacja licznika bloków na 0. Ten licznik będzie inkrementowany za każdym razem, gdy napotkamy nowy blok.
    ile_blokow = 0
    
    # Inicjalizacja zmiennej przechowującej poprzednią cyfrę na None. 
    # Na początku nie mamy jeszcze żadnej poprzedniej cyfry, stąd wartość None.
    cyfra_p = None
    
    # Pętla wykonuje się dopóki liczba jest różna od 0.
    while liczba != 0:
        # Obliczamy resztę z dzielenia liczby przez 2, aby uzyskać ostatni bit liczby binarnej.
        cyfra = liczba % 2
        
        # Sprawdzamy, czy obecny bit (cyfra) różni się od poprzedniego bitu (cyfra_p).
        if cyfra != cyfra_p:
            # Jeśli tak, to znaczy, że rozpoczęliśmy nowy blok, więc inkrementujemy licznik bloków.
            ile_blokow += 1
        
        # Ustawiamy cyfra_p na obecnie sprawdzaną cyfrę, aby w następnej iteracji pętli można było ją porównać z kolejnym bitem.
        cyfra_p = cyfra
        
        # Dzielimy liczbę przez 2 (używamy dzielenia całkowitego //, aby pozbyć się reszty), przesuwając się do kolejnego bitu w liczbie binarnej.
        liczba = liczba // 2
    
    # Zwracamy ostateczną liczbę bloków.
    return ile_blokow

# Testy
print(bloki(67))  # Wynik: 3
print(bloki(245)) # Wynik: 5
print(bloki(255)) # Wynik: 1
print(bloki(0))   # Wynik: 1

```