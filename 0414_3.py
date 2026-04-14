class Car():
    def __init__(self, model=None):
        self.model = model

class Tesla(Car):
    def __init__(self, model="Model S", auto_run=True):
        super().__init__(model)
        self.auto_run = auto_run
    def hello(self):
        print("hello")

tesla = Tesla()
print(tesla.model)
print(tesla.auto_run)
tesla.hello()