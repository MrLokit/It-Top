class PositiveNumber:
    def __set_name__(self, owner, name):
        self.public_name = name

    def set_value(self, obj, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f'{self.public_name} must be a positive number')
        obj.__dict__[self.public_name] = value
        print(f'Setting {self.public_name} to {value}')

    def __get__(self, obj, objtype=None):
        value = obj.__dict__[self.public_name]
        print(f'Get value {self.public_name}: {value}')
        return value

class Order:
    product = PositiveNumber()
    price = PositiveNumber()
    quantity = PositiveNumber()

    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

order = Order('apple', 5, 10)
print(f"Order('{order.product}', {order.price}, {order.quantity})")
print()
print(order.total_cost())
