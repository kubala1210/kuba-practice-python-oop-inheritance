> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e03-python-oop` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;
# `#04` Python: Klasy danych, dziedziczenie i walidacja – jak działa pydantic?

W tym zadaniu poznasz narzędzie `pydantic`, które pozwala bardzo łatwo tworzyć klasy danych i automatycznie sprawdzać poprawność danych wejściowych.  
Dowiesz się też, dlaczego to działa – i jak klasa `BaseModel` wpływa na zachowanie Twojej klasy.

## Wprowadzenie

W Pythonie klasy mogą **dziedziczyć** po innych klasach – oznacza to, że mogą **automatycznie przejąć metody i zachowanie klasy nadrzędnej**.  
W przypadku `pydantic`, Twoja klasa dziedziczy po `BaseModel`, która dostarcza:

- automatyczny konstruktor `__init__`,
- walidację danych na podstawie typów (`int`, `str`, itd.),
- przydatne metody `.dict()` i `.json()`.

Więcej o `pydantic` przeczytasz w dokumentacji:  
https://docs.pydantic.dev/latest/


## Co masz zrobić?

### Krok 1 – Ręczna klasa `Order`

Stwórz klasę `Order` w zwykły sposób, bez `pydantic`.  
Twoja klasa powinna:

- przyjmować `user_id`, `product`, `quantity`, `price` w metodzie `__init__`,
- zapisywać je jako atrybuty instancyjne (`self.user_id`, ...),
- sprawdzać typ `user_id` (czy to `int`) – jeśli nie, podnieś `TypeError`,
- sprawdzać, czy `quantity` ≥ 1 – jeśli nie, podnieś `ValueError`.

Przykład danych wejściowych:

```python
data = {
    "user_id": "abc",   
    "product": "monitor",
    "quantity": 2,
    "price": 899.99
}
```

## Krok 2 – Stwórz klasę `Order` z pydantic

Zamiast pisać `__init__` i walidację, napisz:

```python
from pydantic import BaseModel

class Order(BaseModel):
    user_id: int
    product: str
    quantity: int
    price: float
```

I użyj danych:

```python
data = {
    "user_id": "abc",
    "product": "monitor",
    "quantity": 2,
    "price": 899.99
}

order = Order(**data)
```

## Krok 3 – Porównanie

Odpowiedz sobie:

- Co musiałeś pisać ręcznie w zwykłej klasie?
- Co zrobił za Ciebie `pydantic`?
- Co się stanie, jeśli dane są nieprawidłowe?

## Cel ćwiczenia

Zrozumieć, że `pydantic`:
- tworzy `__init__` za Ciebie,
- sprawdza typy danych automatycznie,
- wyrzuca czytelne błędy (`ValidationError`),
- pozwala szybko tworzyć „inteligentne klasy danych”.

## Bonus. Rozpakowywanie słownika za pomocą **
W wyrażeniu:

```python
order = Order(**data)
```
gwiazdki ** oznaczają rozpakowywanie słownika do argumentów nazwanych.

Jeśli masz:

```python
data = {
    "user_id": 1,
    "product": "monitor",
    "quantity": 2,
    "price": 899.99
}
```
to Order(**data) jest równoważne z:

```python

Order(user_id=1, product="monitor",quantity=2, price=899.99)
```
To działa tylko wtedy, gdy klucz w słowniku = nazwa parametru w konstruktorze.

&nbsp;

> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-oop)*

> :arrow_left: [*poprzednie zadanie*](./../03) | [*następne zadanie*](./../05) :arrow_right:
