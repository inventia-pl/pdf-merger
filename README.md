# pdf-merger
Program z prostym gui stworzony do łatwej edycji plików pdf.

### Uruchomienie
Pobierz całe repozytorium. Następnie wejdź w plik **"dist"** następnie w **"merge"**, kliknij dwukrotnie **merge.exe** i wyświetli się małe szare okienko z 5 przyciskami:
* Połącz pliki pdf 
* Edytuj plik pdf
* Otówrz folder
* Otwórz plik
* Wróć

Trzy ostatnie opcje są wyszarzone i nie dostępne. 
#### Łączenie plików pdf
Naciśnij *Połącz pliki pdf* następnie *Otwórz folder* i nawiguj w menu do folderu z plikami pdf, które chcesz połączyć w jeden plik. Po wybraniu folderu, program poinformuje o znalezionych plikach i wyświetli ich nazwy. Program wyświetli informację w przypadku braku plików .pdf.
Następnie naciśnij *Połącz pliki* i zaczekaj. Przy dużej ilości plików z wieloma stronami program "przestanie na chwilę odpowiadać". (Dla 2000 stron program "zacina się" na minutę). Po udanej operacji program wyświetli informację z lokacją nowo stworzonego pliku.

**Uwaga** 
W okienku wyboru folderów (tj. eksploratorze windows) nie będzie widać zawartości folderów, czyli plików, które się w nich znajdują.

#### Edycja plików pdf
Naciśnij *Edytuj plik pdf* następnie *Otwórz plik*, wybierz plik pdf. Program wyświetli informację o wybranym pliku oraz pokaże dwie nowe opcje. 
* Usuń wybrane strony
* Usuń zbiór

Obie usuwają strony z pliku pdf. *Usuń wybrane strony* wyświetla pole, w którym po przecinku bez spacji wypisujesz strony, które chcesz usunąć z pliku pdf: 
```
66,891,14,51,7,90
```
*Usuń zbiór* pozwala na masowe usunięcie strone pomiędzy dwoma stronami, włączając te wypisane:
> od: 8
> do: 17

Usunie strony od 8 do 17, włączając 8. i 17. <br />

Bez względu, na wybraną opcję, pojawi się przycisk *ok*. Po naciśnięciu wyświetli menu, które pozwoli na wybranie ścieżki oraz nazwy nowego pliku. 

#### Wróć
Przywraca program do początkowego stanu.


