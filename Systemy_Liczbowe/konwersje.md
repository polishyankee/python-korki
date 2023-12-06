Poniżej znajduje się dokumentacja dla przedstawionych skryptów:

### Skrypt 1: Konwersja Liczby Trójkowej na Dziesiętną i Osemkową

#### Funkcja `konwertuj_na_dziesiatkowy`
- **Opis**: Konwertuje liczbę zapisaną w systemie trójkowym (bazie 3) na system dziesiętny.
- **Argumenty**:
  - `n` (int): Liczba w systemie trójkowym do konwersji.
- **Zwraca**:
  - int: Liczba po konwersji na system dziesiętny.

#### Funkcja `konwertuj_na_osemkowy`
- **Opis**: Konwertuje liczbę dziesiętną na system osemkowy (bazie 8).
- **Argumenty**:
  - `wynik` (int): Liczba dziesiętna do konwersji na system osemkowy.
- **Zwraca**:
  - str: Reprezentacja liczby w systemie osemkowym.

### Skrypt 2: Konwersja Liczby Trójkowej Zrównoważonej na Dziesiętną

#### Funkcja `trojkowy_zrownowazonym_na_dziesietny`
- **Opis**: Konwertuje liczbę w systemie trójkowym zrównoważonym na system dziesiętny.
- **Argumenty**:
  - `liczba_trojkowa` (str): Ciąg znaków reprezentujący liczbę w systemie trójkowym zrównoważonym.
- **Zwraca**:
  - int: Liczba po konwersji na system dziesiętny.

#### Funkcja `dziesietny_na_trojkowy_zrownowazonym`
- **Opis**: Konwertuje liczbę dziesiętną na system trójkowy zrównoważony.
- **Argumenty**:
  - `liczba_dziesietna` (int): Liczba dziesiętna do konwersji.
- **Zwraca**:
  - str: Reprezentacja liczby w systemie trójkowym zrównoważonym.

### Skrypt 3: Przetwarzanie Plików z Liczbami Trójkowymi Zrównoważonymi

#### Funkcja `przetwarzaj_plik`
- **Opis**: Czyta liczby trójkowe zrównoważone z pliku, konwertuje je na system dziesiętny i zapisuje wyniki do innego pliku.
- **Argumenty**:
  - `nazwa_pliku_wejsciowego` (str): Nazwa pliku wejściowego zawierającego liczby trójkowe zrównoważone.
  - `nazwa_pliku_wyjsciowego` (str): Nazwa pliku wyjściowego, do którego zapisywane są wyniki.

### Skrypt 4: Przetwarzanie Plików z Liczbami Dziesiętnymi na Trójkowe Zrównoważone

#### Funkcja `przetwarzaj_plik_jeden`
- **Opis**: Czyta liczby dziesiętne z pliku, konwertuje je na system trójkowy zrównoważony i zapisuje wyniki do innego pliku.
- **Argumenty**:
  - `nazwa_pliku_wejsciowego` (str): Nazwa pliku wejściowego zawierającego liczby dziesiętne.
  - `nazwa_pliku_wyjsciowego` (str): Nazwa pliku wyjściowego, do którego zapisywane są wyniki.

### Skrypt 5: Konwersja Liczby z Jednego Systemu Liczbowego na Inny

#### Funkcja `konwertuj_liczbe`
- **Opis**: Konwertuje liczbę z jednego systemu liczbowego na inny.
- **Argumenty**:
  - `liczba` (str): Liczba do konwersji.
  - `podstawa_wejsciowa` (int): Podstawa systemu liczbowego liczby wejściowej.
  - `podstawa_wyjsciowa` (int): Podstawa systemu liczbowego na który ma być przek

onwertowana liczba.
- **Zwraca**:
  - str: Liczba po konwersji na nowy system liczbowy.

#### Przykład Użycia:
```python
with open("dane.txt", "r") as plik:
    linie = plik.readlines()

wyniki = []
for linia in linie:
    liczba, podstawa_wejsciowa, podstawa_wyjsciowa = map(int, linia.split())
    wynik = konwertuj_liczbe(str(liczba), podstawa_wejsciowa, podstawa_wyjsciowa)
    wyniki.append(wynik)

with open("wynik.txt", "w") as plik_wynikowy:
    for wynik in wyniki:
        plik_wynikowy.write(wynik + "\n")
```

Te skrypty umożliwiają konwersję liczb między różnymi systemami liczbowymi oraz przetwarzanie danych z plików tekstowych.