def liczba_blokow(n):
    liczba_blokow = 0
    while n > 0:
        if n % 2 == 1:
            liczba_blokow += 1
        n = n // 2
    return liczba_blokow

# Testowanie funkcji
n = 67 
b = liczba_blokow(n)
print(f"Dla liczby {n} wynikiem jest {b}, ponieważ {n} w zapisie binarnym to {bin(n)[2:]}")
