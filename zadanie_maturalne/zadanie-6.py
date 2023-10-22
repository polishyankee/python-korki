lista_liczb = [1,3,4,5,6,7,8,9]
liczba = 6
def wyszukiwanie_binarne(dana, lista):
    ind_str = 0
    ind_end = len(lista)-1
    while ind_str <= ind_end:
        ind_srod = (ind_str + ind_end) // 2
        if lista[ind_srod] == dana: 
            return ind_srod
        elif lista[ind_srod] > dana:
            ind_end = ind_srod - 1
        elif lista[ind_srod] < dana:
            ind_str = ind_srod + 1       
    return -1 
print(wyszukiwanie_binarne(liczba, lista_liczb))



# implementuje algorytm wyszukiwania binarnego, który jest efektywnym algorytmem do wyszukiwania elementu w posortowanej liście. Poniżej znajdziesz wyjaśnienie działania tego konkretnego kodu:

# ### Zmienne wejściowe:
# - `lista_liczb`: lista posortowanych liczb, w której będziemy szukać
# - `liczba`: liczba, którą chcemy znaleźć w liście

# ### Funkcja `wyszukiwanie_binarne(dana, lista)`:
# - `dana`: wartość, którą chcemy znaleźć w liście
# - `lista`: lista posortowanych liczb, w której będziemy szukać

# ### Przebieg funkcji:
# 1. `ind_str` ustawiamy na 0, co oznacza początek listy.
# 2. `ind_end` ustawiamy na `len(lista)-1`, co oznacza koniec listy.
# 3. Wchodzimy w pętlę `while`, która działa dopóki `ind_str` jest mniejsze lub równe `ind_end`.
# 4. W każdej iteracji pętli obliczamy `ind_srod`, który jest środkowym indeksem aktualnie rozważanego fragmentu listy.
# 5. Jeżeli element w środku (`lista[ind_srod]`) jest równy szukanej wartości (`dana`), zwracamy indeks tego elementu.
# 6. Jeżeli element w środku jest większy niż szukana wartość, oznacza to, że szukana wartość musi znajdować się w lewej części listy. Wtedy ustawiamy `ind_end` na `ind_srod - 1`.
# 7. Jeżeli element w środku jest mniejszy niż szukana wartość, oznacza to, że szukana wartość musi znajdować się w prawej części listy. Wtedy ustawiamy `ind_str` na `ind_srod + 1`.
# 8. Jeśli pętla zakończy się bez znalezienia wartości, zwracamy `-1` jako sygnał, że wartość nie znajduje się w liście.

# ### Przykładowe wykonanie:
# - Szukamy liczby 8 w liście `[1, 3, 4, 5, 6, 7, 8, 9]`.
# - Początkowo `ind_str` wynosi 0, a `ind_end` wynosi 7.
# - W pierwszej iteracji `ind_srod` wynosi 3 (środek listy), a wartość pod tym indeksem to 5. Ponieważ 5 jest mniejsze niż 8, ustawiamy `ind_str` na 4.
# - W drugiej iteracji `ind_srod` wynosi 5 (środek nowego fragmentu listy), a wartość pod tym indeksem to 7. Ponieważ 7 jest mniejsze niż 8, ustawiamy `ind_str` na 6.
# - W trzeciej iteracji `ind_srod` wynosi 6 (środek nowego fragmentu listy), a wartość pod tym indeksem to 8, co jest równa szukanej wartości. Zwracamy indeks 6.

# ### Wynik:
# - Funkcja zwraca 6, co oznacza, że liczba 8 znajduje się na 6-tym indeksie listy (indeksowanie od 0).