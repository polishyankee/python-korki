## Palindrom

### Skrypt dla Zadania 1: Liczenie Palindromów

#### Cel Skryptu:
Ten skrypt ma na celu przeliczenie liczby słów, które są palindromami, w pliku `slowa.txt`.

#### Funkcje:
1. **`is_palindrome(word)`**:
   - **Parametry**: `word` (ciąg znaków do sprawdzenia).
   - **Zwraca**: `True` jeśli słowo jest palindromem, w przeciwnym przypadku `False`.
   - **Opis**: Sprawdza, czy dane słowo jest palindromem (czytane tak samo od przodu jak i od tyłu).

2. **`count_palindromes(file_path)`**:
   - **Parametry**: `file_path` (ścieżka do pliku tekstowego).
   - **Zwraca**: Liczbę palindromów znalezionych w pliku.
   - **Opis**: Czyta plik linia po linii, usuwa białe znaki z końca każdej linii, a następnie sprawdza, czy słowo jest palindromem przy użyciu funkcji `is_palindrome`. Liczy wszystkie wystąpienia palindromów.

#### Przetwarzanie i Zapis Wyników:
- Skrypt czyta zawartość `slowa.txt`.
- Przetwarza każde słowo, by sprawdzić, czy jest palindromem.
- Zapisuje całkowitą liczbę palindromów do pliku `wyniki1.txt`.

---

### Skrypt dla Zadania 2: Liczenie Rodzin Palindromów

#### Cel Skryptu:
Liczenie liczby niepustych rodzin palindromów (grup palindromów tej samej długości) w pliku `slowa.txt`.

#### Funkcje:
1. **`is_palindrome(word)`**: (tak jak w Zadaniu 1).

2. **`count_palindrome_families(file_path)`**:
   - **Parametry**: `file_path` (ścieżka do pliku tekstowego).
   - **Zwraca**: Liczbę niepustych rodzin palindromów.
   - **Opis**: Czyta plik linia po linii, a następnie sprawdza, czy słowo jest palindromem. Jeśli tak, długość tego słowa jest dodawana do zbioru `families`. Zbiór zapewnia unikalność długości i jest używany do policzenia liczby różnych rodzin palindromów.

#### Przetwarzanie i Zapis Wyników:
- Czyta zawartość `slowa.txt`.
- Przetwarza każde słowo, by sprawdzić, czy jest palindromem i liczy różne długości palindromów.
- Zapisuje liczbę rodzin palindromów do `wyniki2.txt`.

---

### Skrypt dla Zadania 3: Zapis Rodzin Palindromów

#### Cel Skryptu:
Zapisuje każdą rodzinę palindromów w osobnym wierszu w pliku `rodziny.txt`.

#### Funkcje:
1. **`is_palindrome(word)`**: (tak jak w Zadaniu 1).

2. **`write_palindrome_families(file_path)`**:
   - **Parametry**: `file_path` (ścieżka do pliku tekstowego).
   - **Opis**: Czyta plik linia po linii i sprawdza, czy słowo jest palindromem. Jeśli tak, dodaje je do słownika `families`, gdzie kluczem jest długość słowa. Słownik przechowuje listy słów, które są palindromami o tej samej długości.

#### Przetwarzanie i Zapis Rodzin Palindromów:
- Czyta zawartość `slowa.txt`.
- Grupuje palindromy według ich długości.
- Sortuje palindromy alfabetycznie w każdej grupie.
- Zapisuje posortowane grupy palindromów do pliku `rodziny.txt`, każda rodzina w nowym wierszu.

Każdy skrypt został zaprojektowany, aby być jak najbardziej samodzielnym i spełniać ok

reślone zadanie. Wszystkie trzy skrypty korzystają z tej samej funkcji `is_palindrome` do sprawdzania, czy słowo jest palindromem.