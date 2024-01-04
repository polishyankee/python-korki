def is_palindrome(word):
    """Sprawdza, czy słowo jest palindromem."""
    return word == word[::-1]

def write_palindrome_families(file_path):
    """Zapisuje rodziny palindromów do pliku."""
    families = {}
    with open(file_path, 'r') as file:
        for word in file:
            word = word.strip()
            if is_palindrome(word):
                word_length = len(word)
                if word_length not in families:
                    families[word_length] = []
                families[word_length].append(word)

    # Sortowanie każdej rodziny
    for length in families:
        families[length].sort()

    with open('rodziny.txt', 'w') as file:
        for length in sorted(families):
            file.write(" ".join(families[length]) + "\n")

# Ścieżka do pliku z danymi
file_path = 'slowa.txt'

# Zapis rodzin palindromów
write_palindrome_families(file_path)
