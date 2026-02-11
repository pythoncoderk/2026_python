class Purchase:

    discount = 0.9

    def __init__(self, price, count):
        self.price = price
        self.count = count

    def total(self):

        return self.price * self.count * self.discount


purchase = Purchase(180, 2)
print(purchase.total())