class Order:
    tax = 1.1

    def __init__(self, price, count):
        self.price = price
        self.count = count

    def total_price(self):
        total = self.price * self.count * Order.tax
        total = int(total)
        print("合計金額は" + str(total) + "円です。")

order1 = Order(price=100, count=10)
order1.total_price()