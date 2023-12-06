# def encrypt(text,s):
# result = ""
#    # transverse the plain text
#    for i in range(len(text)):
#       char = text[i]
#       # Encrypt uppercase characters in plain text
      
#       if (char.isupper()):
#          result += chr((ord(char) + s-65) % 26 + 65)
#       # Encrypt lowercase characters in plain text
#       else:
#          result += chr((ord(char) + s - 97) % 26 + 97)
#       return result
# #check the above function
# text = "CEASER CIPHER DEMO"
# s = 4

# print "Plain Text : " + text
# print "Shift pattern : " + str(s)
# print "Cipher: " + encrypt(text,s)


# message = 'CEASER CIPHER DEMO' #encrypted message
# LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# for key in range(len(LETTERS)):
#    translated = ''
#    for symbol in message:
#       if symbol in LETTERS:
#          num = LETTERS.find(symbol)
#          num = num - key
#          if num < 0:
#             num = num + len(LETTERS)
#          translated = translated + LETTERS[num]
#       else:
#          translated = translated + symbol
# print('Hacking key #%s: %s' % (key, translated))

# message = 'UDZ WKLV VLGH' #encrypted message
# Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# for key in range(len(Letters)):
#    translated = ''
#    for ch in message:
#       if ch in Letters:
#          num = Letters.find(ch)
#          num = num - key
#          if num < 0:
#             num = num + len(Letters)
#          translated = translated + Letters[num]
#       else:
#          translated = translated + ch
#    print('Hacking key is %s: %s' % (key, translated))

def zlam_szyfr_cezara(zaszyfrowany_tekst):
    for przesuniecie in range(26):
        odszyfrowany_tekst = ""
        for znak in zaszyfrowany_tekst:
            if znak.isalpha():
                przesuniecie_znaku = ord(znak) - przesuniecie
                if znak.islower():
                    if przesuniecie_znaku < ord('a'):
                        przesuniecie_znaku += 26
                elif znak.isupper():
                    if przesuniecie_znaku < ord('A'):
                        przesuniecie_znaku += 26
                odszyfrowany_tekst += chr(przesuniecie_znaku)
            else:
                odszyfrowany_tekst += znak
        
        print(f"Przesunięcie: {przesuniecie}, Odszyfrowany tekst: {odszyfrowany_tekst}")

# Przykład użycia
zaszyfrowany_tekst = "Wr mhvw sucbnodgrzb whnvw gr vcbiurzdqld." 
zlam_szyfr_cezara(zaszyfrowany_tekst)
