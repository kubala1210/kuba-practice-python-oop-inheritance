import pytest
from zadanie_03 import PaymentMethod, CardPayment, BlikPayment, CashPayment

# ZASTANAWIAM SIĘ CZY JEST SENS TWORZYĆ TUTAJ FIXTURES,
# CZY NIE WYSTARCZY STWORZYĆ INSTANCJI DANEJ KLASY W METODZIE TESTOWEJ I TAK SPRAWDZAĆ WYNIK?

@pytest.fixture
def mock_payment_data():
    return PaymentMethod()

def test_pay(mock_payment_data):
    assert mock_payment_data.pay(100) == 'Zapłacono 100 zł'

@pytest.fixture
def mock_cardpayment_data():
    return CardPayment()

def test_card(mock_cardpayment_data):
    assert mock_cardpayment_data.pay(100) == 'Zapłacono kartą 100 zł'

@pytest.fixture
def mock_blikpayment_data():
    return BlikPayment()

def test_blik(mock_blikpayment_data):
    assert mock_blikpayment_data.pay(100) == 'Zapłacono blikiem 100 zł (kod jednorazowy)'

@pytest.fixture
def mock_cashpayment_data():
    return CashPayment()

def test_cash(mock_cashpayment_data):
    assert mock_cashpayment_data.pay(100) == 'Zapłacono gotówką 100 zł (proszę wydać resztę)'
