def is_palindrome(word):
    """Sprawdza, czy słowo jest palindromem."""
    return word == word[::-1]

def process_palindromes(file_path):
    """Przetwarza plik, znajdując i grupując palindromy."""
    palindromes = {}  # Słownik do grupowania palindromów według ich długości

    # Liczenie palindromów
    palindrome_count = 0
    with open(file_path, 'r') as file:
        for word in file:
            word = word.strip()  # Usuwa znaki końca linii
            if is_palindrome(word):
                palindrome_count += 1
                word_length = len(word)
                if word_length not in palindromes:
                    palindromes[word_length] = []
                palindromes[word_length].append(word)

    # Sortowanie palindromów w każdej grupie
    for length in palindromes:
        palindromes[length].sort()

    return palindrome_count, palindromes

# Ścieżka do pliku z danymi
file_path = 'slowa.txt'

# Przetwarzanie palindromów
palindrome_count, palindromes = process_palindromes(file_path)

# Zapis wyników do wyniki.txt
with open('wyniki.txt', 'w') as file:
    file.write(f"Zadanie 1\n{palindrome_count}\n")
    file.write(f"Zadanie 2\n{len(palindromes)}\n")

# Zapis rodzin palindromów do rodziny.txt
with open('rodziny.txt', 'w') as file:
    for length in sorted(palindromes):
        file.write(" ".join(palindromes[length]) + "\n")
