from order_data import Order, RegularCustomer, VipCustomer

order_data = {
    "customer_name": "Ola",
    "customer_type": "regular",
    "base_price": '200.0'
}

order = Order(**order_data)
if order.customer_type == 'vip':
    customer = VipCustomer(order.customer_name)
    print('VIP created')
if order.customer_type == 'regular':
    customer = RegularCustomer(order.customer_name)
    print('Regular customer created')
