dane = []
with open('C:/Users/Uczeń.STANOWISKO-12/Desktop/Dane/liczby.txt') as file:
    lines = file.readlines()
    for line in lines:
        dane.append(line.strip())
slownik = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
slownik_cyfr = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,}
for i in range(len(dane)):
    wynik = ''
    liczba = dane[0]
    while liczba > 0: # w tym miejscu wywala błąd rozumiem go ale niewiem jak go poprawic
        reszta = liczba % 16
        liczba = liczba // 16
        if reszta > 9:
            wynik = slownik[reszta] + wynik
        else:
            wynik = str(reszta) + wynik
    for znak in wynik:
        slownik_cyfr[znak] += 1
    print(slownik_cyfr)

    