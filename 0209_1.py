class Human:
    def __init__(self, name, age, born):
        self.name = name
        self.age = age
        self.born = born

    def talk(self):
        print("私は" + self.name + "です")

    def walk(self):
        print("歩く")

    def sleep(self):
        print("寝る")

hanako = Human("花子", 30, "大阪")
hanako.talk()