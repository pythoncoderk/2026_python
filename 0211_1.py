class Item:

    tax_rate = 0.1

    def __init__(self, price):
        self.price = price

    def price_with_tax(self, tax_in):
        self.tax_in = tax_in
        tax_in = self.price * self.tax_rate
        return tax_in

item = Item(100)
print(item.price_with_tax())

