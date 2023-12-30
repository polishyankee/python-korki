def encrypt_columnar_cipher(text, key):
    # Usuwamy spacje z tekstu
    text = text.replace(" ", "")

    # Tworzymy słownik do przechowywania kolumn
    columns = {k: [] for k in range(key)}

    # Dodajemy znaki do odpowiednich kolumn
    for i, char in enumerate(text):
        column = i % key
        columns[column].append(char)

    # Łączymy kolumny w zaszyfrowany tekst
    encrypted_text = ''
    for column in range(key):
        encrypted_text += ''.join(columns[column])

    return encrypted_text

def decrypt_columnar_cipher(encrypted_text, key):
    # Obliczamy długość oryginalnego tekstu
    length = len(encrypted_text)

    # Obliczamy ilość wierszy
    rows = length // key

    # Tworzymy słownik do przechowywania kolumn
    columns = {k: [] for k in range(key)}

    # Wypełniamy kolumny
    index = 0
    for column in range(key):
        for _ in range(rows):
            columns[column].append(encrypted_text[index])
            index += 1

    # Odczytujemy tekst poziomo
    decrypted_text = ''
    for row in range(rows):
        for column in range(key):
            decrypted_text += columns[column][row]

    return decrypted_text

# Przykład użycia
text = "Matura"
key = 3

encrypted = encrypt_columnar_cipher(text, key)
decrypted = decrypt_columnar_cipher(encrypted, key)

print("Tekst oryginalny:", text)
print("Tekst zaszyfrowany:", encrypted)
print("Tekst odszyfrowany:", decrypted)
