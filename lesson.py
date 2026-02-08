class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto fast')

class NissanCar(TeslaCar):
    pass

car = Car()
car.run()
print("#######################")
toyota_car = ToyotaCar("Lexus")
print(toyota_car.model)
toyota_car.run()
print("#######################")
tesla_car = TeslaCar("Modes S")
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()
print("########################")
nissan = NissanCar()
nissan.auto_run()