class Hero:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"私は{self.name}です")


hero = Hero("勇者タロウ")
print(hero.name)

hero.introduce()


