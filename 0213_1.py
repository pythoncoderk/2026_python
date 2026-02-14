class Human:
    def hello(self):
        print("Hello")

class Japanese(Human):
    def hello(self):
        super().hello()
        print("I'm Japanese")

japanese = Japanese()
japanese.hello()
