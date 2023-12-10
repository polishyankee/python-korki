def szyfr_vigenere(tekst, klucz):
    zaszyfrowany_tekst = ""
    klucz = klucz.lower()
    klucz_index = 0

    for znak in tekst:
        if znak.isalpha():  # Sprawdza, czy znak jest literą
            przesuniecie = ord(klucz[klucz_index]) - ord('a')
            zaszyfrowany_znak = chr((ord(znak.lower()) - ord('a') + przesuniecie) % 26 + ord('a'))
            if znak.isupper():
                zaszyfrowany_znak = zaszyfrowany_znak.upper()
            zaszyfrowany_tekst += zaszyfrowany_znak
            klucz_index = (klucz_index + 1) % len(klucz)  # Przejście do następnej litery klucza
        else:
            # Jeśli znak nie jest literą, dodaj go bez zmian
            zaszyfrowany_tekst += znak
    return zaszyfrowany_tekst

# Przykładowe użycie
tekst = "To jest przykładowy tekst do szyfrowania."
klucz = "klucz"
zaszyfrowany_tekst = szyfr_vigenere(tekst, klucz)
print(f"Oryginalny tekst: {tekst}")
print(f"Zaszyfrowany tekst: {zaszyfrowany_tekst}")


