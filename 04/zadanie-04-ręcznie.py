class Order:

    def __init__(self, user_id, product, quantity, price):
        self.user_id = user_id
        self.product = product
        self.quantity = quantity
        self.price = price

    def user_id_check(self):
        if not isinstance(self.user_id, int):
            raise TypeError('User ID must be integer')
        else:
            return True

    def quantity_check(self):
        if not self.quantity >= 1:
            raise ValueError('Quantity must be greater than 0')
        return True


valid_data = {
    "user_id": 123,
    "product": "monitor",
    "quantity": 2,
    "price": 899.99
}

order_2 = Order(**valid_data)
print(order_2.quantity_check())
print(order_2.user_id_check())

invalid_data = {
    "user_id": "abc",
    "product": "monitor",
    "quantity": 2,
    "price": 899.99
}

order = Order(**invalid_data)
order.user_id_check()
