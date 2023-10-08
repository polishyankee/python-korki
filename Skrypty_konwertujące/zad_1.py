dane=[]
counter=0
array=[]
licznik=0
with open("dane.txt") as file:
    lines= file.readlines()
    for line in lines:
        array.append(line.split())
        dane.append([array[counter][0],array[counter][1],array[counter][2]])
        counter+=1
print(dane)

licznikdane=0
while licznikdane<len(dane):
    liczbap=dane[licznik][0]
    systemp=int(dane[licznik][1])
    system=int(dane[licznik][2])
    marker=True
    liczbaps=str(liczbap)
    liczba=0
    potega=0
    slownikp={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    i=0
    a=len(liczbaps)-1
    while i<len(liczbaps):
        if liczbaps[a]=='-':
            marker=False
            break
        if liczbaps[a]=='A' or liczbaps[a]=='B' or liczbaps[a]=='C' or liczbaps[a]=='D' or liczbaps[a]=='E' or liczbaps[a]=='F':
            liczba=liczba+slownikp[liczbaps[a]]
            systemp**potega
        else:
            liczba=liczba+int(liczbaps[a])
            systemp**potega
        a=a-1
        potega=potega+1
        i=i+1
    wynik=""
    slownik={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    while liczba>0:
        reszta=liczba%system
        liczba=liczba//system
        if reszta>9:
            wynik=slownik[reszta]+wynik
        else:
            wynik=str(reszta)+wynik
    if marker==False:
        wynik = '-'+wynik
    print(wynik)
    licznikdane=licznikdane+1
    licznik=licznik+1