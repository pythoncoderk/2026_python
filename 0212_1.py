class Order:

    tax = 1.1

    def __init__(self, price, count):
        self.price = price
        self.count = count

    def total_price(self):
        return int(self.price * self.count * self.tax)

order = Order(100, 10)
print(order.total_price())

order = Order(128, 8)
print(order.total_price())

