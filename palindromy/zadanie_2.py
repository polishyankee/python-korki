def is_palindrome(word):
    """Sprawdza, czy słowo jest palindromem."""
    return word == word[::-1]

def count_palindrome_families(file_path):
    """Liczy rodzin palindromów."""
    families = set()
    with open(file_path, 'r') as file:
        for word in file:
            word = word.strip()
            if is_palindrome(word):
                families.add(len(word))
    return len(families)

# Ścieżka do pliku z danymi
file_path = 'slowa.txt'

# Liczenie rodzin palindromów i zapis wyników
family_count = count_palindrome_families(file_path)
with open('wyniki2.txt', 'w') as file:
    file.write(f"Zadanie 2\n{family_count}\n")
