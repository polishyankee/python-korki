w1 =6
w2 =7
licznik = 0
while w1 != w2:
    if w1 > w2:
        w1 = w1 // 2 
    else:
        w2 = w2 // 2
    licznik += 1
print(licznik)