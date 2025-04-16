> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e03-python-oop` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#05` Python: Dziedziczenie, polimorfizm i walidacja danych

W tym zadaniu utrwalisz wiedzę o dziedziczeniu i polimorfizmie, a także wykorzystasz bibliotekę `pydantic` do walidacji danych wejściowych.

## Cel

Zbudujesz prosty system, który:

- waliduje dane zamówienia (z użyciem `pydantic`),
- obsługuje różnych klientów (`Regular` i `VIP`),
- oblicza końcową cenę zamówienia na podstawie typu klienta.


## Co masz zrobić?

### 1. Stwórz klasę `Order`, która dziedziczy po `pydantic.BaseModel`.  
Powinna zawierać:

- `customer_name: str`
- `customer_type: str`
- `base_price: float`

### 2. Stwórz klasę `Customer`, która:

- przyjmuje w konstruktorze `name`,
- zawiera metodę `get_price(self, base_price)`, która zwraca cenę bez rabatu.

### 3. Stwórz klasy dziedziczące po `Customer`:

- `RegularCustomer` – nadpisuje `get_price`, daje 10% rabatu,
- `VipCustomer` – nadpisuje `get_price`, daje 20% rabatu.

### 4. W kodzie głównym:

- przygotuj słownik `order_data`,
- utwórz obiekt `Order(**order_data)`,
- sprawdź `customer_type` i utwórz odpowiedniego klienta (`RegularCustomer` lub `VipCustomer`),
- wywołaj metodę `get_price()` i wypisz końcową cenę.


## Przykład danych wejściowych

```python
order_data = {
    "customer_name": "Ola",
    "customer_type": "vip",
    "base_price": 200.0
}
```
## Przykład działania

```Python

order = Order(**order_data)

if order.customer_type == "vip":
    customer = VipCustomer(order.customer_name)
elif order.customer_type == "regular":
    customer = RegularCustomer(order.customer_name)

final_price = customer.get_price(order.base_price)
print(final_price)  # 160.0

```

&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-oop)*

> :arrow_left: [*poprzednie zadanie*](./../04) | ~~*następne zadanie*~~ :arrow_right:
