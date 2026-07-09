class Cat:

    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"私は{self.name}です")

cat1 = Cat("タマ")
cat2 = Cat("ミケ")

cat1.hello()
cat2.hello()