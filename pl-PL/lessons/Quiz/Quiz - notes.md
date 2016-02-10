---
title: Quiz — Informacje dla prowadzącego 
language: pl
embeds: "*.png"
...

#Wprowadzenie:
Ten projekt uczy dzieci jak używać warunków (komend `if`, `else` i `elif`) w ich programach tak, żeby zmienić przebieg programu w zależności od danych wejściowych. Osiągamy to przez napisanie i przetestowanie prostego programu quizu, składającego się z tekstu i pytań wielokrotnego wyboru.

# Źródła online
Do pisania kodu w języku Python online rekomendujemy używanie edytora (https://trinket.io/).  

W tym projekcie dzieci mogą skorzystać z pustego edytora ([https://trinket.io/python/7c0a7396c0](https://trinket.io/python/7c0a7396c0)), by pisać własny kod.

# Źródła offline
Aby wykonać ten projekt w trybie offline (bez korzystania z platformy trinket.io) konieczne jest, aby na komputerze zainstalowamy był Python (najlepiej w wersji 3.2).

Dzieci mogą też korzystać z materiałów dołączonych do tego projektu. Pliki załączone w katalogu "Project Resources" (do pobrania po kliknięciu w link "Pobierz materiały")

+ Quiz.py

Upewnij się, że każde z dzieci ma dostęp do odczytu i zapisu ich kopii materiałów.

#Cele dydaktyczne
+ Komendy warunkowe, czyli:
	+ `if`;
	+ `else`;
	+ `elif`.
+ Testowanie programu i rozwiązywanie problemów.

#Wyzwania
+ Czas na pytania - wykorzystać `if` i `else` do wskazania prawidłowej lub błędnej odpowiedzi;
+ Naprawienie swojego quizu - korzystając z motedy `.lower()` zmniejszyć ilość błędów w ocenie odpowiedzi;
+ Pytania wielokrotnego wyboru - korzystając z `elif` dodać pytania z wieloma odpowiedziami;
+ Liczenie punktów - dodanie zmiennej `punkty` do śledzenia wyniku;
+ Jak mi poszło? - dalsze wykorzystanie `if` i `else` do wyświetlenia wiadomości na koncu quizu, opartej na ilości punktów.

#Często zadawane pytania
+ Ponieważ odpowiedzi gracza są wczytywane jako text, każde z pytań z odpowiedzią numeryczną powinno być również reprezentowane jako text. Na przykład:

```python
if odpowiedz == "4":
	...
```

a *nie*:

```python
if odpowiedz == 4:
	...
```

Alternatywą może być konwersja odpowiedzi gracza na liczbę, a potem porównanie arytmetyczne wartości:

```python
odpowiedz = int(answer)
if odpowiedz == 4:
	...
```

+ Każde `if`/`else`/`elif` powinno być zakończone dwukropkiem (:).

+ Ciało każdego z wyrażeń `if`/`else`/`elif` powinno być równo wcięte. Zaleca się wykorzystanie klawisza Tab do tworzenia wcięć, ponieważ ułatwia to zauważenie błędów w indentacji. Na przykład, poniższy program nie będzie działać:

```python
if odpowiedz == "zmienna":
   print("Dobra robota")
  print("---------")
    print(" :) ")
 )
```

+ Dzieci powinny zapamiętać różnicę między `=` (wykorzystywane go przypisania zmiennych) i `==` (używanego do sprawdzania równości).
