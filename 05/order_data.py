from pydantic import BaseModel


class Order(BaseModel):
    customer_name: str
    customer_type: str
    base_price: float


class Customer:

    def __init__(self, name):
        self.name = name

    def get_price(self, base_price):
        return base_price


class RegularCustomer(Customer):

    def get_price(self, base_price):
        return 0.9 * base_price


class VipCustomer(Customer):

    def get_price(self, base_price):
        return 0.8 * base_price
