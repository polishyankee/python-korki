## Open()

Kluczową funkcją do pracy z plikami w Pythonie jest funkcja open().
Funkcja open() przyjmuje dwa parametry; nazwę pliku i tryb.
Istnieją cztery różne metody (modes) otwierania pliku:

* "r" - Read - Default value. Opens a file for reading, error if the file does not exist
* "a" - Append - Opens a file for appending, creates the file if it does not exist
* "w" - Write - Opens a file for writing, creates the file if it does not exist
* "x" - Create - Creates the specified file, returns an error if the file exists


```
f = open("demofile.txt", "r")
print(f.read())
```

Aby zapisać do istniejącego pliku, musisz dodać parametr do funkcji open():

* "a"- Dołącz - dołączy do końca pliku
* "w"- Napisz - zastąpi każdą istniejącą zawartość

```
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
```


### Utwórz nowy plik

Aby utworzyć nowy plik w Pythonie, użyj metody open() z jednym z następujących parametrów:

* "x"- Utwórz - utworzy plik, zwraca błąd, jeśli plik istnieje
* "a"- Dołącz - utworzy plik, jeśli określony plik nie istnieje
* "w"- Napisz - utworzy plik, jeśli określony plik nie istnieje


f = open("myfile.txt", "x")

### Usuń plik

Aby usunąć plik, musisz zaimportować moduł systemu operacyjnego i uruchomić jego funkcję os.remove():

```
import os
os.remove("demofile.txt")
```

```
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
```

Aby usunąć folder 

```
  import os
os.rmdir("myfolder")
```