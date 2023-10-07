# Funkcja do obliczania silni liczby n iteracyjnie
def oblicz_silnie_iteracyjnie(n):
    if n < 0:
        return "Nie można obliczyć silni dla liczby ujemnej."
    elif n == 0 or n == 1:
        return 1
    else:
        silnia = 1
        for i in range(2, n + 1):
            silnia *= i
        return silnia

# Wczytaj liczbę od użytkownika
try:
    liczba = int(input("Podaj liczbę, dla której chcesz obliczyć silnię: "))
    wynik = oblicz_silnie_iteracyjnie(liczba)
    print(f"Silnia z {liczba} wynosi: {wynik}")
except ValueError:
    print("Podana wartość nie jest liczbą całkowitą.")



# x = 5
# s = ""
# silnia = 1
# k = 1

# while silnia < x:
#     k = k + 1
#     silnia = silnia * k
# if silnia > x:
#     silnia = silnia // k
#     k = k - 1
# while k > 0:
#     cyfra = x // silnia 
#     s = s + str(cyfra)
#     x = x % silnia
#     silnia = silnia // k 
#     k = k - 1
# print(s)      

# ten kod jest błędny nie oblicza silni!!! Od kiedy 4! to 20 a 5! to 21 ???

# Inicjalizacja zmiennych:
# x = 164 - To jest liczba, którą będziemy konwertować.
# s = "" - To jest pusty string, w którym będziemy przechowywać cyfry reprezentacji liczby x.
# silnia = 1 - To jest zmienna, która będzie przechowywać wartość silni.
# k = 1 - To jest zmienna, która będzie używana jako mnożnik w obliczeniach silni.
# Obliczanie silni:
# W pierwszym while-loop, program zwiększa wartość k i mnoży silnia przez k tak długo, aż silnia stanie się większa lub równa x. Po zakończeniu tego pętla k będzie równa liczbie, której silnią jest wartość silnia, ale nie większą od x. Następnie, jeśli silnia jest większa niż x, silnia jest dzielona przez k i k jest zmniejszane o 1.
# Obliczanie cyfr:
# W drugim while-loop, program dzieli x przez silnia i otrzymuje cyfra, która jest dodawana do stringu s. Następnie x jest aktualizowane jako reszta z dzielenia x przez silnia. silnia jest aktualizowana jako wartość silni dla liczby mniejszej o 1 od obecnej wartości k. Proces ten powtarza się, aż k stanie się mniejsze lub równe 0.


