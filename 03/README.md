> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s8e03-python-oop` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#03` Python: Programowanie obiektowe – dziedziczenie i polimorfizm

W tym zadaniu stworzysz system obsługi różnych metod płatności. Każda forma płatności realizuje metodę `pay(amount)`, ale działa ona inaczej w zależności od klasy. Dzięki temu powtórzysz sobie, czym jest polimorfizm – czyli wspólna metoda dla wielu klas, która może mieć różne zachowanie.

## Co masz zrobić?

1. Stwórz klasę bazową `PaymentMethod`, która zawiera metodę `pay(amount)`.  
   Metoda ta powinna wypisywać:  
   `Zapłacono {amount} zł`

2. Stwórz klasę `CardPayment`, która dziedziczy po `PaymentMethod` i nadpisuje metodę `pay()`.  
   Powinna wypisywać:  
   `Zapłacono kartą: {amount} zł`

3. Stwórz klasę `BlikPayment`, która dziedziczy po `PaymentMethod` i nadpisuje metodę `pay()`.  
   Powinna wypisywać:  
   `Płatność BLIK: {amount} zł (kod jednorazowy)`

4. Stwórz klasę `CashPayment`, która dziedziczy po `PaymentMethod` i nadpisuje metodę `pay()`.  
   Powinna wypisywać:  
   `Zapłacono gotówką: {amount} zł (proszę wydać resztę)`

5. Utwórz listę różnych metod płatności i wywołaj na każdej z nich metodę `pay()` z taką samą kwotą.

## Przykład użycia

```python
payments = [
    CardPayment(),
    BlikPayment(),
    CashPayment()
]

for payment in payments:
    payment.pay(100)
```
## Oczekiwany wynik
```python
Zapłacono kartą: 100 zł 
Płatność BLIK: 100 zł (kod jednorazowy)
Zapłacono gotówką: 100 zł (proszę wydać resztę)
```

```


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-python-oop)*

> :arrow_left: [*poprzednie zadanie*](./../02) | [*następne zadanie*](./../04) :arrow_right:
