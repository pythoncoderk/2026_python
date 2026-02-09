class Order(object):
    def __init__(self, price, count, tax):
        self.price = price
        self.count = count
        self.tax = 1.1

    def total_price(self):
        price 

order = Order()
print(order.price * order.count * order.tax)

