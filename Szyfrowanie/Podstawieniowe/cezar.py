# def szyfruj(napis, klucz): # napis — zmienna przechowująca tekst do zaszyfrowania

#     szyfrogram = "" # zmienna przechowująca zaszyfrowany napis
#     for i in napis: # przegląd kolejnych liter tekstu jawnego
#         litera = klucz + ord(i) # (*) w postaci kodu ASCII
#         if litera > ord('z'): # (**) jeśli wyjdziemy poza alfabet z prawej strony (klucz o wartości dodatniej)
#             litera -= 26
#         elif litera < ord('a'):  #  (***) jeśli wyjdziemy poza alfabet z lewej strony (klucz o wartości ujemnej)
#             litera += 26

#         szyfrogram += chr(litera) # dokładamy kolejne litery do wyniku, konwertując ASCII na znak

#     return szyfrogram

# # część główna programu

# napis = 'abcd'
# klucz = 10

# # szyfrowanie
# szyfrogram = szyfruj(napis, klucz) # cdezab
# print(szyfrogram)
# # deszyfrowanie
# napis = szyfruj(szyfrogram, -klucz)
# print(napis) # abcxyz


# def encrypt_text(plaintext,n):
#     ans = ""
#     # iterate over the given text
#     for i in range(len(plaintext)):
#         ch = plaintext[i]
        
#         # check if space is there then simply add space
#         if ch==" ":
#             ans+=" "
#         # check if a character is uppercase then encrypt it accordingly 
#         elif (ch.isupper()):
#             ans += chr((ord(ch) + n-65) % 26 + 65)
#         # check if a character is lowercase then encrypt it accordingly
        
#         else:
#             ans += chr((ord(ch) + n-97) % 26 + 97)
    
#     return ans

# plaintext = "Zakopane na pokaz"
# n = 10
# print("Plain Text is : " + plaintext)
# print("Shift pattern is : " + str(n))
# print("Cipher Text is : " + encrypt_text(plaintext,n))

#-------------------------------

def szyfr_cezara(tekst, przesuniecie):
    zaszyfrowany_tekst = ""
    for znak in tekst:
        if znak.isalpha():  # Sprawdza, czy znak jest literą
            przesuniecie_znaku = ord(znak) + przesuniecie
            if znak.islower():
                # Dla małych liter
                if przesuniecie_znaku > ord('z'):
                    przesuniecie_znaku -= 26
                elif przesuniecie_znaku < ord('a'):
                    przesuniecie_znaku += 26
            elif znak.isupper():
                # Dla dużych liter
                if przesuniecie_znaku > ord('Z'):
                    przesuniecie_znaku -= 26
                elif przesuniecie_znaku < ord('A'):
                    przesuniecie_znaku += 26
            
            zaszyfrowany_tekst += chr(przesuniecie_znaku)
        else:
            # Jeśli znak nie jest literą, dodaj go bez zmian
            zaszyfrowany_tekst += znak
    
    return zaszyfrowany_tekst

# Przykładowe użycie
tekst = "To jest przykladowy tekst do szyfrowania."
przesuniecie = 3
zaszyfrowany_tekst = szyfr_cezara(tekst, przesuniecie)
print(f"Oryginalny tekst: {tekst}")
print(f"Zaszyfrowany tekst: {zaszyfrowany_tekst}")

