class PaymentMethod:

    def pay(self, amount):
        return f'Zapłacono {amount} zł'

class CardPayment(PaymentMethod):

    def pay(self, amount):
        return f'Zapłacono kartą {amount} zł'

class BlikPayment(PaymentMethod):

    def pay(self, amount):
        return f'Zapłacono blikiem {amount} zł (kod jednorazowy)'

class CashPayment(PaymentMethod):

    def pay(self, amount):
        return f'Zapłacono gotówką {amount} zł (proszę wydać resztę)'

payments = [
    CardPayment(),
    BlikPayment(),
    CashPayment(),
]

for payment in payments:
    print(payment.pay(100))