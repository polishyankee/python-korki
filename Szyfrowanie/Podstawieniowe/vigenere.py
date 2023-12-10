def szyfr_vigenere(napis, klucz, alfabet):
    zakodowany = ""
    napis = napis.upper()
    klucz = klucz.upper()
    for i in range(len(napis)):
        pozycja_n = alfabet.find(napis[i])
        pozycja_k = alfabet.find(klucz[i % len(klucz)])
        pozycja_z = (pozycja_n + pozycja_k) % len(alfabet)
        zakodowany += alfabet[pozycja_z]
    return zakodowany

def odk_szyfr_vigenere(napis, klucz, alfabet):
    odkodowany = ""
    napis = napis.upper()
    klucz = klucz.upper()
    for i in range(len(napis)):
        pozycja_n = alfabet.find(napis[i])
        pozycja_k = alfabet.find(klucz[i % len(klucz)])
        pozycja_z = (pozycja_n - pozycja_k) % len(alfabet)
        odkodowany += alfabet[pozycja_z]
    return odkodowany

podaj = str(input("Wybierz: Zakoduj/Odkoduj: "))
alfabet_lacinski = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

match podaj:
    case "Zakoduj":
        napis_do_zakodowania = input("Wpisz tekst do zakodowania: ")
        klucz_do_zakodowania = input("Wpisz klucz: ")
        print("Zakodowany tekst:", szyfr_vigenere(napis_do_zakodowania, klucz_do_zakodowania, alfabet_lacinski))

    case "Odkoduj":
        napis_do_odkodowania = input("Wpisz tekst do odkodowania: ")
        klucz_do_odkodowania = input("Wpisz klucz: ")
        print("Odkodowany tekst:", odk_szyfr_vigenere(napis_do_odkodowania, klucz_do_odkodowania, alfabet_lacinski))

    case _:
        print("Błędna czynność")



#------------------------

def szyfr_vigenere(napis, klucz, alfabet):
    zakodowany = ""
    napis = napis.upper()
    klucz = klucz.upper()
    for i in range(len(napis)):
        if napis[i].isalpha():
            pozycja_n = alfabet.find(napis[i])
            pozycja_k = alfabet.find(klucz[i % len(klucz)])
            pozycja_z = (pozycja_n + pozycja_k) % len(alfabet)
            zakodowany += alfabet[pozycja_z]
        else:
            zakodowany += napis[i]
    return zakodowany

def odk_szyfr_vigenere(napis, klucz, alfabet):
    odkodowany = ""
    napis = napis.upper()
    klucz = klucz.upper()
    for i in range(len(napis)):
        if napis[i].isalpha():
            pozycja_n = alfabet.find(napis[i])
            pozycja_k = alfabet.find(klucz[i % len(klucz)])
            pozycja_z = (pozycja_n - pozycja_k) % len(alfabet)
            odkodowany += alfabet[pozycja_z]
        else:
            odkodowany += napis[i]
    return odkodowany

podaj = str(input("Wybierz: Zakoduj/Odkoduj "))
alfabet_lacinski = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

match podaj:
    case "Zakoduj":
        napis_do_zakodowania = str(input("Podaj tekst do zakodowania: "))
        klucz_do_zakodowania = str(input("Podaj klucz: "))
        print(szyfr_vigenere(napis_do_zakodowania, klucz_do_zakodowania, alfabet_lacinski))
    case "Odkoduj":
        napis_do_odkodowania = str(input("Podaj tekst do odkodowania: "))
        klucz_do_odkodowania = str(input("Podaj klucz: "))
        print(odk_szyfr_vigenere(napis_do_odkodowania, klucz_do_odkodowania, alfabet_lacinski))
    case _:
        print("Błędna czynność")
