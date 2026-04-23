class VendingMachine:
    def __init__(self):
        self.money = 0

    def insert(self, yen):
        self.money += yen

    def show(self):
        print(self.money)

v = VendingMachine()
v.insert(100)
v.insert(50)
v.show()

