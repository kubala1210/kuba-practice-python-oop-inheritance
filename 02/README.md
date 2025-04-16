> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e03-python-oop` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#02` Python: Programowanie obiektowe – dziedziczenie

W tym zadaniu poznasz nowe pojęcie, jakim jest **atrybut klasowy**.

Atrybut klasowy to zmienna, która należy do całej klasy, a nie tylko do pojedynczego obiektu. Oznacza to, że wszystkie obiekty danej klasy mają dostęp do tej samej wartości. Jeśli atrybut klasowy zostanie zmieniony, zmiana będzie widoczna we wszystkich instancjach tej klasy.

**Atrybut klasowy zapisujemy bez `self`.**  
Tworzymy go bezpośrednio wewnątrz klasy:

```python
class User:
    total_users = 0  # atrybut klasowy
```

Z kolei atrybut instancyjny, który jest unikalny dla każdego obiektu, przypisujemy za pomocą `self` w metodzie `__init__`:

```python
def __init__(self, name):
    self.name = name  # atrybut instancyjny
```
## Co masz zrobić?
Stwórz klasę User, która:

1. posiada atrybut klasowy total_users = 0,

2. w metodzie __init__ przyjmuje argument name, zapisuje go jako self.name,

3. za każdym razem, gdy tworzony jest nowy obiekt klasy User, zwiększa wartość User.total_users o 1.

4. Stwórz klasy Admin i Guest, które dziedziczą po User:

- Nie kopiuj kodu z User, tylko korzystaj z dziedziczenia,

- w konstruktorze (__init__) ustaw dodatkowo self.role = "admin" lub self.role = "guest".

## Przykład użycia

```python
admin = Admin("Ola")
guest = Guest("Ania")
user = User("Jan")

print(User.total_users)  # 3
print(admin.name, admin.role)  # Ola admin
print(guest.name, guest.role)  # Ania guest

```


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-oop)*

> :arrow_left: [*poprzednie zadanie*](./../01) | [*następne zadanie*](./../03) :arrow_right:
