class Human:
    name = ""
    age = 0
    born = ""

    def talk(self):
        print("私の名前は" + self.name + "です。")

    def walk(self):
        print("歩く")

    def sleep(self):
        print("寝る")

taro = Human()
taro.name = "太郎"
taro.age = 20
taro.born = "東京"
taro.talk()