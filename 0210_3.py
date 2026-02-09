class Order:

    tax = 1.1

    def __init__(self, price, count):

        self.price = price
        self.count = count

    def total_price(self):
        total = self.price * self.count
        return int(total + (total * self.tax))

order = Order(300, 2)
print(order.total_price())
