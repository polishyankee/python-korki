# def is_palindrome(word):
#     """Sprawdza, czy słowo jest palindromem."""
#     return word == word[::-1]

# def count_palindromes(file_path):
#     """Liczy palindromy w pliku."""
#     count = 0
#     with open(file_path, 'r') as file:
#         for word in file:
#             if is_palindrome(word.strip()):
#                 count += 1
#     return count

# # Ścieżka do pliku z danymi
# file_path = 'slowa.txt'

# # Liczenie palindromów i zapis wyników
# palindrome_count = count_palindromes(file_path)
# print(palindrome_count)
# with open('wyniki1.txt', 'w') as file:
#     file.write(f"Zadanie 1\n{palindrome_count}\n")

def count_palindromes(file_path):
    """Liczy palindromy w pliku."""
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            if word == word[::-1]:  # Sprawdzenie palindromu bez dodatkowej funkcji
                count += 1
    return count

# Ścieżka do pliku z danymi
file_path = 'slowa.txt'
# Liczenie palindromów i wypisanie wyniku
palindrome_count = count_palindromes(file_path)
print(palindrome_count)

