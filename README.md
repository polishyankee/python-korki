# python-korki

## Definiowanie zmiennych w Pythonie

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

Python nie ma polecenia do deklarowania zmiennej.
Zmienna jest tworzona w momencie, gdy po raz pierwszy przypiszesz do niej wartość.

```
x = 5
y = "John"
print(x)
print(y)
```

Jeśli chcesz określić typ danych zmiennej, można to zrobić za pomocą rzutowania.

```
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```

Python pozwala przypisać wartości do wielu zmiennych w jednym wierszu:

```
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```

I możesz przypisać tę samą wartość do wielu zmiennych w jednym wierszu:

```
x = y = z = "Orange"
print(x)
print(y)
print(z)
```

## Metody Pythona 


### Dodanie do listy 

Aby dodać element na końcu listy, użyj metody append():

```
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
```

Aby wstawić element listy o określonym indeksie, użyj metody insert()

```
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
```

Aby dodać elementy z innej listy do bieżącej listy, użyj metody extend().Elementy zostaną dodane na końcu listy.

```
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
```

### Usunięcie z listy 

Metoda remove() usuwa określony element.
Jeśli jest więcej niż jeden element o określonej wartości, metoda remove() usuwa pierwsze wystąpienie:

```
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
```

Metoda pop() usuwa określony indeks.
Jeśli nie określisz indeksu, metoda pop() usunie ostatni element.

```
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
```

Metoda del:

Słowo kluczowe del usuwa również określony indeks.
Słowo kluczowe del może również całkowicie usunąć listę.

```
thislist = ["apple", "banana", "cherry"]
del thislist
```
