class Order:
    tax = 1.1

    def __init__(self, price, count):
        self.price = price
        self.count = count

    def total_price(self):
        return int(self.price * self.count * Order.tax)


order = Order(100, 10)
print(order.total_price())

order2 = Order(128, 8)
print(order2.total_price())

