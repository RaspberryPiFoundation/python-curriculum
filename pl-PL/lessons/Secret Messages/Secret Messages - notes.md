---
title: Sekretne Wiadomości — Informacje dla prowadzącego
language: pl
embeds: "*.png"
...

#Wprowadzenie:
Ten projekt uczy iterowania po ciągu znaków tekstowych i stworzenia szyfratora cezara.

#Źródła online
Do pisania kodu w języku Python online rekomendujemy używanie edytora (https://trinket.io/).  

W tym projekcie dzieci mogą skorzystać z pustego edytora ([https://trinket.io/python/7c0a7396c0](https://trinket.io/python/7c0a7396c0)), by pisać własny kod.

#Źródła offline
Aby wykonać ten projekt w trybie offline (bez korzystania z platformy trinket.io) konieczne jest, aby na komputerze zainstalowamy był Python (najlepiej w wersji 3.2).

Dzieci mogą też korzystać z materiałów dołączonych do tego projektu. Pliki załączone w katalogu "Project Resources" (do pobrania po kliknięciu w link "Pobierz materiały")

+ Encryption.py

Upewnij się, że każde dziecko ma dostęp do odczytu i zapisu ich kopii materiałów.

Rozwiązane wyzwania dla tego projektu można pobrać klikając link 'Download Project Materials` dla tego projektu, które zawiera:

+ LoveCalculator.py

#Cele dydaktyczne:
+ Iterowanie po ciągu znaków;
+ Metoda `find()`;
+ Operator modulo (`%`).

#Wyzwania
+ Zmienne klucze - pozwól użytkownikowi wprowadzić wartość klucza;
+ Zaszyfruj i odszyfruj litery - szyfrowanie i odszyfrowanie pojedynczych liter;
+ Szyfrowanie i odszyfrowanie wiadomości - szyfrowanie i odszyfrowanie całych wiadomości;
+ Ulepszenie szyfru - modyfikacja programu w taki sposób aby utrudnić złamanie kodu szyfrującego;
+ Kalkulator Miłości - zastosowanie iteracji po ciągu znaków do rozwiązania nowego problemu.

#Często zadawane pytania
+ Podczas wyszukiwania liter metodą `find()` lub `if litera in alfabet:` ważna jest wielkość liter. Uczniowie mogą użyć:

```python
message = input("Prosze wprowadzic wiadomosc do zaszyfrowania: ").lower()
```

aby zamienić wprowadzoną wiadomość na małe litery przed wyszukiwaniem.