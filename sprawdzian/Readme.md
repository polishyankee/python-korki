# Zadanie 1
---

## Wytłumaczenie Skryptu

### Funkcja `dziesietna_na_binarny(liczba: int) -> str`
Konwertuje liczbę dziesiętną na jej reprezentację binarną w postaci ciągu znaków.

- `liczba`: Liczba dziesiętna do konwersji.
- `wynik`: Zmienna akumulacyjna, do której dopisywane są kolejne bity liczby binarnej. 

Funkcja używa dzielenia liczby przez 2 i zapisywania reszty z dzielenia jako kolejnego bitu liczby binarnej. Proces ten jest powtarzany, aż liczba zostanie zredukowana do 0. Wtedy zwracany jest odwrócony ciąg znaków `wynik`, który reprezentuje liczbę w systemie binarnym.

---

### Funkcja `licz_bloki(liczba_binarna: str) -> int`
Liczy ilość bloków w liczbie binarnej.

- `liczba_binarna`: Liczba binarna w postaci ciągu znaków.
- `ile_blokow`: Zmienna licznik, przechowująca ilość bloków w liczbie binarnej.
- `cyfra_poprzednia`: Zmienna pomocnicza do przechowywania poprzedniego bitu liczby binarnej podczas iteracji.

Funkcja iteruje po każdym bicie liczby binarnej i zlicza zmiany między 0 a 1 (lub odwrotnie), traktując je jako nowe bloki.

---

### Funkcja `oblicz_bloki_dla_liczb_z_pliku(nazwa_pliku_wejsciowego: str, nazwa_pliku_wyjsciowego: str)`
Oblicza ilość bloków dla każdej liczby dziesiętnej z pliku wejściowego i zapisuje wyniki do pliku wyjściowego.

- `nazwa_pliku_wejsciowego`: Nazwa pliku z liczbami dziesiętnymi, po jednej w linii.
- `nazwa_pliku_wyjsciowego`: Nazwa pliku, do którego zapisane będą wyniki.

Funkcja otwiera plik wejściowy, czyta z niego linia po linii (traktując każdą linię jako oddzielną liczbę dziesiętną), konwertuje liczbę dziesiętną na binarną, liczy ilość bloków, a następnie zapisuje wyniki do pliku wyjściowego oraz wypisuje je na konsolę.

---

### Przykład użycia
Aby użyć tego skryptu, należy umieścić liczby dziesiętne w pliku tekstowym (np. `liczby.txt`), po jednej liczbie w linii. Następnie należy wywołać funkcję `oblicz_bloki_dla_liczb_z_pliku`, podając jako argumenty nazwy plików wejściowego i wyjściowego.

Przykład:
```python
oblicz_bloki_dla_liczb_z_pliku('liczby.txt', 'wyniki1.txt')
```

Wyniki zostaną zapisane w pliku wyjściowym (`wyniki1.txt`) oraz wypisane na konsolę.

---

# Zadanie 2

## Wytłumaczenie Kodu

### Funkcja `bin_na_int(binarny: str) -> int`
Ta funkcja konwertuje ciąg binarny na odpowiadającą mu liczbę dziesiętną. Realizuje to poprzez iterowanie po ciągu od prawej do lewej (od najmniej znaczącego bitu do najbardziej znaczącego), mnożąc wartość każdego bitu przez odpowiadającą mu potęgę dwójki.

- `dziesietny`: Zmienna, w której przechowywana jest wynikowa liczba dziesiętna.
- `potega`: Początkowo ustawiona na 1, zmienna ta jest mnożona przez 2 w każdej iteracji, reprezentując kolejne potęgi dwójki.
- `dlugosc`: Długość ciągu binarnego.

Dla każdego bitu '1' w ciągu binarnym, do zmiennej `dziesietny` dodawana jest aktualna wartość `potega`.

---

### Funkcja `znajdz_maksimum_i_minimum(nazwa_pliku: str) -> Tuple[str, str]`
Funkcja ta otwiera plik tekstowy, czyta zawarte w nim liczby binarne, a następnie znajduje i zwraca największą i najmniejszą z nich.

- `maksimum`: Zmienna przechowująca największą znalezioną liczbę. Początkowo ustawiona na 0.
- `minimum`: Zmienna przechowująca najmniejszą znalezioną liczbę. Początkowo ustawiona na nieskończoność (`float('inf')`).

Dla każdej linii w pliku, ciąg binarny konwertowany jest na liczbę dziesiętną za pomocą funkcji `bin_na_int`. Następnie liczba ta jest porównywana z aktualnymi wartościami `maksimum` i `minimum`, i jeśli jest potrzeba, te wartości są aktualizowane.

Po przeczytaniu całego pliku, wartości `maksimum` i `minimum` są konwertowane z powrotem na ciągi binarne i zwracane.

---

### Przykład użycia

1. Funkcja `znajdz_maksimum_i_minimum` jest wywoływana z nazwą pliku tekstowego jako argumentem. Plik powinien zawierać liczby binarne, każdą w nowej linii.
2. Wyniki są wypisywane na konsolę.
3. Wyniki są również zapisywane do pliku tekstowego `wyniki2.txt`, w formacie:
   ```
   Maksimum: <maksimum_bin>
   Minimum: <minimum_bin>
   ```

---

# Zadanie 3 

Skrypt jest programem w Pythonie, który konwertuje liczby dziesiętne z pliku wejściowego na ich reprezentacje w systemie szesnastkowym, zlicza wystąpienia poszczególnych cyfr szesnastkowych w tych reprezentacjach, a następnie zapisuje wyniki do pliku wyjściowego.

