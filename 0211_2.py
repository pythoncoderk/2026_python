import math

class Item:

    tax_rate = 0.1

    def __init__(self, price):
        self.price = price

    def price_with_tax(self):
        total = self.price * (1 + self.tax_rate)
        return math.ceil(total)

item = Item(100)
print(item.price_with_tax())