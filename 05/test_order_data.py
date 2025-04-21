import pytest
from order_data import Customer, VipCustomer, RegularCustomer

@pytest.fixture
def mock_customer():
    return Customer('Kuba')

def test_get_price(mock_customer):
    assert mock_customer.get_price(100) == 100

@pytest.fixture
def mock_vip():
    return VipCustomer('Kuba')

def test_vip_get_price(mock_vip):
    assert mock_vip.get_price(100) == 80

@pytest.fixture
def mock_regular():
    return RegularCustomer('Kuba')

def test_regular_get_price(mock_regular):
    assert mock_regular.get_price(100) == 90


