from pydantic import BaseModel, PositiveInt


class Order(BaseModel):
    user_id: int
    product: str
    quantity: PositiveInt
    price: float


valid_data = {
    "user_id": 123,
    "product": "monitor",
    "quantity": 2,
    "price": 899.99
}

data = {
    "user_id": "abc",
    "product": "monitor",
    "quantity": -2,
    "price": 899.99
}

order = Order(**data)