### Funkcja `dziesietna_na_szesnastkowy(liczba, slownik) -> str`
Funkcja ta konwertuje liczbę dziesiętną na jej reprezentację w systemie szesnastkowym.

- `liczba`: Liczba dziesiętna do konwersji.
- `slownik`: Słownik przypisujący wartościom dziesiętnym odpowiadające im litery w systemie szesnastkowym (10: 'A', 11: 'B', itd.).
- `wynik`: Zmienna, do której zapisywany jest wynik konwersji.

W pętli `while`, liczba dziesiętna jest dzielona przez 16, a reszta z dzielenia (reprezentująca cyfrę szesnastkową) jest dodawana do wyniku. Jeśli reszta jest większa niż 9, zamieniana jest na odpowiadającą jej literę za pomocą słownika `slownik`. Pętla kontynuuje działanie, dopóki `liczba` nie stanie się równa 0.

---

### Funkcja `zlicz_cyfry_szesnastkowe(nazwa_pliku_wejsciowego, slownik, slownik_cyfr) -> dict`
Funkcja ta zlicza wystąpienia poszczególnych cyfr szesnastkowych w reprezentacjach szesnastkowych liczb z pliku wejściowego.

- `nazwa_pliku_wejsciowego`: Ścieżka do pliku z liczbami dziesiętnymi.
- `slownik`: Słownik używany do konwersji liczb na system szesnastkowy.
- `slownik_cyfr`: Słownik zliczający wystąpienia poszczególnych cyfr szesnastkowych.
- `liczby`: Lista liczb dziesiętnych wczytanych z pliku.

Po wczytaniu liczb, dla każdej z nich obliczana jest jej reprezentacja szesnastkowa. Następnie, dla każdej cyfry w tej reprezentacji, zliczane jest jej wystąpienie w słowniku `slownik_cyfr`.

---

### Funkcja `zapisz_do_pliku(nazwa_pliku_wyjsciowego, dane)`
Funkcja ta zapisuje zawartość słownika do pliku wyjściowego.

- `nazwa_pliku_wyjsciowego`: Ścieżka do pliku wyjściowego.
- `dane`: Słownik z danymi do zapisania.

Dla każdej pary klucz-wartość w słowniku, linia w formacie `klucz:wartość` jest zapisywana do pliku.

---

### Przykład użycia
Na początku skryptu inicjalizowane są dwa słowniki: `slownik` do konwersji liczb na cyfry szesnastkowe i `slownik_cyfr` do zliczania wystąpień poszczególnych cyfr.

Następnie wywoływana jest funkcja `zlicz_cyfry_szesnastkowe` z odpowiednimi argumentami, a jej wyniki są zapisywane do pliku za pomocą funkcji `zapisz_do_pliku`.

```python
# Zliczanie cyfr szesnastkowych
zliczenia = zlicz_cyfry_szesnastkowe('liczby.txt', slownik, slownik_cyfr)

# Zapisanie wyniku do pliku
zapisz_do_pliku('wynik3.txt', zliczenia)
```

W pliku `liczby.txt` powinny znajdować się liczby dziesiętne, po jednej w linii. Wynikiem działania programu będzie plik `wynik3.txt

---

# Zadanie 5 

Ten skrypt Pythona konwertuje liczby zapisane w zrównoważonym systemie trójkowym na liczby dziesiętne, a następnie zapisuje wyniki do pliku.

### Funkcja `trojkowy_zrownowazonym_na_dziesietny(liczba_trojkowa) -> int`
Funkcja ta przekształca liczbę z zrównoważonego systemu trójkowego na liczbę dziesiętną.

- `liczba_trojkowa`: String reprezentujący liczbę w zrównoważonym systemie trójkowym, gdzie `+` to +1, `0` to 0, a `-` to -1.
- `wartosc`: Zmienna przechowująca wynik konwersji.
- `potega`: Zmienna przechowująca aktualną potęgę trójki.

Pętla `for` iteruje przez każdą cyfrę liczby trójkowej od końca (najmniej znaczącej cyfry). W zależności od cyfry, `wartosc` jest zwiększana lub zmniejszana o `potega`. Po każdej iteracji, `potega` jest mnożona przez 3.

---

### Funkcja `przetwarzaj_plik(nazwa_pliku_wejsciowego, nazwa_pliku_wyjsciowego)`
Funkcja ta przetwarza plik z liczbami w zrównoważonym systemie trójkowym, konwertując je na liczby dziesiętne i zapisując wyniki do innego pliku.

- `nazwa_pliku_wejsciowego`: Ścieżka do pliku wejściowego z liczbami w zrównoważonym systemie trójkowym.
- `nazwa_pliku_wyjsciowego`: Ścieżka do pliku wyjściowego, do którego zostaną zapisane wyniki.
- `wyniki`: Lista przechowująca wyniki konwersji.

Plik wejściowy jest czytany linia po linii, a każda linia jest przetwarzana przez funkcję `trojkowy_zrownowazonym_na_dziesietny`. Wyniki są zapisywane do listy `wyniki`.

Następnie, plik wyjściowy jest otwierany i każda liczba dziesiętna z listy `wyniki` jest do niego zapisywana, każda w nowej linii.

---

### Przykład użycia
Funkcja `przetwarzaj_plik` jest wywoływana z nazwami plików wejściowego i wyjściowego jako argumentami.

```python
przetwarzaj_plik('liczby3.txt', 'wyniki5.txt')
```

W pliku `liczby3.txt` powinny znajdować się liczby w zrównoważonym systemie trójkowym, po jednej w linii. Wynikiem działania programu będzie plik `wyniki5.txt`, zawierający przekonwertowane liczby w systemie dziesiętnym, również po jednej w linii.

