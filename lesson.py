class Car(object):
    def run(self):
        print("run")

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print("auto_run")

car = Car()
car.run()
print("##################")
toyota = ToyotaCar()
toyota.run()
print("##################")
tesla = TeslaCar()
tesla.run()
tesla.auto_run()