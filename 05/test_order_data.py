import pytest
from order_data import Customer, VipCustomer, RegularCustomer


def test_get_price():
    assert Customer('Kuba').get_price(100) == 100


def test_vip_get_price():
    assert VipCustomer('Kuba').get_price(100) == 80


def test_regular_get_price():
    assert RegularCustomer('Kuba').get_price(100) == 90
