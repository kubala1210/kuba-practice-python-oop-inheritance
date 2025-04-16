> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e03-python-oop` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#01` Python: Programowanie obiektowe – dziedziczenie


Twoim zadaniem jest stworzenie systemu zarządzania użytkownikami w aplikacji. Zbudujesz klasę bazową `User`, z której będą dziedziczyć inne typy użytkowników, takie jak `Admin` i `Guest`.

To ćwiczenie ma na celu sprawdzenie, czy potrafisz:

- prawidłowo zaprojektować klasy bazowe i dziedziczące,
- wykorzystywać metody wspólne dla klas potomnych bez ich duplikowania,
- nadpisywać metody w klasach potomnych,
- stosować dobre praktyki w kodzie obiektowym.

## Wymagania

1. Stwórz klasę `User`, która:
   - przyjmuje w konstruktorze `name` i `password`,
   - zawiera metodę `get_display_name()` – zwraca `name` wielkimi literami,
   - zawiera metodę `authorize()` – zwraca `True`, jeśli hasło ma co najmniej 8 znaków.

2. Stwórz klasę `Admin`, która dziedziczy po `User` i:
   - korzysta z metody `authorize()` z klasy bazowej,
   - dodaje metodę `has_access()` – zawsze zwraca `True`.

3. Stwórz klasę `Guest`, która dziedziczy po `User` i:
   - **nadpisuje** metodę `authorize()` – zawsze zwraca `False`,
   - **nie duplikuje** `get_display_name()` – ma korzystać z metody klasy bazowej.

## Przykład użycia

```python
admin = Admin("Kuba", "supersecret")
print(admin.get_display_name())  # "KUBA"
print(admin.authorize())         # True
print(admin.has_access())        # True

guest = Guest("Anna", "123")
print(guest.get_display_name())  # "ANNA"
print(guest.authorize())         # False
```


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-oop)*

> :arrow_left: ~~*poprzednie zadanie*~~ | [*następne zadanie*](./../02) :arrow_right:
