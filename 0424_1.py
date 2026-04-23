class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("私は", self.name, "です")


p = Person("どんぐり")
p.hello()