class Human:
    def __init__(self, name, age, bor):
        self.name = name
        self.age = age
        self.bor = bor

    def talk(self):
        print(self.name + "は話しました。")

    def age2(self):
        print(self.name + "は" + str(self.age) + "歳です。")

    def bor2(self):
        print(self.name + "は" + self.bor + "出身です。")


masashi = Human("まさし", 23, "米国")
masashi.talk()
masashi.age2()

masashi.bor2()
